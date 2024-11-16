import subprocess

def install_requirements():
    """Installs the required dependencies."""
    print("Installing requirements...")
    subprocess.run(["pip", "install", "."], check=True)
