#!/usr/bin/env python
import pandas as pd
import json
from pathlib import Path

groups = ["cpg", "mfc", "imr"]

ignore_names = {
    ".github", "comp-physics.github.io", "MFlowCode.github.io", "benchmark",
    "stats"}

for grp in groups:
    fn = Path(f"{grp}.json")
    with fn.open() as f:
        obj = json.load(f)

    # Drop ignored repos
    obj = [item for item in obj if item.get("name") not in ignore_names]

    # Build DataFrame
    df = pd.DataFrame(obj)

    # Escape LaTeX-unfriendly characters in ALL string columns
    # 1) underscores -> \_
    # 2) @ -> "at"
    if not df.empty:
        str_cols = df.select_dtypes(include="object").columns
        for col in str_cols:
            s = df[col].astype(str)  # ensure string ops, keeps non-nulls fine
            s = s.str.replace('_', r'\_', regex=False)
            s = s.str.replace('@', 'at', regex=False)
            df[col] = s

        # Also escape underscores in column names
        df = df.rename(columns=lambda c: c.replace('_', r'\_'))

    # Write CSV
    df.to_csv(f"github-{grp}.csv", encoding="utf-8", index=False)
