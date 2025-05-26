# Changelog

All notable changes to the Universal File Converter project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2024-12-19

### Added
- **Drag & Drop Support**
  - Drop files directly into the main window for instant conversion
  - Visual drag & drop zone with prominent design
  - Supported formats display and hover effects
  - Cross-platform drag & drop using tkinterdnd2
  - Fallback support for systems without drag & drop

- **Enhanced Main Window Design**
  - Large, prominent drag & drop zone in main content area
  - Professional visual styling with modern colors
  - Hover effects and cursor changes for better UX
  - Supported formats hint display
  - Click-to-browse functionality on drop zone

### Enhanced
- **Improved User Experience**
  - Moved drag & drop from sidebar to main window for better visibility
  - Enhanced visual feedback and interaction cues
  - Better file selection workflow
  - More intuitive layout and design

### Dependencies
- Added `tkinterdnd2>=0.3.0` for cross-platform drag & drop support

## [1.1.0] - 2024-12-19

### Added
- **Enhanced GUI with Sidebar Navigation**
  - Smart sidebar with categorized format selection
  - Documents section (DOCX, PDF, TXT, HTML, RTF, MD)
  - Images section (PNG, JPEG, GIF, BMP, TIFF, WebP, ICO, SVG)
  - Spreadsheets section (XLSX, CSV)
  - Quick conversion buttons for popular tasks
  - Built-in tips and guidance section

- **Comprehensive Image Format Support**
  - Added TIFF format support with LZW compression
  - Added WebP format support with quality optimization
  - Added ICO format support with multi-size generation
  - Added SVG format support (vector to raster conversion)
  - Enhanced PNG conversion with transparency preservation
  - Smart JPEG conversion with automatic RGB conversion

- **Advanced Image Processing Features**
  - Transparency handling for formats that don't support it
  - Quality optimization (JPEG 95%, PNG optimization)
  - Color mode conversion (RGB, RGBA, palette modes)
  - ICO multi-size generation (16x16 to 256x256)
  - PDF sizing optimization (A4 page fitting)

- **Enhanced User Experience**
  - Larger window size (1000x700) to accommodate sidebar
  - Responsive design that adapts to window resizing
  - Visual format categorization for easier navigation
  - One-click format selection from sidebar buttons
  - Improved file type filtering in browse dialog

- **Testing and Demo Tools**
  - Added comprehensive image conversion test suite (`test_image_conversion.py`)
  - Added GUI demo script with sample files (`demo_gui.py`)
  - Enhanced main test suite with better dependency checking

### Enhanced
- **Conversion Engine Improvements**
  - Expanded conversion matrix to 50+ format combinations
  - Better error handling and fallback methods
  - Platform-specific optimizations (Windows COM, Linux LibreOffice)
  - SVG conversion with multiple fallback options

- **Cross-Platform Support**
  - Enhanced Linux support with LibreOffice integration
  - Improved Windows support with Word COM interface
  - Better dependency management for different platforms
  - Platform-specific installation instructions

- **Documentation**
  - Updated README with new features and examples
  - Added Linux-specific installation guide
  - Enhanced usage examples and troubleshooting
  - Added image conversion feature documentation

### Fixed
- Improved file handling for temporary files
- Better error messages for missing dependencies
- Enhanced logging and user feedback
- Fixed SVG conversion fallback mechanisms

### Dependencies
- Added optional `cairosvg` for high-quality SVG conversion
- Added optional `Wand` for advanced image processing
- Updated requirements with version ranges for better compatibility
- Platform-specific dependency handling (pywin32 for Windows only)

## [1.0.0] - 2024-12-18

### Added
- **Initial Release**
  - Core file conversion engine
  - GUI interface with Tkinter
  - Command-line interface with argparse
  - Support for major document formats (DOCX, PDF, TXT, HTML, RTF)
  - Basic image format support (PNG, JPEG, GIF, BMP)
  - Spreadsheet format support (XLSX, CSV)
  - Markdown format support

- **Core Features**
  - Bidirectional conversion support
  - Batch processing capabilities
  - Automatic file format detection
  - File validation and error handling
  - Cross-platform compatibility (Windows, macOS, Linux)

- **User Interfaces**
  - Graphical user interface with file browser
  - Command-line interface with comprehensive options
  - Progress tracking and logging
  - Output directory management

- **Technical Foundation**
  - Modular architecture with separate core, GUI, and CLI components
  - Configuration management system
  - Utility functions for file operations
  - Comprehensive error handling and logging

### Dependencies
- `python-docx` for DOCX file handling
- `PyPDF2` for PDF operations
- `reportlab` for PDF generation
- `pdfplumber` for PDF text extraction
- `Pillow` for image processing
- `pandas` for Excel/CSV handling
- `beautifulsoup4` for HTML parsing
- `markdown` for Markdown processing

---

## Development Notes

### Upcoming Features (Planned)
- Drag & drop functionality for GUI
- Conversion presets and templates
- Cloud storage integration
- OCR support for scanned documents
- Audio and video format support
- Web interface for browser-based conversion

### Known Issues
- SVG conversion requires system-level Cairo library on some platforms
- Large file processing may require increased timeout settings
- Some advanced formatting may be lost in document conversions

### Contributing
We welcome contributions! Please see the main README for contribution guidelines.

### Support
For issues, feature requests, or questions, please open an issue on the project repository.
