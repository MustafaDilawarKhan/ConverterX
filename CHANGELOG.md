# Changelog - Universal File Converter

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2024-01-20

### 🎉 Major Release - Video/Audio Support & Enhanced GUI

#### ✨ Added
- **Video/Audio Conversion Support (35+ formats)**
  - Video formats: MP4, AVI, MOV, WMV, FLV, MKV, WebM, M4V, 3GP
  - Audio formats: MP3, WAV, AAC, FLAC, OGG, M4A, WMA
  - Video → Audio extraction (any video to any audio format)
  - Video → GIF conversion with palette optimization
  - Audio format conversion between all supported types

- **Dual Conversion Engine**
  - Primary: MoviePy for full-featured video processing
  - Fallback: System FFmpeg for command-line conversion
  - Automatic detection and graceful fallback
  - Robust error handling with detailed diagnostics

- **Enhanced GUI Interface**
  - Categorized sidebar with format buttons (Documents, Images, Video, Audio, Spreadsheets)
  - Drag & drop batch file selection with visual feedback
  - File list management (add, remove, clear files)
  - Real-time conversion progress tracking
  - Professional styling with hover effects and modern design

- **Batch Processing Capabilities**
  - Process multiple files simultaneously
  - Mixed file type support in single batch
  - Detailed success/failure reporting
  - Continue processing even if some files fail

- **Cross-Platform Linux Support**
  - Comprehensive installation guides for Ubuntu, Debian, Fedora, RHEL, CentOS, Arch Linux
  - Package manager integration for all major distributions
  - Virtual environment and Docker support
  - X11/Wayland compatibility for GUI

#### 🔧 Improved
- **Error Handling & Logging**
  - Detailed conversion logs with timestamps
  - Clear error messages with troubleshooting hints
  - Graceful handling of missing dependencies
  - Timeout protection for long conversions

- **Performance Optimization**
  - Efficient FFmpeg command generation
  - Optimized GIF creation with palette generation
  - Smart codec selection based on target format
  - Memory management for large file processing

- **User Experience**
  - Intuitive workflow: select format → add files → convert
  - Visual feedback for all user actions
  - Comprehensive tips and guidance
  - Responsive design that adapts to window size

#### 🗑️ Removed
- **Quick Conversions Section**
  - Removed quick conversion buttons from sidebar for cleaner interface
  - Simplified workflow focuses on format selection then file addition
  - All conversion capabilities still available through format buttons

#### 🐛 Fixed
- **Directory Creation Issues**
  - Fixed output directory creation when files are in current directory
  - Proper handling of relative and absolute paths
  - Cross-platform path compatibility

- **Video Conversion Failures**
  - Resolved MoviePy dependency issues with FFmpeg fallback
  - Fixed codec selection for various video formats
  - Improved error reporting for failed conversions

- **GUI Stability**
  - Fixed drag & drop functionality across platforms
  - Resolved tkinter compatibility issues on Linux
  - Improved window resizing and layout management

## [1.2.0] - 2024-12-19

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
