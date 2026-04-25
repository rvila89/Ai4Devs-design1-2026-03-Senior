#!/usr/bin/env python3
"""
generate_diagram.py — CLI wrapper that runs a `diagrams` (mingrammer) Python script
and copies the output to a specified destination.

Usage:
    python scripts/generate_diagram.py <script.py> [--out DIR] [--format png|svg|pdf]

Examples:
    python scripts/generate_diagram.py my_aws_diagram.py
    python scripts/generate_diagram.py my_aws_diagram.py --out /mnt/user-data/outputs --format svg

The script:
1. Validates the environment (dot + diagrams library).
2. Injects show=False into the diagram script env so it never tries to open a viewer.
3. Executes the script.
4. Finds the generated output file(s) and copies them to --out if specified.
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def run_check_env() -> bool:
    """Quick inline check before running anything."""
    import importlib
    issues = []
    try:
        import diagrams  # noqa: F401
    except ImportError:
        issues.append("diagrams library not installed — run: pip install diagrams --break-system-packages")

    if not shutil.which("dot"):
        issues.append(
            "Graphviz 'dot' not found — install Graphviz:\n"
            "  macOS:  brew install graphviz\n"
            "  Ubuntu: sudo apt-get install -y graphviz"
        )

    if issues:
        print("❌  Missing dependencies:")
        for i in issues:
            print(f"    • {i}")
        return False
    return True


def find_generated_files(working_dir: Path, before: set, formats: list) -> list:
    """Find files that were newly created after the script ran."""
    after = set(working_dir.iterdir())
    new_files = after - before
    return [
        f for f in new_files
        if f.suffix.lstrip(".").lower() in formats
    ]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run a diagrams (mingrammer) Python script and collect outputs."
    )
    parser.add_argument("script", help="Path to the Python diagram script to run")
    parser.add_argument(
        "--out",
        default=None,
        help="Directory to copy output file(s) into (default: leave in place)",
    )
    parser.add_argument(
        "--format",
        default="png",
        choices=["png", "jpg", "svg", "pdf", "dot"],
        help="Expected output format (default: png)",
    )
    args = parser.parse_args()

    script_path = Path(args.script).resolve()
    if not script_path.exists():
        print(f"❌  Script not found: {script_path}")
        return 1

    if not run_check_env():
        return 1

    working_dir = script_path.parent
    before = set(working_dir.iterdir())

    print(f"▶  Running: {script_path.name}")
    env = os.environ.copy()
    # Ensure diagrams never tries to pop open a file viewer in headless environments
    env["DIAGRAMS_SHOW"] = "false"

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(working_dir),
        env=env,
    )

    if result.returncode != 0:
        print(f"❌  Script exited with code {result.returncode}")
        return result.returncode

    # Discover output files
    generated = find_generated_files(working_dir, before, [args.format])
    if not generated:
        # Fall back: look for any image-like files created
        generated = find_generated_files(working_dir, before, ["png", "jpg", "svg", "pdf"])

    if not generated:
        print("⚠️   No output files detected. Check that your Diagram() call uses show=False and a filename.")
        return 1

    for f in generated:
        print(f"✅  Generated: {f}")
        if args.out:
            dest_dir = Path(args.out)
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest = dest_dir / f.name
            shutil.copy2(f, dest)
            print(f"   Copied to: {dest}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
