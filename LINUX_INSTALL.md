# Linux Installation Guide for Universal File Converter

This guide provides specific instructions for installing and running the Universal File Converter on Linux systems, with special focus on Fedora.

## System Requirements

- Python 3.7 or higher
- pip (Python package manager)
- tkinter (for GUI support)
- LibreOffice (recommended for best DOCX→PDF conversion)

## Installation Steps

### Quick Installation (Recommended)

```bash
# Make the script executable
chmod +x install_linux.sh

# Run the automated installation script
./install_linux.sh
```

This script will:
- Detect your Linux distribution
- Install system dependencies (tkinter, LibreOffice, etc.)
- Install Python dependencies
- Optionally create a virtual environment
- Test the installation
- Create a desktop entry

### Manual Installation

### 1. Install System Dependencies

#### For Fedora/RHEL/CentOS:
```bash
# Install Python tkinter for GUI support
sudo dnf install python3-tkinter

# Install LibreOffice for better document conversion
sudo dnf install libreoffice

# Install poppler-utils for better PDF handling (optional)
sudo dnf install poppler-utils

# Install development tools if needed
sudo dnf groupinstall "Development Tools"
sudo dnf install python3-devel
```

#### For Ubuntu/Debian:
```bash
# Install Python tkinter for GUI support
sudo apt-get update
sudo apt-get install python3-tk

# Install LibreOffice for better document conversion
sudo apt-get install libreoffice

# Install poppler-utils for better PDF handling (optional)
sudo apt-get install poppler-utils

# Install development tools if needed
sudo apt-get install build-essential python3-dev
```

#### For Arch Linux:
```bash
# Install tkinter for GUI support
sudo pacman -S tk

# Install LibreOffice for better document conversion
sudo pacman -S libreoffice-fresh

# Install poppler for better PDF handling (optional)
sudo pacman -S poppler
```

### 2. Install Python Dependencies

```bash
# Navigate to the application directory
cd /path/to/saeedOS

# Run the installation script
python3 install.py

# Or install manually
pip3 install --user -r requirements.txt
```

### 3. Test Installation

```bash
# Run the test suite
python3 test_converter.py

# Test GUI (if tkinter is installed)
python3 file_converter_gui.py

# Test CLI
python3 cli_converter.py --help
```

## Linux-Specific Features

### DOCX to PDF Conversion Methods

1. **LibreOffice (Recommended)**: Best quality, preserves formatting
   - Requires: `libreoffice` package
   - Command: `libreoffice --headless --convert-to pdf`

2. **Fallback Method**: Text extraction + PDF generation
   - Uses: `python-docx` + `reportlab`
   - Quality: Basic, loses formatting

### File Permissions

Make scripts executable (optional):
```bash
chmod +x cli_converter.py
chmod +x file_converter_gui.py
chmod +x test_converter.py
```

## Usage Examples

### Command Line Interface

```bash
# Convert single file
python3 cli_converter.py document.docx -t pdf

# Batch convert all files in a directory
python3 cli_converter.py -b input_folder output_folder -t pdf

# Convert with verbose output
python3 cli_converter.py document.pdf -t txt -v

# List supported formats
python3 cli_converter.py --list-formats
```

### GUI Application

```bash
# Launch GUI
python3 file_converter_gui.py
```

## Troubleshooting

### Common Issues

1. **"tkinter not found" error**
   ```bash
   # Fedora/RHEL/CentOS
   sudo dnf install python3-tkinter

   # Ubuntu/Debian
   sudo apt-get install python3-tk
   ```

2. **"libreoffice command not found"**
   ```bash
   # Fedora/RHEL/CentOS
   sudo dnf install libreoffice

   # Ubuntu/Debian
   sudo apt-get install libreoffice
   ```

3. **Permission denied errors**
   ```bash
   # Use --user flag for pip
   pip3 install --user package_name

   # Or create virtual environment
   python3 -m venv converter_env
   source converter_env/bin/activate
   pip install -r requirements.txt
   ```

4. **Missing development headers**
   ```bash
   # Fedora/RHEL/CentOS
   sudo dnf install python3-devel

   # Ubuntu/Debian
   sudo apt-get install python3-dev
   ```

### Performance Tips

1. **Use LibreOffice for best DOCX→PDF quality**
2. **Install poppler-utils for better PDF text extraction**
3. **Use virtual environments to avoid conflicts**

## Virtual Environment Setup (Recommended)

```bash
# Create virtual environment
python3 -m venv converter_env

# Activate virtual environment
source converter_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python file_converter_gui.py

# Deactivate when done
deactivate
```

## Desktop Integration (Optional)

Create a desktop entry for easy access:

```bash
# Create desktop file
cat > ~/.local/share/applications/file-converter.desktop << EOF
[Desktop Entry]
Name=Universal File Converter
Comment=Convert between various document formats
Exec=python3 /path/to/saeedOS/file_converter_gui.py
Icon=applications-office
Terminal=false
Type=Application
Categories=Office;Utility;
EOF

# Update desktop database
update-desktop-database ~/.local/share/applications/
```

## Supported Conversions on Linux

✅ **Fully Supported:**
- TXT ↔ PDF, DOCX, HTML
- HTML ↔ TXT, PDF
- Markdown → HTML, PDF
- Images ↔ PDF, other formats
- Excel ↔ CSV

✅ **With LibreOffice:**
- DOCX ↔ PDF (high quality)
- RTF ↔ PDF, DOCX

⚠️ **Limited Support:**
- DOCX ↔ PDF (fallback method, basic quality)

## Additional Notes

- The application works best with LibreOffice installed
- GUI requires X11 or Wayland display server
- Some conversions may take longer on older hardware
- Large files (>100MB) may require increased timeout settings

For more information, see the main README.md file.
