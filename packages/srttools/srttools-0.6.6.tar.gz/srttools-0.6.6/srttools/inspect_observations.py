"""Read the relevant information and link observations to calibrators."""

import warnings
from collections.abc import Iterable
import numpy as np
from astropy.table import Table, Column
from astropy.time import Time
import logging
from .io import read_data, chan_re
from .scan import list_scans, _is_summary_file
from .calibration import read_calibrator_config
from .read_config import sample_config_file
from .utils import remove_suffixes_and_prefixes

try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser

__all__ = [
    "inspect_directories",
    "split_observation_table",
    "split_by_source",
    "dump_config_files",
]


def inspect_directories(
    directories, only_after=None, only_before=None, ignore_suffix=[], ignore_prefix=[]
):
    import datetime

    info = Table()
    names = [
        "Dir",
        "Sample File",
        "Source",
        "Receiver",
        "Backend",
        "Time",
        "Frequency",
        "Bandwidth",
        "is_skydip",
    ]

    dtype = [
        "S200",
        "S200",
        "S200",
        "S200",
        "S200",
        np.double,
        float,
        float,
        bool,
    ]

    for n, d in zip(names, dtype):
        if n not in info.keys():
            info.add_column(Column(name=n, dtype=d))

    if only_after is not None:
        only_after = Time(
            datetime.datetime.strptime(only_after, "%Y%m%d-%H%M%S"),
            scale="utc",
        ).mjd
        logging.info("Filtering out observations before " "MJD {}".format(only_after))
    if only_before is not None:
        only_before = Time(
            datetime.datetime.strptime(only_before, "%Y%m%d-%H%M%S"),
            scale="utc",
        ).mjd
        logging.info("Filtering out observations after " "MJD {}".format(only_before))

    for d in directories:
        fits_files = list_scans(".", [d])
        for f in fits_files:
            if _is_summary_file(f):
                continue
            logging.info("Reading {}".format(f))
            try:
                data = read_data(f)
                time_start = data[0]["time"]
                time_end = data[-1]["time"]

                elevation = data["el"]
                # If range of elevation change is more than 60 degrees,
                # this is a skydip.
                is_skydip = np.max(elevation) - np.min(elevation) > np.pi / 3.0

                if only_after is not None and time_start < only_after:
                    continue
                if only_before is not None and time_end > only_before:
                    continue

                backend = data.meta["backend"]
                receiver = data.meta["receiver"]
                chan = [ch for ch in data.colnames if chan_re.search(ch)][0]
                frequency = data[chan].meta["frequency"]
                bandwidth = data[chan].meta["bandwidth"]
                source = remove_suffixes_and_prefixes(
                    data.meta["SOURCE"], suffixes=ignore_suffix, prefixes=ignore_prefix
                )

                info.add_row(
                    [
                        d,
                        f,
                        source,
                        receiver,
                        backend,
                        time_start,
                        frequency,
                        bandwidth,
                        is_skydip,
                    ]
                )
                break
            except Exception as e:
                warnings.warn("Errors while opening {}".format(f))
                warnings.warn(str(e))
                continue

    return info


def split_observation_table(
    info, max_calibrator_delay=0.4, max_source_delay=0.2, group_by_entries=None
):
    if group_by_entries is None:
        group_by_entries = ["Receiver", "Backend"]
    grouped_table = info.group_by(group_by_entries)

    indices = grouped_table.groups.indices

    groups = {}
    for i, ind in enumerate(zip(indices[:-1], indices[1:])):
        start_row = grouped_table[ind[0]]
        logging.info(
            "Group {}, Backend = {}, "
            "Receiver = {}".format(i, start_row["Backend"], start_row["Receiver"])
        )
        s = split_by_source(
            grouped_table[ind[0] : ind[1]],
            max_calibrator_delay=max_calibrator_delay,
            max_source_delay=max_source_delay,
        )

        label = ",".join([start_row[e] for e in group_by_entries])

        groups[label] = s

    return groups


def split_by_source(info, max_calibrator_delay=0.4, max_source_delay=0.2):
    cal_config = read_calibrator_config()
    calibrators = cal_config.keys()

    sources = list(set(info["Source"]))
    # Find observation blocks of a given source
    retval = {}
    for s in sources:
        if s in calibrators:
            continue
        condition = info["Source"] == s
        filtered_table = info[condition]
        if np.any(filtered_table["is_skydip"]):
            continue
        s = s
        retval[s] = {}

        start_idxs = []
        end_idxs = []
        for i, f in enumerate(filtered_table):
            if i == 0:
                start_idxs.append(0)
                continue
            if f["Time"] - filtered_table[i - 1]["Time"] > max_source_delay:
                start_idxs.append(i)
                end_idxs.append(i)
        end_idxs.append(len(filtered_table))

        contiguous = list(zip(start_idxs, end_idxs))

        for i, cont in enumerate(contiguous):
            retval[s]["Obs{}".format(i)] = {}
            print("---------------")
            print("{}, observation {}\n".format(s, i + 1))
            ft = filtered_table[cont[0] : cont[1]]

            observation_start = ft[0]["Time"]
            observation_end = ft[-1]["Time"]

            print("Source observations:")
            retval[s]["Obs{}".format(i)]["Src"] = []
            for c in range(cont[0], cont[1]):
                print(filtered_table[c]["Dir"])
                retval[s]["Obs{}".format(i)]["Src"].append(filtered_table[c]["Dir"])

            print("")
            print("Calibrator observations:")
            retval[s]["Obs{}".format(i)]["Cal"] = []

            condition1 = np.abs(info["Time"] - observation_start) < max_calibrator_delay
            condition2 = np.abs(info["Time"] - observation_end) < max_calibrator_delay
            condition = condition1 & condition2

            for row in info[condition]:
                if row["Source"] in calibrators:
                    print(row["Dir"])
                    retval[s]["Obs{}".format(i)]["Cal"].append(row["Dir"])

            print("")
            print("Skydip observations:")

            retval[s]["Obs{}".format(i)]["Skydip"] = []

            condition1 = np.abs(info["Time"] - observation_start) < max_calibrator_delay
            condition2 = np.abs(info["Time"] - observation_end) < max_calibrator_delay
            condition = condition1 & condition2

            for row in info[condition]:
                if row["is_skydip"]:
                    print(row["Dir"])
                    retval[s]["Obs{}".format(i)]["Skydip"].append(row["Dir"])

            print("")
            print("---------------\n")
    return retval


