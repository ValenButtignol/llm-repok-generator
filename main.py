import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from classes.system import System

def main():
    system = System()
    system.initialize()
    system.execute()

if __name__ == "__main__":
    main()
