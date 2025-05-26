#!/usr/bin/env python3
"""
Universal File Converter Launcher
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    print("Universal File Converter")
    print("1. GUI Application")
    print("2. Command Line Interface")
    print("3. Run Tests")
    print("4. Exit")

    while True:
        choice = input("\nSelect option (1-4): ").strip()

        if choice == "1":
            try:
                import file_converter_gui
                file_converter_gui.main()
            except ImportError as e:
                print(f"Error: {e}")
            break
        elif choice == "2":
            try:
                import cli_converter
                print("\nUse: python cli_converter.py --help for usage")
                print("Example: python cli_converter.py document.docx -t pdf")
            except ImportError as e:
                print(f"Error: {e}")
            break
        elif choice == "3":
            try:
                import test_converter
                test_converter.main()
            except ImportError as e:
                print(f"Error: {e}")
            break
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
