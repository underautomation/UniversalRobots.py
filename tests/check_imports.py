"""
Run pyright and filter out .NET/pythonnet imports (UnderAutomation.*, clr, System.*)
that cannot be resolved statically but are valid at runtime via pythonnet.
"""
import subprocess
import json
import sys
import re

# Patterns for imports that come from .NET (pythonnet) and should be ignored
IGNORED_IMPORT_PATTERNS = [
    r'Import "UnderAutomation\.',
    r'Import "clr"',
    r'Import "System\.',
    r'Import "System"',
]

def main():
    result = subprocess.run(
        [sys.executable, "-m", "pyright", "--outputjson"],
        capture_output=True,
        text=True,
    )

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("Failed to parse pyright output:")
        print(result.stdout)
        print(result.stderr)
        return 1

    diagnostics = data.get("generalDiagnostics", [])

    # Filter out .NET imports
    filtered = []
    ignored_count = 0
    for diag in diagnostics:
        msg = diag.get("message", "")
        if any(re.search(pat, msg) for pat in IGNORED_IMPORT_PATTERNS):
            ignored_count += 1
            continue
        filtered.append(diag)

    # Display results
    errors = [d for d in filtered if d.get("severity") == "error"]
    warnings = [d for d in filtered if d.get("severity") == "warning"]

    for diag in filtered:
        severity = diag.get("severity", "?")
        file = diag.get("file", "?")
        msg = diag.get("message", "")
        rule = diag.get("rule", "")
        rng = diag.get("range", {})
        start = rng.get("start", {})
        line = start.get("line", 0)
        col = start.get("character", 0)
        print(f"  {file}:{line + 1}:{col + 1} - {severity}: {msg} ({rule})")

    print()
    print(f"  {len(errors)} error(s), {len(warnings)} warning(s)  (filtered out {ignored_count} .NET import(s))")

    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
