#!/usr/bin/env python3
"""Remap Meteocons hex colors in weather SVGs to Catppuccin Frappe. Run after sync-icons."""

from __future__ import annotations

import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIRS = [
    ROOT / "src/icons/fill/svg-static",
    ROOT / "src/icons/fill/svg",
    ROOT / "src/icons/line/svg-static",
    ROOT / "src/icons/line/svg",
]

MAP = {
    "#0950bc": "#737994",
    "#0a5ad4": "#85c1dc",
    "#0b65ed": "#8caaee",
    "#1e293b": "#232634",
    "#212529": "#232634",
    "#2477b2": "#737994",
    "#2885c7": "#85c1dc",
    "#2a81bf": "#85c1dc",
    "#3392d6": "#8caaee",
    "#343a40": "#414559",
    "#374151": "#51576d",
    "#374251": "#51576d",
    "#37b24d": "#a6d189",
    "#384354": "#626880",
    "#39ad4e": "#a6d189",
    "#40c057": "#a6d189",
    "#475569": "#626880",
    "#495057": "#51576d",
    "#4b5563": "#51576d",
    "#515a69": "#626880",
    "#51cf66": "#a6d189",
    "#5b6472": "#626880",
    "#5eafcf": "#85c1dc",
    "#624226": "#737994",
    "#6b7280": "#626880",
    "#72b9d5": "#85c1dc",
    "#744e2d": "#737994",
    "#848b98": "#949cbb",
    "#86c3db": "#99d1db",
    "#875b34": "#626880",
    "#91c700": "#a6d189",
    "#94a3b8": "#838ba7",
    "#9936d4": "#ca9ee6",
    "#9ca3af": "#838ba7",
    "#a5aab2": "#949cbb",
    "#afb4bc": "#949cbb",
    "#b8bdc6": "#a5adce",
    "#bec1c6": "#949cbb",
    "#cbd5e1": "#a5adce",
    "#dc2626": "#e78284",
    "#deeafb": "#949cbb",
    "#e2e8f0": "#b5bfe2",
    "#e34647": "#e78284",
    "#e5e7eb": "#b5bfe2",
    "#e64980": "#f4b8e4",
    "#e6effc": "#838ba7",
    "#ef4444": "#e78284",
    "#f06595": "#f4b8e4",
    "#f3f7fe": "#a5adce",
    "#f59e0b": "#ef9f76",
    "#f6a823": "#e5c890",
    "#f7b23b": "#e5c890",
    "#f783ac": "#f4b8e4",
    "#f87171": "#e78284",
    "#f8af18": "#e5c890",
    "#fbbf24": "#e5c890",
    "#fcc419": "#e5c890",
    "#fccd34": "#e5c890",
    "#fcd34d": "#e5c890",
    "#fcd966": "#e5c890",
    "#fd7e14": "#ef9f76",
    "#fde171": "#e5c890",
    "#fde68a": "#e5c890",
    "#ff3c00": "#e78284",
    "#ff8d00": "#ef9f76",
    "#ff922b": "#ef9f76",
    "#ffa94d": "#ef9f76",
    "#ffb800": "#e5c890",
    "#ffc078": "#e5c890",
    "#ffd43b": "#e5c890",
    "#ffe066": "#e5c890",
}

pat = re.compile(r"#([0-9a-fA-F]{6})\b")


def recolor(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        return MAP.get(m.group(0).lower(), m.group(0))

    return pat.sub(repl, text)


def main() -> None:
    changed = 0
    for d in DIRS:
        for p in sorted(d.glob("*.svg")):
            t = p.read_text(encoding="utf-8")
            n = recolor(t)
            if n != t:
                p.write_text(n, encoding="utf-8")
                changed += 1
    print(f"remap-weather-icons-catppuccin-frappe: updated {changed} SVG files")


if __name__ == "__main__":
    main()
