"""RP To-Do entry point script."""
# zinley/__main__.py

from zinley import cli, __app_name__


def main():
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()
