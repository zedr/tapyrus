import argparse

from tapyrus.documents import SwaggerDocument

parser = argparse.ArgumentParser(description="Tapyrus command line interface")
subparsers = parser.add_subparsers(help="subcommand help")
run_parser = subparsers.add_parser("run")
run_parser.add_argument("path_to_swagger_file", help="Path to Swagger file")


def run(args: argparse.Namespace) -> None:
    document = SwaggerDocument.load(args.path_to_swagger_file)
    server = WebServer.load(document)
    server.run()


run_parser.set_defaults(func=run)


def main() -> None:
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
