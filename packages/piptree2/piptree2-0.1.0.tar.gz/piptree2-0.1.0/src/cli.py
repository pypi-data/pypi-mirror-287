import pip
import argparse

from src.piptree import *

__name__ = "piptree2"
__version__ = "0.1.0"

try:
    ModuleNotFoundError
except NameError:
    ModuleNotFoundError = ImportError

try:
    # pip >= 10.0.0 hides main in pip._internal. We'll monkey patch what we need and hopefully this becomes available
    # at some point.
    from pip._internal import logger, main

    pip.main = main
    pip.logger = logger
except (ModuleNotFoundError, ImportError):
    pass


def create_parser():
    parser = argparse.ArgumentParser(
        description="""
        piptree is a tool for visualizing the dependency tree of a pip
        installation. It is a wrapper around pip freeze, so it will only work
        with packages that are installed with pip.
        """,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{__name__} {__version__}",
        help="show this version number and exit",
    )
    parser.add_argument(
        "-l",
        "--list",
        type=str,
        nargs="*",
        # const=[],
        help="list dependencies and children",
    )
    parser.add_argument(
        "-r",
        "--remove",
        type=str,
        nargs="*",
        # const=[],
        help="remove dependencies and children",
    )
    parser.add_argument(
        "-y",
        "--yes",
        action="store_true",
        default=False,
        help="do not ask for confirmation of remove deletions",
    )
    return parser


def main(argv=None):
    # if args.exclude and (args.all or args.packages):
    #     return parser.error("cannot use --exclude with --packages or --all")
    # if args.license and args.freeze:
    #     return parser.error("cannot use --license with --freeze")

    parser = create_parser()
    args = parser.parse_args(argv)
    # print(f'args: {args}')
    if args.list is not None:
        list_dists(args.list)
    elif args.remove is not None:
        remove_dists(args.remove, args.yes)
    else:
        parser.print_help()


if __name__ == "__main__":
    sys.exit(main())
