# Universal File Converter

A comprehensive Python application for converting between various document and file formats including DOCX, PDF, TXT, HTML, RTF, images, and more.

## Features

- **Multiple Format Support**: Convert between DOCX, PDF, TXT, HTML, RTF, Markdown, Excel, CSV, and image formats
- **Bidirectional Conversion**: Convert DOCX ↔ PDF and many other format combinations
- **Enhanced GUI Interface**: User-friendly graphical interface with organized sidebar navigation
- **Smart Sidebar**: Categorized format selection (Documents, Images, Spreadsheets)
- **Quick Conversions**: One-click buttons for popular conversion tasks
- **Command Line Interface**: Powerful CLI for batch processing and automation
- **Batch Processing**: Convert multiple files at once
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Error Handling**: Comprehensive error handling and logging
- **File Validation**: Automatic file format detection and validation
- **Quality Optimization**: Smart handling of transparency, compression, and format-specific features

## Supported Formats

### Document Formats
- **DOCX** → PDF, TXT, HTML, RTF
- **PDF** → TXT, DOCX, HTML
- **TXT** → DOCX, PDF, HTML, RTF
- **HTML** → DOCX, PDF, TXT
- **RTF** → DOCX, PDF, TXT
- **Markdown** → HTML, PDF, DOCX

### Spreadsheet Formats
- **XLSX** → CSV, PDF
- **CSV** → XLSX, PDF

### Image Formats
- **PNG** ↔ JPG, GIF, BMP, TIFF, WebP, ICO, PDF
- **JPG/JPEG** ↔ PNG, GIF, BMP, TIFF, WebP, PDF
- **GIF** ↔ PNG, JPG, BMP, TIFF, WebP, PDF
- **BMP** ↔ PNG, JPG, GIF, TIFF, WebP, PDF
- **TIFF** ↔ PNG, JPG, GIF, BMP, WebP, PDF
- **WebP** ↔ PNG, JPG, GIF, BMP, TIFF, PDF
- **ICO** ↔ PNG, JPG, GIF, BMP, PDF
- **SVG** → PNG, JPG, PDF (vector to raster conversion)

## Installation

### Quick Install (All Platforms)
```bash
python install.py
```

### Manual Installation

1. **Clone or download the repository**
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### System Requirements

- Python 3.7 or higher
- **Windows**: Microsoft Word (for optimal DOCX to PDF conversion)
- **Linux**: See [LINUX_INSTALL.md](LINUX_INSTALL.md) for detailed Linux installation
- **macOS**: Additional system dependencies may be required

### Platform-Specific Setup

#### Windows
- Install Python dependencies: `pip install -r requirements.txt`
- Microsoft Word recommended for best DOCX→PDF conversion

#### Linux (Fedora/Ubuntu/etc.)
- See detailed guide: [LINUX_INSTALL.md](LINUX_INSTALL.md)
- Install tkinter: `sudo dnf install python3-tkinter` (Fedora)
- Install LibreOffice: `sudo dnf install libreoffice` (recommended)

#### macOS
- Install Python dependencies: `pip install -r requirements.txt`
- Tkinter should be included with Python

## Usage

### GUI Application

Run the graphical interface:
```bash
python file_converter_gui.py
```

**Enhanced GUI Features:**
- **Smart Sidebar Navigation**: Organized by file categories (Documents, Images, Spreadsheets)
- **Quick Conversion Buttons**: One-click access to popular conversions
- **Format Selection**: Click sidebar buttons to instantly set target format
- **Browse and select input files** with enhanced file type filtering
- **Automatic format detection** and validation
- **Real-time conversion progress** with detailed logging
- **Conversion tips and guidance** built into the interface
- **Responsive design** that adapts to different window sizes

**Sidebar Categories:**
- 📄 **Documents**: DOCX, PDF, TXT, HTML, RTF, Markdown
- 🖼️ **Images**: PNG, JPEG, GIF, BMP, TIFF, WebP, ICO, SVG
- 📊 **Spreadsheets**: XLSX, CSV

**Quick Conversions:**
- DOCX → PDF (most popular)
- PDF → TXT (text extraction)
- PNG → JPG (with transparency handling)
- JPG → PNG (add transparency support)
- Images → PDF (any image to PDF)

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

## Dependencies

- `python-docx`: DOCX file handling
- `PyPDF2`: PDF operations
- `reportlab`: PDF generation
- `pdfplumber`: PDF text extraction
- `Pillow`: Image processing (PNG, JPG, GIF, BMP, TIFF, WebP, ICO)
- `pandas`: Excel/CSV handling
- `beautifulsoup4`: HTML parsing
- `markdown`: Markdown processing
- `cairosvg`: SVG conversion (optional)
- `Wand`: Advanced image processing (optional)

## License

This project is open source. Feel free to modify and distribute.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Version History

- **v1.1.0**: Enhanced GUI with sidebar navigation, quick conversions, and improved user experience
- **v1.0.0**: Initial release with GUI and CLI interfaces, support for major document and image formats

For detailed changes, see [CHANGELOG.md](CHANGELOG.md)
