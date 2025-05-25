import argparse
import aari
import aari_listen
from messages import BASE_LANG


def main(argv=None):
    parser = argparse.ArgumentParser(description="Aari command line interface")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("self-check", help="Run self check")
    sub.add_parser("system-data", help="Show system data")
    sub.add_parser("listen", help="Start voice recognition loop")
    say_p = sub.add_parser("say", help="Speak the given text")
    say_p.add_argument("text")

    args = parser.parse_args(argv)

    if args.command == "self-check":
        lang = aari.load_config().get("language", BASE_LANG)
        aari.perform_self_check(lang)
    elif args.command == "system-data":
        aari.display_system_data()
    elif args.command == "listen":
        aari_listen.listen_loop()
    elif args.command == "say":
        lang = aari.load_config().get("language", BASE_LANG)
        aari.say(args.text, lang)
    else:
        parser.print_help()


if __name__ == "__main__":  # pragma: no cover - manual use
    main()
