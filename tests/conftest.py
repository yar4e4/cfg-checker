import subprocess
from pathlib import Path
import pytest

PROJECT_ROOT = Path(__file__).parent.parent
BINARY_PATH = PROJECT_ROOT / "bin" / "validator"


@pytest.fixture(scope="session")
def ensure_binary():
    if not BINARY_PATH.is_file():
        print("Building validator binary...")
        result = subprocess.run(
            ["go", "build", "-o", "validator", "main.go"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print("Build failed:")
            print(result.stderr)
            pytest.fail("Failed to build validator binary")
        print("Binary built successfully")
    yield