import json
from pathlib import Path

# === CONFIGURATION ===
board = "nice_nano_v2"
# automatically find all *.keymap filenames under ../config/keymap
keymap_dir = Path(__file__).parent.parent / "config" / "keymap"
keymaps = sorted(p.stem for p in keymap_dir.glob("*.keymap"))

# Map each format to the shields it should build
format_shields = {
    "bt": ["scylla_left", "scylla_right"],
    "reset": ["settings_reset"],
}

groups = []
for keymap in keymaps:
    for fmt in ["bt"]:
        groups.append({
            "keymap": keymap,
            "format": fmt,
            "name": f"{keymap}-{fmt}",
            "board": board,
        })

# single reset entry
groups.append({
    "keymap": "default",
    "format": "reset",
    "name": "reset-nanov2",
    "board": board,
})

# Dump matrix as compact JSON (GitHub expects it this way)
print(json.dumps(groups))
