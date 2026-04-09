#!/usr/bin/env python3
import csv
import json
import subprocess
from pathlib import Path

REPOS = {
    "cpg": "comp-physics",
    "mfc": "mflowcode",
    "imr": "InertialMicrocavitationRheometry",
}

IGNORE_NAMES = {
    ".github",
    "comp-physics.github.io",
    "MFlowCode.github.io",
    "benchmark",
    "stats",
}

FIELDNAMES = ["name", "description", "url"]


def run(cmd):
    subprocess.run(cmd, check=True)


def capture_json(cmd):
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def escape_latex(value):
    if value is None:
        return ""
    s = str(value)
    s = s.replace("_", r"\_")
    s = s.replace("@", "at")
    return s


def write_csv_atomic(path: Path, rows, fieldnames):
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    with tmp_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    tmp_path.replace(path)


def fetch_repos(org_name):
    return capture_json([
        "gh", "repo", "list", org_name,
        "--visibility", "public",
        "--source",
        "--json", "name,description,url",
    ])


def build_csv_rows(repos):
    repos = [repo for repo in repos if repo.get("name") not in IGNORE_NAMES]
    return [
        {key: escape_latex(repo.get(key, "")) for key in FIELDNAMES}
        for repo in repos
    ]


def csv_paths():
    return [Path(f"github-{group}.csv") for group in REPOS]


def remove_csv_outputs():
    for path in csv_paths():
        path.unlink(missing_ok=True)


def main():
    remove_csv_outputs()

    try:
        for group, org in REPOS.items():
            repos = fetch_repos(org)
            rows = build_csv_rows(repos)
            write_csv_atomic(Path(f"github-{group}.csv"), rows, FIELDNAMES)

        run(["latexmk", "-c", "cv.tex"])
        run(["latexmk", "-pdf", "cv.tex"])
    finally:
        remove_csv_outputs()


if __name__ == "__main__":
    main()
