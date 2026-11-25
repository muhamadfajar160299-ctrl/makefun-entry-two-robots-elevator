"""Write one line of awkward robot elevator small talk to entry.txt.

Stdlib only. Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt when set,
otherwise entry.txt beside this program. The line is a single robot's
elevator small talk: it computed things to say, discarded them all, and
now reports the silence as measurably worse -- machine logic showing
through forced politeness.
"""

import os
import sys

LINE = "I calculated 47 things to say to you in this elevator. I discarded all of them. The silence is now 94% more awkward."


def main():
    if not LINE.strip():
        print("error: entry line is empty", file=sys.stderr)
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.getcwd()
    path = os.path.join(out_dir, "entry.txt")
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError as exc:
        print(f"error: cannot write {path}: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
