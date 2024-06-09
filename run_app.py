import os
import sys
import subprocess

def install_packages():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'flask'])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install Flask: {e}")
        sys.exit(1)

def run_app():
    try:
        subprocess.check_call([sys.executable, 'app.py'])
    except subprocess.CalledProcessError as e:
        print(f"Failed to run the app: {e}")
        sys.exit(1)

if __name__ == '__main__':
    install_packages()
    run_app()
