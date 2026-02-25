from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .llm import OllamaClient
from .prompting import SYSTEM_PROMPT, build_user_prompt
from .renderer import D2Renderer
from .style import enrich_d2_styles


@dataclass
class DiagramPipeline:
    model: str
    llm_base_url: str = "http://localhost:11434"

    def generate(self, prompt: str, out_file: Path, keep_d2: bool = True) -> Path:
        llm = OllamaClient(base_url=self.llm_base_url)
        raw_d2 = llm.generate(
            model=self.model,
            system_prompt=SYSTEM_PROMPT,
            user_prompt=build_user_prompt(prompt),
        )
        enhanced_d2 = enrich_d2_styles(raw_d2)

        d2_path = out_file.with_suffix(".d2")
        d2_path.parent.mkdir(parents=True, exist_ok=True)
        d2_path.write_text(enhanced_d2, encoding="utf-8")

        try:
            D2Renderer().render(d2_path, out_file)
            if not keep_d2:
                d2_path.unlink(missing_ok=True)
            return out_file
        except Exception:
            return d2_path
