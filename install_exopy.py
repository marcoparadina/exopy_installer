import os
import subprocess
import platform
import sys

def run_command(command, env=None):
    """Runs a command in the terminal and checks for errors."""
    result = subprocess.run(command, shell=True, env=env)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}")

def create_virtual_environment(env_name="exopy_env"):
    """Creates a virtual environment."""
    print("Creating virtual environment...")
    run_command(f"python -m venv {env_name}")

def activate_virtual_environment(env_name="exopy_env"):
    """Activates the virtual environment based on the operating system and returns the environment variables."""
    print("Activating virtual environment...")
    if platform.system() == "Windows":
        activate_script = os.path.join(env_name, "Scripts", "activate.bat")
        env = os.environ.copy()
        env["VIRTUAL_ENV"] = os.path.abspath(env_name)
        env["PATH"] = os.path.join(env_name, "Scripts") + os.pathsep + env["PATH"]
    else:
        activate_script = os.path.join(env_name, "bin", "activate")
        env = os.environ.copy()
        env["VIRTUAL_ENV"] = os.path.abspath(env_name)
        env["PATH"] = os.path.join(env_name, "bin") + os.pathsep + env["PATH"]

    return env

def run_installer(env, installer_dir="exopy_installer"):
    """Runs the exopy installer."""
    print("Running the exopy installer...")
    os.chdir(installer_dir)
    run_command("python exopy_installer.py", env)

def main():
    env_name = "exopy_env"
    installer_dir = "exopy_installer"

    create_virtual_environment(env_name)
    env = activate_virtual_environment(env_name)
    run_installer(env, installer_dir)

    print("Exopy is now installed.")

if __name__ == "__main__":
    main()
