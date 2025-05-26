# Universal File Converter

A comprehensive, modern file conversion tool with an intuitive GUI interface. Convert between documents, images, videos, audio files, and spreadsheets with professional-grade batch processing capabilities.

## 🚀 Features

### 📁 **Comprehensive Format Support (35+ Formats)**
- **📄 Documents**: DOCX, PDF, TXT, HTML, RTF, Markdown
- **🖼️ Images**: PNG, JPG, GIF, BMP, TIFF, WebP, ICO, SVG
- **🎬 Video**: MP4, AVI, MOV, WMV, FLV, MKV, WebM, M4V, 3GP
- **🎵 Audio**: MP3, WAV, AAC, FLAC, OGG, M4A, WMA
- **📊 Spreadsheets**: XLSX, CSV

### 🎨 **Modern User Interface**
- **Drag & Drop**: Batch file selection with visual feedback
- **Categorized Sidebar**: Organized format buttons by type
- **File List Management**: Add, remove, and clear files easily
- **Progress Tracking**: Real-time conversion status for each file
- **Professional Styling**: Clean, modern design with hover effects

### ⚡ **Advanced Processing**
- **Batch Conversion**: Process multiple files simultaneously
- **Smart Error Handling**: Continue processing even if some files fail
- **Quick Conversions**: One-click popular format combinations
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Dual Engine**: MoviePy + FFmpeg fallback for video/audio

### 🎯 **Popular Use Cases**
- **Video → MP3**: Extract audio tracks from videos
- **Video → GIF**: Create animated previews
- **DOCX → PDF**: Professional document conversion
- **Images → PDF**: Combine multiple images
- **Audio Format Conversion**: High-quality codec support

## 🔄 Supported Conversions

### **📄 Document Conversions**
```
DOCX ↔ PDF ↔ TXT ↔ HTML ↔ RTF ↔ MD
```

### **🖼️ Image Conversions**
```
PNG ↔ JPG ↔ GIF ↔ BMP ↔ TIFF ↔ WebP ↔ ICO ↔ SVG
```

### **🎬 Video Conversions**
```
MP4 ↔ AVI ↔ MOV ↔ WMV ↔ FLV ↔ MKV ↔ WebM ↔ M4V ↔ 3GP
Video → MP3/WAV/AAC (audio extraction)
Video → GIF (animated conversion)
```

### **🎵 Audio Conversions**
```
MP3 ↔ WAV ↔ AAC ↔ FLAC ↔ OGG ↔ M4A ↔ WMA
```

### **📊 Spreadsheet Conversions**
```
XLSX ↔ CSV
```

## 📦 Installation

### 🖥️ **Windows**

#### **Quick Install (Recommended)**
```bash
# 1. Clone the repository
git clone <repository-url>
cd universal-file-converter

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Install FFmpeg (for video/audio conversion)
# Download from: https://ffmpeg.org/download.html#build-windows
# Add to PATH or place ffmpeg.exe in the project folder

# 4. Run the application
python file_converter_gui.py
```

#### **Optional: Enhanced PDF Support**
```bash
# Download and install wkhtmltopdf for advanced PDF features
# From: https://wkhtmltopdf.org/downloads.html
```

### 🍎 **macOS**

```bash
# 1. Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Install system dependencies
brew install python3 ffmpeg wkhtmltopdf

# 3. Clone the repository
git clone <repository-url>
cd universal-file-converter

# 4. Install Python dependencies
pip3 install -r requirements.txt

# 5. Run the application
python3 file_converter_gui.py
```

### 🐧 **Linux (Ubuntu/Debian/Fedora)**

#### **Ubuntu/Debian**
```bash
# 1. Update package list
sudo apt update

# 2. Install system dependencies
sudo apt install -y python3 python3-pip ffmpeg wkhtmltopdf

# 3. Install additional libraries for GUI and media processing
sudo apt install -y python3-tk python3-dev build-essential

# 4. Clone the repository
git clone <repository-url>
cd universal-file-converter

# 5. Install Python dependencies
pip3 install -r requirements.txt

# 6. Run the application
python3 file_converter_gui.py
```

