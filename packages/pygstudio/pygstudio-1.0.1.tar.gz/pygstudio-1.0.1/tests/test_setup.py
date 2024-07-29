import subprocess
from datetime import datetime
import os
import time

print(f"=== Test executed at: [{datetime.now()}] ===")
subprocess.call("python --version")
subprocess.call('python -m pygstudio create "Test Pygstudio Project" -o ".temp"')