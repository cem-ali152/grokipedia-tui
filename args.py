import argparse








def args_get():
    parser = argparse.ArgumentParser(
        description="Grokipedia API CLI"
    )

    # ORTAK
    parser.add_argument(
        "-q", "--query",
        required=True,
        type=str,
        help="Örnek: mustafa_kemal_ataturk"
    )

    # MOD SEÇİMİ
    mode_group = parser.add_mutually_exclusive_group()

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

    # ORTAK OPSİYONLAR
    parser.add_argument(
        "-l", "--limit",
        type=int,
        help="Çıktı limitini belirler",
        default=5
    )

    parser.add_argument(
        "-o", "--offset",
        type=int,
        help="Offset değeri (sadece full-text-search için)",
        default=0

    )

    parser.add_argument(
        "--search","-s",
        action="store_true",
        help="Referansları getirir (mod seçilmezse zorunludur)"
    )

    args = parser.parse_args()
    # typeahead → offset yasak
    if args.typeahead and args.offset is None:
        parser.error("--typeahead modunda --offset kullanılamaz")

    # HİÇ MOD SEÇİLMEDİYSE → references zorunlu
    if not (args.typeahead or args.full_text_search or args.search):
        parser.error(
            "Hiçbir mod seçilmedi. "
            "-h yazın"
        )
    return args

