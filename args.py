import argparse

def args_get():
    parser = argparse.ArgumentParser(
        description="Grokipedia API CLI"
    )

    parser.add_argument(
        "-q", "--query",
        type=str,
        help="Örnek: mustafa_kemal_ataturk"
    )

    mode_group = parser.add_mutually_exclusive_group(required=True)

    mode_group.add_argument(
        "-t", "--typeahead",
        action="store_true",
        help="Runs the Typeahead API"
    )

    mode_group.add_argument(
        "-f", "--full-text-search",
        action="store_true",
        help="Runs the Full Text Search API"
    )

    mode_group.add_argument(
        "-s", "--search",
        action="store_true",
        help="Performs a simple search"
    )

    mode_group.add_argument(
        "-T", "--tui",
        action="store_true",
        help="Opens the text-based TUI"
    )

    parser.add_argument(
        "-l", "--limit",
        type=int,
        default=5,
        help="Sets the output limit"
    )

    parser.add_argument(
        "-o", "--offset",
        type=int,
        default=0,
        help="Changes the offset value"
    )

    args = parser.parse_args()

    if not args.tui and not args.query:
        parser.error("All modes except TUI require --query")

    if args.typeahead and args.offset != 0:
        parser.error("--offset cannot be used in --typeahead mode")")
    

    return args
