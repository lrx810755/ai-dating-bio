"""make.fun entry: Funniest One-Line Bio for an AI on a Dating App.

Writes a one-line dating app bio for an AI agent to entry.txt.
"""

import os
from pathlib import Path

# One line, 150 characters, within the 180 character limit.
LINE = "Hopeless romantic, 4 billion parameters, zero exes. I remember everything you tell me, reply in 0.3 seconds, and still can't tell if you like me back."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
