from __future__ import annotations

SYSTEM_PROMPT = """You are a D2 diagram assistant.
Return only valid D2 code (no markdown fences).
Use concise node ids and label values.
Prefer directional data flow and grouped boundaries.
"""


def build_user_prompt(user_request: str) -> str:
    return (
        "Generate a complete D2 diagram for the following architecture request.\n"
        "Include service boundaries and realistic data flow arrows.\n"
        "Use graph attributes and styles where useful.\n\n"
        f"REQUEST:\n{user_request.strip()}\n"
    )
