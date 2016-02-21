import argparse
from twitch_cli.api_v3 import v3_router as router


def main():
    arg_parser = argparse.ArgumentParser(
        description='',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        prog='twitch_cli'
    )

    sub_parsers = arg_parser.add_subparsers(dest='api_name', help='sub-command help')

    api_arguments = router.get_arguments()

    for api_name, args in api_arguments.iteritems():
        parser = sub_parsers.add_parser(api_name, help=api_name)

        for arg in args:
            parser.add_argument(arg.name, type=arg.type, help=arg.help)

    args = arg_parser.parse_args()

    api_class = router.apis[args.api_name]
    api = api_class(vars(args))
    api.execute()
    api.pretty_print()

if __name__ == '__main__':
    main()
