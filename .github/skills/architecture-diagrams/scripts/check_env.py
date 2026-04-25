#!/usr/bin/env python3
"""
check_env.py — Environment checker for the architecture-diagrams skill.

Verifies that all required tools and libraries are installed and prints
actionable fix instructions for anything that is missing.

Usage:
    python scripts/check_env.py
"""

import importlib
import shutil
import subprocess
import sys


def check(label: str, ok: bool, fix: str = "") -> bool:
    status = "✅" if ok else "❌"
    print(f"  {status}  {label}")
    if not ok and fix:
        print(f"       FIX: {fix}")
    return ok


def pip_install(package: str) -> None:
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", package, "--break-system-packages"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def main() -> None:
    print("\n─── Architecture Diagrams — Environment Check ───\n")
    all_ok = True

    # ── Python version ──────────────────────────────────────────────────────
    print("Python:")
    py_ok = sys.version_info >= (3, 7)
    all_ok &= check(
        f"Python ≥ 3.7  (found {sys.version.split()[0]})",
        py_ok,
        "Install Python 3.7+ from https://python.org",
    )

    # ── diagrams library ─────────────────────────────────────────────────────
    print("\ndiagrams (mingrammer):")
    try:
        import diagrams  # noqa: F401

        version = importlib.metadata.version("diagrams")
        all_ok &= check(f"diagrams installed (v{version})", True)
    except Exception:
        all_ok = False
        check(
            "diagrams not found",
            False,
            "pip install diagrams --break-system-packages",
        )
        print("       Auto-installing…")
        try:
            pip_install("diagrams")
            check("diagrams installed (auto)", True)
        except Exception as e:
            check(f"Auto-install failed: {e}", False)

    # ── Graphviz (dot) ───────────────────────────────────────────────────────
    print("\nGraphviz (rendering engine for diagrams):")
    dot = shutil.which("dot")
    all_ok &= check(
        f"dot executable found at: {dot}" if dot else "dot not found",
        bool(dot),
        (
            "macOS:   brew install graphviz\n"
            "       Ubuntu:  sudo apt-get install -y graphviz\n"
            "       Windows: choco install graphviz  OR  winget install Graphviz.Graphviz"
        ),
    )

    # ── Java (for PlantUML) ──────────────────────────────────────────────────
    print("\nJava (required to run PlantUML for C4-PlantUML diagrams):")
    java = shutil.which("java")
    if java:
        try:
            result = subprocess.run(
                ["java", "-version"], capture_output=True, text=True
            )
            version_line = (result.stderr or result.stdout).splitlines()[0]
            all_ok &= check(f"java found — {version_line}", True)
        except Exception:
            all_ok &= check("java found but version check failed", True)
    else:
        # Non-fatal: only needed for C4-PlantUML rendering
        check(
            "java not found (only needed for C4-PlantUML rendering)",
            False,
            (
                "macOS:   brew install openjdk\n"
                "       Ubuntu:  sudo apt-get install -y default-jre\n"
                "       Windows: https://adoptium.net\n"
                "       Alternatively use the PlantUML online server at https://www.plantuml.com/plantuml"
            ),
        )
        # Don't fail all_ok for Java — it's optional if user only needs mingrammer
        print("       (Skipping Java — won't affect mingrammer diagrams)")

    # ── PlantUML jar ─────────────────────────────────────────────────────────
    print("\nPlantUML:")
    plantuml = shutil.which("plantuml")
    if plantuml:
        check(f"plantuml CLI found at: {plantuml}", True)
    else:
        # Check for jar in common locations
        import os
        jar_paths = [
            "./plantuml.jar",
            os.path.expanduser("~/plantuml.jar"),
            "/usr/local/bin/plantuml.jar",
        ]
        jar_found = next((p for p in jar_paths if os.path.exists(p)), None)
        if jar_found:
            check(f"plantuml.jar found at: {jar_found}", True)
        else:
            check(
                "plantuml not found (only needed for C4-PlantUML rendering)",
                False,
                (
                    "Download from https://github.com/plantuml/plantuml/releases\n"
                    "       Or use online server: https://www.plantuml.com/plantuml\n"
                    "       Or paste .puml content at https://kroki.io"
                ),
            )

    # ── Summary ──────────────────────────────────────────────────────────────
    print("\n─────────────────────────────────────────────────")
    if all_ok:
        print("✅  All required dependencies satisfied. Ready to generate diagrams.\n")
    else:
        print(
            "⚠️   Some dependencies are missing. See FIX instructions above.\n"
            "    For mingrammer diagrams: Python + diagrams + Graphviz are required.\n"
            "    For C4-PlantUML diagrams: Java + PlantUML are required.\n"
        )


if __name__ == "__main__":
    main()