#### **Fedora/RHEL/CentOS**
```bash
# 1. Install system dependencies
sudo dnf install -y python3 python3-pip ffmpeg wkhtmltopdf

# 2. Install development tools
sudo dnf groupinstall -y "Development Tools"
sudo dnf install -y python3-tkinter python3-devel

# 3. Clone the repository
git clone <repository-url>
cd universal-file-converter

# 4. Install Python dependencies
pip3 install -r requirements.txt

# 5. Run the application
python3 file_converter_gui.py
```

#### **Arch Linux**
```bash
# 1. Install system dependencies
sudo pacman -S python python-pip ffmpeg wkhtmltopdf tk

# 2. Clone the repository
git clone <repository-url>
cd universal-file-converter

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Run the application
python file_converter_gui.py
```

### 🔧 **Troubleshooting Linux Installation**

#### **If FFmpeg is not available in repositories:**
```bash
# Ubuntu/Debian - Enable universe repository
sudo add-apt-repository universe
sudo apt update
sudo apt install ffmpeg

# Or install from snap
sudo snap install ffmpeg
```

#### **If wkhtmltopdf is not available:**
```bash
# Download directly from the official website
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo dpkg -i wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo apt-get install -f  # Fix any dependency issues
```

#### **Permission Issues:**
```bash
# If you get permission errors, try:
pip3 install --user -r requirements.txt

# Or create a virtual environment:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🎯 Usage

### **Basic Workflow**
1. **Launch**: `python file_converter_gui.py` (or `python3` on Linux/macOS)
2. **Add Files**: Drag & drop multiple files or use "Browse Files"
3. **Select Format**: Choose target format from categorized sidebar
4. **Convert**: Click "Convert X Files" for batch processing
5. **Results**: Check log for detailed conversion status

### **Quick Conversions**
- **Video → MP3**: Extract audio from any video file
- **Video → GIF**: Create animated GIFs with optimization
- **DOCX → PDF**: Professional document conversion
- **PNG → JPG**: Image format optimization
- **Images → PDF**: Combine multiple images into one PDF

### **Batch Processing**
1. Drag multiple files of different types
2. Select target format (applies to compatible files)
3. Convert all files with one click
4. Get detailed success/failure report

### Command Line Interface

#### Basic Usage
```bash
# Convert a single file
python cli_converter.py document.docx -t pdf

# Convert with custom output filename
python cli_converter.py document.pdf -t txt -o output.txt

# Batch convert all files in a directory
python cli_converter.py -b input_folder output_folder -t pdf
```

#### List Available Formats and Conversions
```bash
# List all supported formats
python cli_converter.py --list-formats

# List all available conversions
python cli_converter.py --list-conversions

# List conversions for specific format
python cli_converter.py --list-conversions docx
```

#### Advanced Options
```bash
# Verbose output
python cli_converter.py document.docx -t pdf -v

# Show version
python cli_converter.py --version

# Show help
python cli_converter.py --help
```

## Configuration

Edit `config.py` to customize:
- File size limits
- Batch processing limits
- Default output directory
- Logging settings
- Supported formats

## File Structure

```
saeedOS/
├── file_converter_gui.py    # GUI application
├── cli_converter.py         # Command line interface
├── converter_core.py        # Core conversion logic
├── utils.py                 # Utility functions
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Testing and Demo

### Quick Demo
```bash
# Run interactive demo with sample files
python demo_gui.py
```
This creates sample files and launches the GUI with instructions for testing all features.

### Test Suite
```bash
# Test all functionality
python test_converter.py

# Test image conversions specifically
python test_image_conversion.py

# Test installation
python install.py
```

## Examples

### Converting Documents
```bash
# DOCX to PDF
python cli_converter.py report.docx -t pdf

# PDF to TXT
python cli_converter.py document.pdf -t txt

# HTML to DOCX
python cli_converter.py webpage.html -t docx
```

### Converting Images
```bash
# Basic image conversions
python cli_converter.py image.png -t jpg
python cli_converter.py photo.jpg -t png
python cli_converter.py icon.png -t ico

# Advanced image conversions
python cli_converter.py image.png -t webp     # Modern WebP format
python cli_converter.py photo.tiff -t jpg     # TIFF to JPEG
python cli_converter.py logo.svg -t png       # SVG to PNG (vector to raster)

# Images to PDF
python cli_converter.py image.png -t pdf
python cli_converter.py -b images_folder pdf_output -t pdf

# Batch convert all images to PNG
python cli_converter.py -b mixed_images png_output -t png
```

