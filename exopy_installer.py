import subprocess

# List of scripts to run in order
scripts = ["clone_repos.py", "install_packages.py"]

# Run each script
for script in scripts:
    print(f"Running {script}")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error occurred while running {script}:")
        print(result.stderr)
        break  # Stop if a script fails
