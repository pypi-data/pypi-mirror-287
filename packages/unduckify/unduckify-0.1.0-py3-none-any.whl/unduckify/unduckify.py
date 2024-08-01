import argparse
import logging
from pathlib import Path

import r2pipe

from unduckify.reverse import reverse_combo, reverse_combo_key, reverse_key
from unduckify.utils import get_possible_layouts, load_layout


def unduckify_string(line, layout):
    line = [int(i.strip()) for i in line.split(",")]
    logging.info(f"Values to test: {line}")
    decoded = ""
    offset = 0
    for i in range(0, len(line), 1):
        i += offset
        try:
            _combo_key = reverse_combo(line[i], line[i+1], layout)
        except IndexError:
            continue
        if _combo_key:
            # check if next key can be combo-ed
            try:
                _k = reverse_combo_key(line[i+2], line[i+3], layout, _combo_key)
                if _k:
                    # combo key sucess
                    logging.debug(_k)
                    decoded += _k.char
                    offset += 3
                    continue
            except IndexError:
                continue
        try:
            _k = reverse_key(line[i], line[i+1], layout)
        except IndexError:
            continue
        if _k is False:
            continue
        logging.debug(_k)
        decoded += _k.char
        offset += 1
    logging.info(decoded)


def unduckify_dump(filepath, layout):
    # load binary
    binary_file = Path(filepath).resolve()
    try:
        r = r2pipe.open(str(binary_file))
    except Exception:
        exit()
    else:
        logging.info(f"Binary loaded: {str(binary_file)}")

    # analyze binary
    r.cmdj("aaa")
    binary_size = r.cmdj("ij").get("core", {}).get("size")
    functions = r.cmdj("aflj")
    # strings = r.cmdj('izzj')
    logging.info(f"{binary_size=}")
    logging.info(f"{len(functions)=}")
    # logging.info(f"{len(strings)=}")

    total_extracted = ""
    offset = 0
    for i in range(0, binary_size, 1):
        i += offset
        # ignore memory that is part of a function
        for f in functions:
            if f.get("offset") <= i < f.get("offset") + f.get("realsz"):
                break
        # ignore strings
        # for s in strings:
        #     if s.get("vaddr") <= i < s.get("vaddr") + s.get("size"):
        #         break
        ex = r.cmdj(f"pxj 4 @ {i}")
        try:
            _combo_key = reverse_combo(ex[0], ex[1], layout)
        except IndexError:
            continue
        if _combo_key:
            # check if next key can be comboed
            try:
                _k = reverse_combo_key(ex[2], ex[3], layout, _combo_key)
                if _k:
                    # combo key sucess
                    logging.debug(f"0x{i:08x} - {_k}")
                    total_extracted += _k.char
                    offset += 3
                    continue
            except IndexError:
                continue
        try:
            _k = reverse_key(ex[0], ex[1], layout)
        except IndexError:
            continue
        if _k is False:
            continue
        if _k.char == "":
            continue
        logging.debug(f"0x{i:08x} - {_k}")
        total_extracted += _k.char
        offset += 1
    logging.info(f"extracted data:\n{total_extracted}")


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", type=str)
    group.add_argument("-t", "--test", type=str,
                       help="Provide a value list to test. Example: \"0,6, 0,16, 0,7, 0,44, 2,36, 0,14\"")
    parser.add_argument("-l", "--layout", default="us", type=str, choices=get_possible_layouts())
    parser.add_argument("-s", "--system", default="win", type=str, choices=["win", "mac"])
    parser.add_argument("-v", "--verbose", action="store_true", default=False)
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
    else:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

    logging.debug(f"{args.file=}")
    logging.debug(f"{args.test=}")
    logging.debug(f"{args.layout=}")
    logging.debug(f"{args.system=}")
    logging.debug(f"{args.verbose=}")

    layout = load_layout(args.system, args.layout)

    try:
        if args.test:
            unduckify_string(args.test, layout)
    except AttributeError:
        pass

    try:
        if args.file:
            unduckify_dump(args.file, layout)
    except AttributeError:
        pass


if __name__ == "__main__":
    main()
