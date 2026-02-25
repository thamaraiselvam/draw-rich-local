from __future__ import annotations

import json
from dataclasses import dataclass
from urllib import request


@dataclass
class OllamaClient:
    base_url: str = "http://localhost:11434"
    timeout_s: int = 120

    def generate(self, model: str, system_prompt: str, user_prompt: str) -> str:
        payload = {
            "model": model,
            "stream": False,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        }

        req = request.Request(
            url=f"{self.base_url}/api/chat",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        with request.urlopen(req, timeout=self.timeout_s) as resp:
            body = json.loads(resp.read().decode("utf-8"))

        return body["message"]["content"].strip()
