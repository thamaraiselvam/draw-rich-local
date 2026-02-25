from __future__ import annotations

ICON_COLOR_RULES = {
    "api": ("https://icons.terrastruct.com/azure/networking/api-management.svg", "#D6E4FF"),
    "db": ("https://icons.terrastruct.com/azure/databases/sql-database.svg", "#E8F5E9"),
    "queue": ("https://icons.terrastruct.com/azure/integration/service-bus.svg", "#FFF3E0"),
    "worker": ("https://icons.terrastruct.com/azure/compute/container-instances.svg", "#F3E5F5"),
    "monitor": ("https://icons.terrastruct.com/azure/management/governance.svg", "#FCE4EC"),
    "vector": ("https://icons.terrastruct.com/azure/ai-machine-learning/machine-learning.svg", "#E1F5FE"),
}


def enrich_d2_styles(d2_source: str) -> str:
    enriched: list[str] = []

    for line in d2_source.splitlines():
        stripped = line.strip()
        lower = stripped.lower()
        is_plain_node = ":" in stripped and "->" not in stripped and "{" not in stripped and "}" not in stripped
        if is_plain_node:
            icon, color = _pick_style(lower)
            if icon and color:
                indent = line[: len(line) - len(line.lstrip())]
                enriched.append(f"{indent}{stripped} {{")
                enriched.append(f'{indent}  style.fill: "{color}"')
                enriched.append(f'{indent}  icon: "{icon}"')
                enriched.append(f"{indent}}}")
                continue

        enriched.append(line)

    return "\n".join(enriched).rstrip() + "\n"


def _pick_style(text: str) -> tuple[str | None, str | None]:
    for keyword, style in ICON_COLOR_RULES.items():
        if keyword in text:
            return style
    return None, None
