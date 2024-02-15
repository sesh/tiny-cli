import sys
import textwrap

VERSION = "0.1"


def parse_args(args):
    result = {
        a.split("=")[0]: int(a.split("=")[1])
        if "=" in a and a.split("=")[1].isnumeric()
        else a.split("=")[1]
        if "=" in a
        else True
        for a in args
        if "--" in a
    }
    result["[]"] = [a for a in args if not a.startswith("--")]
    return result


def help():
    print(
        textwrap.dedent(
            """\
    {{ cookiecutter.app_name }}

    Usage:
        {{ cookiecutter.hyphenated_app_name }} [--help] [--version]

    Options:
        --help          Print this help message
        --version       Print version information
    """
        )
    )
    sys.exit()


def version():
    print(f"{{ cookiecutter.app_name }} {VERSION}")


def cli():
    args = parse_args(sys.argv[1:])

    if "--help" in args:
        help()

    if "--version" in args:
        version()
