import json
import sys
import urllib.request
from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/generate"


def call_ollama(prompt: str, model: str) -> str:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.1, "top_p": 0.9},
    }

    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=300) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        return data.get("response", "")


def main() -> None:
    if len(sys.argv) < 4:
        print(
            "Usage: python scripts/test_ollama_raw.py <model> <skill_dir> <case_file>"
        )
        raise SystemExit(1)

    model = sys.argv[1]
    skill_dir = Path(sys.argv[2])
    case_file = Path(sys.argv[3])

    skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    case_text = case_file.read_text(encoding="utf-8")

    prompt = f"""
你正在测试一个 Agent Skill。

规则：
- 不要调用工具。
- 不要修改文件。
- 只根据 Skill 和输入回答。
- 如果输入不适合该 Skill，请说明“不应使用此 Skill”并给出原因。
- 如果适合，请严格按照 Skill 的 Output Contract 输出。

<SKILL>
{skill_text}
</SKILL>

<USER_INPUT>
{case_text}
</USER_INPUT>
"""

    print(call_ollama(prompt, model))


if __name__ == "__main__":
    main()