def dump_config_files(info, group_by_entries=None, options=None):
    observation_dict = split_observation_table(info, group_by_entries=group_by_entries)
    config_files = []
    for label in observation_dict.keys():
        group = observation_dict[label]

        for sourcelabel in group.keys():
            source = group[sourcelabel]
            for obslabel in source.keys():
                obs = source[obslabel]
                srcdata = obs["Src"]
                caldata = obs["Cal"]
                skydata = obs["Skydip"]

                filename = "{}_{}_{}.ini".format(label.replace(",", "_"), sourcelabel, obslabel)
                fname = sample_config_file()
                config = ConfigParser()
                config.read(fname)
                if len(srcdata) > 0:
                    config.set(
                        "analysis",
                        "list_of_directories",
                        "\n" + "\n".join(srcdata),
                    )

                if len(caldata) > 0:
                    config.set(
                        "analysis",
                        "calibrator_directories",
                        "\n" + "\n".join(caldata),
                    )

                if len(skydata) > 0:
                    config.set(
                        "analysis",
                        "skydip_directories",
                        "\n" + "\n".join(skydata),
                    )

                if options is not None:
                    for k in options.keys():
                        val = options[k]
                        if isinstance(val, Iterable) and not isinstance(val, str):
                            val = "\n" + "\n".join(val)
                        config.set("analysis", k, val)
                config.write(open(filename, "w"))
                config_files.append(filename)

    return config_files


def main_inspector(args=None):
    import ast
    import argparse

    description = (
        "From a given list of directories, read the relevant "
        "information and link observations to calibrators. A single"
        " file is read for each directory."
    )
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(
        "directories",
        nargs="+",
        help="Directories to inspect",
        default=None,
        type=str,
    )
    parser.add_argument("-g", "--group-by", default=None, type=str, nargs="+")
    parser.add_argument(
        "--options",
        default=None,
        type=str,
        help="Options to be written in config files; they have"
        " to be specified as a string defining a "
        "dictionary. For example,"
        '\'{"pixel_size": 0.6, '
        '"noise_threshold": 5}\' ',
    )
    parser.add_argument("-d", "--dump-config-files", action="store_true", default=False)
    parser.add_argument(
        "--only-after",
        type=str,
        default=None,
        help="Only after a certain date and time, e.g. "
        "``--only-after 20150510-111020`` to indicate "
        "scans done after 11:10:20 UTC on May 10th, 2015",
    )
    parser.add_argument(
        "--only-before",
        type=str,
        default=None,
        help="Only before a certain date and time, e.g. "
        "``--only-before 20150510-111020`` to indicate "
        "scans done before 11:10:20 UTC, May 10th, 2015",
    )

    parser.add_argument(
        "--ignore-suffix",
        default="",
        help=(
            "Suffix, or comma-separated list of suffixes, to be removed from source name. "
            "E.g. --ignore-suffix _ra,_dec,_k"
        ),
    )
    parser.add_argument(
        "--ignore-prefix",
        default="",
        help=(
            "Prefix, or comma-separated list of prefixes, to be removed from source name. "
            "E.g. --ignore-prefix ra_,dec_,k_"
        ),
    )

    args = parser.parse_args(args)
    ignore_suffix = args.ignore_suffix.split(",")
    ignore_prefix = args.ignore_prefix.split(",")

    info = inspect_directories(
        args.directories,
        args.only_after,
        args.only_before,
        ignore_suffix=ignore_suffix,
        ignore_prefix=ignore_prefix,
    )
    info.write("table.csv", overwrite=True)

    if len(info) == 0:
        raise ValueError("No valid observations found")

    config_files = []
    if args.dump_config_files:
        if args.options is not None:
            args.options = ast.literal_eval(args.options)
        else:
            args.options = {}

        args.options.update({"ignore_prefix": ignore_prefix, "ignore_suffix": ignore_suffix})

        config_files = dump_config_files(info, group_by_entries=args.group_by, options=args.options)
        logging.debug(config_files)
    else:
        groups = split_observation_table(info, group_by_entries=args.group_by)
        logging.debug(groups)
    return config_files
