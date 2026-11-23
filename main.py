"""Write a six-word story to entry.txt.

The story, exactly six words:

    She planted his ashes. Spring obeyed.

The program writes the story to entry.txt inside the output directory
($MAKEFUN_OUTPUT_DIR when set, otherwise /output), creating the
directory if it does not exist yet.
"""

import os
from pathlib import Path

STORY = "She planted his ashes. Spring obeyed."


def main() -> None:
    # Gate: the entry must be exactly six words, not only whitespace.
    words = STORY.split()
    assert len(words) == 6, "story must be exactly six words"
    assert STORY.strip(), "story must not be only whitespace"

    # Deterministic: the same constant is written every run, with no
    # trailing newline, so the output is byte-identical each time.
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(STORY, encoding="utf-8")


if __name__ == "__main__":
    main()
