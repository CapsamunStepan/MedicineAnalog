import os
import re
from typing import Optional


_DOSAGE_RE = re.compile(
    r"(?i)\b(\d+([.,]\d+)?\s?(mg|мг|g|г|mcg|мкг|мкг/доза|iu|ме|мл|ml))\b"
)
_FORM_WORDS_RE = re.compile(
    r"(?i)\b(таблетк\w*|капсул\w*|сироп\w*|порош\w*|раствор\w*|спрей\w*|маз\w*|крем\w*|гель\w*|ампул\w*|саше|капли|суспенз\w*)\b"
)
_PACK_RE = re.compile(r"(?i)\b(n\d+|№\s?\d+|\d+\s?шт\.?)\b")


def _fallback_extract_active_ingredient(title: str) -> str:
    """
    Heuristic fallback: strip dosage/form/pack tokens, keep first 1-3 words.
    Not perfect, but works offline and avoids hard dependency on external APIs.
    """
    if not title:
        return ""

    s = title.strip()
    s = _DOSAGE_RE.sub(" ", s)
    s = _FORM_WORDS_RE.sub(" ", s)
    s = _PACK_RE.sub(" ", s)
    s = re.sub(r"[(){}\[\];:,/\\|+*<>=\"'`~]", " ", s)
    s = re.sub(r"\s+", " ", s).strip().lower()

    if not s:
        return ""

    parts = s.split(" ")
    return " ".join(parts[:3]).strip()


def extract_active_ingredient(title: str) -> str:
    """
    Best-effort extraction. If OPENAI_API_KEY is configured, uses OpenAI to extract
    the active ingredient; otherwise falls back to a heuristic extractor.
    """
    api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return _fallback_extract_active_ingredient(title)

    try:
        from openai import OpenAI
    except Exception:
        return _fallback_extract_active_ingredient(title)

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Ты фармацевтический помощник. "
                        "Извлекай активное вещество из названия препарата. "
                        "Отвечай только активным веществом, без пояснений."
                    ),
                },
                {"role": "user", "content": title},
            ],
        )
        content = (response.choices[0].message.content or "").strip().lower()
        return content
    except Exception:
        return _fallback_extract_active_ingredient(title)
