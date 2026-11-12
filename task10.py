import argparse
import textwrap


def format_text_block(frame_height: int, frame_width: int, file_name: str) -> str:
   
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            raw = f.read()
    except Exception as e:
        return str(e)            

    result_lines = []
    for paragraph in raw.splitlines():
        if not paragraph.strip():
            result_lines.append("")
            if len(result_lines) >= frame_height:
                break
            continue
        wrapped = textwrap.wrap(paragraph, width=frame_width)
        for line in wrapped:
            result_lines.append(line)
            if len(result_lines) >= frame_height:
                break
        if len(result_lines) >= frame_height:
            break

    return "\n".join(result_lines[:frame_height])


def main() -> None:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--frame-height", type=int, default=10)
    parser.add_argument("--frame-width", type=int, default=30)
    parser.add_argument("file_name", nargs="?")
    ns = parser.parse_args()

    if not ns.file_name:
        print("NO FILE")
        return

    print(format_text_block(ns.frame_height, ns.frame_width, ns.file_name))


if __name__ == "__main__":
    main()