### Batch Processing
```bash
# Convert all documents in folder to PDF
python cli_converter.py -b documents output_pdfs -t pdf

# Convert all images to PNG
python cli_converter.py -b mixed_images png_output -t png
```

## Troubleshooting

### Common Issues

1. **DOCX to PDF conversion fails on Windows**
   - Ensure Microsoft Word is installed
   - Run Python as administrator if needed

2. **Import errors**
   - Install all dependencies: `pip install -r requirements.txt`
   - Check Python version (3.7+ required)

3. **File size too large**
   - Check file size limits in `config.py`
   - Increase `MAX_FILE_SIZE` if needed

4. **Conversion quality issues**
   - Some conversions may lose formatting
   - For best results, use native applications when possible

### Logging

Check `converter.log` for detailed error messages and conversion history.

## Image Conversion Features

### Smart Format Handling
- **Transparency Support**: Automatically handles transparent images when converting to formats that don't support transparency (adds white background)
- **Quality Optimization**: JPEG saved with 95% quality, PNG with optimization
- **Color Mode Conversion**: Automatic conversion between RGB, RGBA, palette modes as needed
- **ICO Multi-Size**: Creates ICO files with multiple icon sizes (16x16 to 256x256)

### Advanced Features
- **WebP Support**: Modern image format with superior compression
- **TIFF with Compression**: LZW compression for smaller file sizes
- **SVG to Raster**: Vector graphics converted to high-quality raster images
- **PDF Sizing**: Images automatically sized to fit A4 pages when converting to PDF

### Optional Dependencies for Enhanced SVG Support
- `cairosvg`: High-quality SVG to PNG/PDF conversion
- `Wand`: ImageMagick Python binding for advanced image processing

## 📋 Dependencies

### **Core Dependencies**
- `python-docx`: Word document processing
- `PyPDF2`: PDF file handling
- `Pillow`: Image processing
- `pandas`: Data manipulation
- `openpyxl`: Excel file support
- `tkinterdnd2`: Drag & drop functionality

### **Video/Audio Dependencies**
- `moviepy`: Video/audio processing (optional, FFmpeg fallback available)
- `ffmpeg-python`: FFmpeg Python bindings (optional)

### **System Dependencies**
- `FFmpeg`: Video/audio conversion engine
- `wkhtmltopdf`: Advanced PDF generation (optional)

## 🛠️ Troubleshooting

### **Common Issues & Solutions**

#### **Video/Audio Conversion Fails**
```bash
# Check FFmpeg installation
ffmpeg -version

# If not installed:
# Ubuntu/Debian: sudo apt install ffmpeg
# macOS: brew install ffmpeg
# Windows: Download from https://ffmpeg.org/
```

#### **Import Errors**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Check Python version (3.8+ required)
python --version
```

#### **Permission Errors on Linux**
```bash
# Use user installation
pip3 install --user -r requirements.txt

# Or fix permissions
sudo chown -R $USER:$USER ~/.local/
```

#### **GUI Doesn't Start on Linux**
```bash
# Install tkinter
sudo apt install python3-tk  # Ubuntu/Debian
sudo dnf install python3-tkinter  # Fedora

# Check DISPLAY variable for remote sessions
echo $DISPLAY
```

#### **Drag & Drop Not Working**
```bash
# Install tkinterdnd2
pip install tkinterdnd2

# On Linux, ensure X11 forwarding if using SSH
ssh -X username@hostname
```

### **Performance Tips**
- **Use SSD storage** for faster file I/O
- **Close other media applications** during video conversion
- **Process smaller batches** for better responsiveness
- **Check available disk space** before large conversions

### **Getting Help**
1. **Check the conversion log** in the application for detailed error messages
2. **Verify all dependencies** are installed correctly
3. **Test with sample files** (use `python create_test_video.py`)
4. **Check file permissions** and output directory access
5. **Review system requirements** for your operating system

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 🎉 Acknowledgments

- **FFmpeg** - Multimedia processing framework
- **MoviePy** - Video editing library
- **Pillow** - Python Imaging Library
- **tkinter** - GUI framework
