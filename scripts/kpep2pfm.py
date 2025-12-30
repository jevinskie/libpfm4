#!/usr/bin/env python3

import argparse
import sys
import plistlib


def real_main(args) -> int:
    d = plistlib.load(open(args.in_file, "rb"))
    print(f"in_buf: {d}")
    out_buf = ""
    open(args.out_file, "w").write(out_buf)
    return 0


def get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="kpep2pfm.py")
    parser.add_argument("-i", "--in-file", required=True, help="Input kpep plist path")
    parser.add_argument("-o", "--out-file", required=True, help="Output event header path")
    return parser


def main() -> int:
    return real_main(get_arg_parser().parse_args())


if __name__ == "__main__":
    sys.exit(main())
