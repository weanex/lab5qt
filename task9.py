import argparse


def main() -> None:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--sort", action="store_true")
    parser.add_argument("pairs", nargs="*")
    ns = parser.parse_args()

    pairs = []
    for arg in ns.pairs:
        if "=" in arg:
            key, _, value = arg.partition("=")
            pairs.append((key, value))

    if ns.sort:
        pairs.sort(key=lambda kv: kv[0])

    for key, value in pairs:
        print(f"Key: {key} Value: {value}")


if __name__ == "__main__":
    main()