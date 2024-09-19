import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

try:
    import pygame
    print("Pygame is already installed.")
except ImportError:
    print("Pygame not found. Installing...")
    install('pygame')
    print("Pygame has been installed successfully.")
