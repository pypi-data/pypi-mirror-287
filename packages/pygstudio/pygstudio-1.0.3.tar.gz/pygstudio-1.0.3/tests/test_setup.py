import subprocess
import pytest

pytest.skip(reason="This test is a cli based test", allow_module_level=True)

def test_main():
    subprocess.call('python -m pygstudio create "Test Pygstudio Project" -o ".temp"')