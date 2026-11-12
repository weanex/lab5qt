import argparse


def main() -> None:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("nums", nargs="*")
    try:
        ns = parser.parse_args()
    except SystemExit:
        return

    try:
        if len(ns.nums) == 0:
            print("NO PARAMS")
            return
        ints = [int(x) for x in ns.nums]
        if len(ints) == 1:
            print("TOO FEW PARAMS")
        elif len(ints) > 2:
            print("TOO MANY PARAMS")
        else:
            print(ints[0] + ints[1])
    except Exception as e:
        print(type(e).__name__)


if __name__ == "__main__":
    main()