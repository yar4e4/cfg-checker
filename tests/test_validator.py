import subprocess
from pathlib import Path
import pytest

from conftest import PROJECT_ROOT, BINARY_PATH


def run_validator(config_name: str) -> subprocess.CompletedProcess:
    config_path = PROJECT_ROOT / "tests" / "data" / config_name
    if not config_path.exists():
        pytest.fail(f"Test config file not found: {config_path}")

    result = subprocess.run(
        [str(BINARY_PATH), str(config_path)],
        capture_output=True,
        text=True,
    )
    return result


@pytest.mark.usefixtures("ensure_binary")
def test_valid_config():
    result = run_validator("valid.yaml")
    assert result.returncode == 0
    assert "valid" in result.stdout.lower()


@pytest.mark.usefixtures("ensure_binary")
def test_missing_version():
    result = run_validator("missing_version.yaml")
    assert result.returncode == 1
    assert "version" in result.stderr.lower()


@pytest.mark.usefixtures("ensure_binary")
def test_invalid_port():
    result = run_validator("invalid_port.yaml")
    assert result.returncode == 1
    assert "port" in result.stderr.lower()


@pytest.mark.usefixtures("ensure_binary")
def test_non_existent_file():
    fake_path = PROJECT_ROOT / "tests" / "data" / "does_not_exist.yaml"
    result = subprocess.run(
        [str(BINARY_PATH), str(fake_path)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "read" in result.stderr.lower() or "open" in result.stderr.lower()