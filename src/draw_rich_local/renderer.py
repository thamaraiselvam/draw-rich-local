from __future__ import annotations

import subprocess
from pathlib import Path


class D2Renderer:
    def render(self, d2_file: Path, output_file: Path) -> None:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["d2", str(d2_file), str(output_file)],
            check=True,
            capture_output=True,
            text=True,
        )
