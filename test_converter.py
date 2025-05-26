#!/usr/bin/env python3
"""
Test script for Universal File Converter
"""

import os
import tempfile
import sys
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import utils
import config
from converter_core import DocumentConverter

def create_test_files():
    """Create test files for conversion testing"""
    test_dir = tempfile.mkdtemp(prefix="converter_test_")
    print(f"Creating test files in: {test_dir}")

    # Create a simple text file
    txt_file = os.path.join(test_dir, "test.txt")
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write("This is a test document.\n")
        f.write("It contains multiple lines.\n")
        f.write("This will be used to test file conversion.\n")

    # Create a simple HTML file
    html_file = os.path.join(test_dir, "test.html")
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write("""<!DOCTYPE html>
<html>
<head>
    <title>Test Document</title>
</head>
<body>
    <h1>Test Document</h1>
    <p>This is a test HTML document.</p>
    <p>It will be used for conversion testing.</p>
</body>
</html>""")

    # Create a simple Markdown file
    md_file = os.path.join(test_dir, "test.md")
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write("""# Test Document

This is a **test** Markdown document.

## Features
- Bullet point 1
- Bullet point 2
- Bullet point 3

This will be used for conversion testing.
""")

    return test_dir, [txt_file, html_file, md_file]

def test_utils():
    """Test utility functions"""
    print("Testing utility functions...")

    # Test format detection
    test_files = {
        "test.docx": "docx",
        "test.pdf": "pdf",
        "test.txt": "txt",
        "test.html": "html",
        "test.jpg": "jpg",
        "unknown.xyz": None
    }

    for filename, expected in test_files.items():
        result = utils.get_file_format(filename)
        status = "✓" if result == expected else "✗"
        print(f"  {status} Format detection for {filename}: {result} (expected: {expected})")

    # Test conversion matrix
    test_conversions = [
        ("docx", "pdf", True),
        ("pdf", "txt", True),
        ("txt", "docx", True),
        ("docx", "xyz", False),
        ("xyz", "pdf", False)
    ]

    for source, target, expected in test_conversions:
        result = utils.can_convert(source, target)
        status = "✓" if result == expected else "✗"
        print(f"  {status} Conversion {source}→{target}: {result} (expected: {expected})")

def test_conversions():
    """Test actual file conversions"""
    print("\nTesting file conversions...")

    test_dir, test_files = create_test_files()
    output_dir = os.path.join(test_dir, "output")
    os.makedirs(output_dir, exist_ok=True)

    converter = DocumentConverter()

    # Test conversions
    test_cases = [
        ("test.txt", "txt", "pdf"),
        ("test.html", "html", "txt"),
        ("test.md", "md", "html")
    ]

    for filename, source_format, target_format in test_cases:
        input_file = os.path.join(test_dir, filename)
        output_file = utils.generate_output_filename(input_file, target_format, output_dir)

        print(f"  Testing {source_format.upper()} → {target_format.upper()}")

        try:
            success = converter.convert(input_file, output_file, source_format, target_format)
            if success and os.path.exists(output_file):
                file_size = os.path.getsize(output_file)
                print(f"    ✓ Success: {os.path.basename(output_file)} ({file_size} bytes)")
            else:
                print(f"    ✗ Failed: Conversion unsuccessful")
        except Exception as e:
            print(f"    ✗ Error: {str(e)}")

    print(f"\nTest files created in: {test_dir}")
    print("You can manually inspect the converted files.")

def test_cli_import():
    """Test CLI module import"""
    print("\nTesting CLI module...")
    try:
        import cli_converter
        print("  ✓ CLI module imported successfully")

        # Test help function
        try:
            # This would normally call sys.exit, so we catch it
            import argparse
            parser = argparse.ArgumentParser()
            print("  ✓ CLI argument parsing available")
        except Exception as e:
            print(f"  ✗ CLI argument parsing error: {e}")

    except ImportError as e:
        print(f"  ✗ CLI module import failed: {e}")

def test_gui_import():
    """Test GUI module import"""
    print("\nTesting GUI module...")
    try:
        import tkinter as tk
        print("  ✓ Tkinter available")

        try:
            import file_converter_gui
            print("  ✓ GUI module imported successfully")
        except ImportError as e:
            print(f"  ✗ GUI module import failed: {e}")

    except ImportError:
        print("  ✗ Tkinter not available (GUI will not work)")

def test_dependencies():
    """Test required dependencies"""
    print("\nTesting dependencies...")

    required_modules = [
        ("docx", "python-docx"),
        ("PyPDF2", "PyPDF2"),
        ("reportlab", "reportlab"),
        ("pdfplumber", "pdfplumber"),
        ("PIL", "Pillow"),
        ("pandas", "pandas"),
        ("bs4", "beautifulsoup4"),
        ("markdown", "markdown")
    ]

    missing_modules = []

    for module, package in required_modules:
        try:
            __import__(module)
            print(f"  ✓ {module} ({package})")
        except ImportError:
            print(f"  ✗ {module} ({package}) - missing")
            missing_modules.append(package)

    # Test Windows-specific modules
    import platform
    if platform.system() == "Windows":
        try:
            import win32com.client
            print(f"  ✓ win32com.client (pywin32) - for optimal DOCX→PDF conversion")
        except ImportError:
            print(f"  ⚠ win32com.client (pywin32) - missing (DOCX→PDF will use fallback method)")

    if missing_modules:
        print(f"\n⚠️  Missing packages: {', '.join(missing_modules)}")
        print("Install with: pip install " + " ".join(missing_modules))
        return False

    return True

def main():
    """Run all tests"""
    print("Universal File Converter - Test Suite")
    print("=" * 50)

    # Test dependencies first
    test_dependencies()

    # Test utility functions
    test_utils()

    # Test module imports
    test_cli_import()
    test_gui_import()

    # Test actual conversions
    try:
        test_conversions()
    except Exception as e:
        print(f"\nConversion testing failed: {e}")
        print("This might be due to missing dependencies or system requirements.")

    print("\n" + "=" * 50)
    print("Test completed!")
    print("\nTo run the application:")
    print("  GUI: python file_converter_gui.py")
    print("  CLI: python cli_converter.py --help")

if __name__ == "__main__":
    main()
