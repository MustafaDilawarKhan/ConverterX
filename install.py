#!/usr/bin/env python3
"""
Installation script for Universal File Converter
"""

import subprocess
import sys
import os
import platform

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7 or higher is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    else:
        print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
        return True

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing required packages...")

    try:
        # Upgrade pip first
        print("  Upgrading pip...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Install requirements
        print("  Installing packages from requirements.txt...")
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                              capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ All packages installed successfully!")
            return True
        else:
            print("⚠️  Some packages may have failed to install:")
            print(result.stderr)

            # Try installing packages individually
            print("\n🔄 Trying to install packages individually...")
            return install_packages_individually()

    except FileNotFoundError:
        print("❌ requirements.txt file not found")
        return False

def install_packages_individually():
    """Install packages one by one to identify problematic ones"""
    packages = [
        "python-docx>=0.8.11",
        "PyPDF2>=3.0.1",
        "reportlab>=4.0.4",
        "pdfplumber>=0.9.0",
        "docx2txt>=0.8",
        "pandas>=2.0.0",
        "openpyxl>=3.1.0",
        "Pillow>=10.0.0",
        "markdown>=3.5.0",
        "beautifulsoup4>=4.12.0",
        "lxml>=4.9.0"
    ]

    # Add Windows-specific packages
    if platform.system() == "Windows":
        packages.append("pywin32>=306")

    successful = []
    failed = []

    for package in packages:
        try:
            print(f"  Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            successful.append(package)
            print(f"    ✅ {package}")
        except subprocess.CalledProcessError:
            failed.append(package)
            print(f"    ❌ {package}")

    print(f"\n📊 Installation summary:")
    print(f"  ✅ Successful: {len(successful)}")
    print(f"  ❌ Failed: {len(failed)}")

    if failed:
        print(f"\n⚠️  Failed packages: {', '.join(failed)}")
        print("The application may still work with reduced functionality.")

    return len(failed) == 0

def check_system_requirements():
    """Check system-specific requirements"""
    print("\n🔍 Checking system requirements...")

    system = platform.system()
    print(f"Operating System: {system}")

    if system == "Windows":
        print("📝 Note: For optimal DOCX to PDF conversion on Windows:")
        print("   - Microsoft Word should be installed")
        print("   - You may need to run as administrator for some conversions")
    elif system == "Darwin":  # macOS
        print("📝 Note: Some conversions may require additional system libraries")
        print("   - For GUI: Tkinter should be included with Python")
        print("   - For better PDF handling: brew install poppler")
    elif system == "Linux":
        print("📝 Linux-specific requirements:")
        print("   - For GUI support: Install tkinter")

        # Detect Linux distribution
        try:
            with open('/etc/os-release', 'r') as f:
                os_info = f.read().lower()

            if 'fedora' in os_info or 'rhel' in os_info or 'centos' in os_info:
                print("   📦 Fedora/RHEL/CentOS:")
                print("      sudo dnf install python3-tkinter")
                print("      sudo dnf install poppler-utils  # for better PDF handling")
            elif 'ubuntu' in os_info or 'debian' in os_info:
                print("   📦 Ubuntu/Debian:")
                print("      sudo apt-get install python3-tk")
                print("      sudo apt-get install poppler-utils")
            elif 'arch' in os_info:
                print("   📦 Arch Linux:")
                print("      sudo pacman -S tk")
                print("      sudo pacman -S poppler")
            else:
                print("   📦 General Linux:")
                print("      Install tkinter and poppler-utils using your package manager")

        except FileNotFoundError:
            print("   📦 Install tkinter and poppler-utils using your package manager")

        print("   - LibreOffice can be used for better DOCX→PDF conversion:")
        print("     sudo dnf install libreoffice  # Fedora")
        print("     sudo apt install libreoffice  # Ubuntu/Debian")

    return True

def test_installation():
    """Test if installation was successful"""
    print("\n🧪 Testing installation...")

    # Test imports
    test_modules = [
        ("docx", "python-docx"),
        ("PyPDF2", "PyPDF2"),
        ("reportlab", "reportlab"),
        ("pdfplumber", "pdfplumber"),
        ("PIL", "Pillow"),
        ("pandas", "pandas"),
        ("bs4", "beautifulsoup4"),
        ("markdown", "markdown")
    ]

    failed_imports = []

    for module, package in test_modules:
        try:
            __import__(module)
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package}")
            failed_imports.append(package)

    # Test GUI availability
    try:
        import tkinter
        print("  ✅ tkinter (GUI support)")
    except ImportError:
        print("  ❌ tkinter (GUI will not work)")
        failed_imports.append("tkinter")

    if failed_imports:
        print(f"\n❌ Some modules failed to import: {', '.join(failed_imports)}")
        print("Try running: pip install " + " ".join(failed_imports))
        return False
    else:
        print("\n✅ All modules imported successfully!")
        return True

def create_shortcuts():
    """Create convenient shortcuts"""
    print("\n🔗 Creating shortcuts...")

    # Create a simple launcher script
    launcher_content = '''#!/usr/bin/env python3
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
        choice = input("\\nSelect option (1-4): ").strip()

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
                print("\\nUse: python cli_converter.py --help for usage")
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
'''

    try:
        with open("launcher.py", "w", encoding="utf-8") as f:
            f.write(launcher_content)
        print("✅ Created launcher.py")

        # Make executable on Unix systems
        if platform.system() != "Windows":
            os.chmod("launcher.py", 0o755)

    except Exception as e:
        print(f"❌ Failed to create launcher: {e}")

def main():
    """Main installation function"""
    print("🚀 Universal File Converter - Installation Script")
    print("=" * 50)

    # Check Python version
    if not check_python_version():
        sys.exit(1)

    # Check system requirements
    check_system_requirements()

    # Install requirements
    if not install_requirements():
        print("\n❌ Installation failed!")
        sys.exit(1)

    # Test installation
    if not test_installation():
        print("\n⚠️  Installation completed with warnings.")
        print("Some features may not work properly.")
    else:
        print("\n✅ Installation completed successfully!")

    # Create shortcuts
    create_shortcuts()

    print("\n🎉 Setup complete!")
    print("\nTo get started:")
    print("  • Run GUI: python file_converter_gui.py")
    print("  • Run CLI: python cli_converter.py --help")
    print("  • Run tests: python test_converter.py")
    print("  • Use launcher: python launcher.py")

    print("\n📚 See README.md for detailed usage instructions.")

if __name__ == "__main__":
    main()
