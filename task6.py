import sys


def main() -> None:
    args = sys.argv[1:]
    sort = "--sort" in args
    if sort:
        args = [a for a in args if a != "--sort"]

    pairs = []
    for arg in args:
        if "=" in arg:
            key, _, value = arg.partition("=")
            pairs.append((key, value))

    if sort:
        pairs.sort(key=lambda kv: kv[0])

    for key, value in pairs:
        print(f"Key: {key} Value: {value}")


if __name__ == "__main__":
    main()