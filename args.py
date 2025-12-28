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
        help="Typeahead API çalıştırır"
    )

    mode_group.add_argument(
        "-f", "--full-text-search",
        action="store_true",
        help="Full Text Search API çalıştırır (offset zorunlu)"
    )

    mode_group.add_argument(
        "-s", "--search",
        action="store_true",
        help="Basit arama yapar"
    )

    mode_group.add_argument(
        "-T", "--tui",
        action="store_true",
        help="Textual tabanlı TUI'yi açar"
    )

    parser.add_argument(
        "-l", "--limit",
        type=int,
        default=5,
        help="Çıktı limitini belirler"
    )

    parser.add_argument(
        "-o", "--offset",
        type=int,
        default=0,
        help="Offset değeri (sadece full-text-search için)"
    )

    args = parser.parse_args()

    if not args.tui and not args.query:
        parser.error("TUI dışındaki tüm modlar --query ister")

    if args.typeahead and args.offset != 0:
        parser.error("--typeahead modunda --offset kullanılamaz")
    

    return args
