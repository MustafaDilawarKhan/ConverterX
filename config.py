"""
Configuration file for the Document Converter Application
"""

import os

# Supported file formats and their extensions
SUPPORTED_FORMATS = {
    'docx': ['.docx'],
    'pdf': ['.pdf'],
    'txt': ['.txt'],
    'rtf': ['.rtf'],
    'html': ['.html', '.htm'],
    'odt': ['.odt'],
    'xlsx': ['.xlsx'],
    'csv': ['.csv'],
    'md': ['.md'],
    'png': ['.png'],
    'jpg': ['.jpg', '.jpeg'],
    'gif': ['.gif'],
    'bmp': ['.bmp'],
    'tiff': ['.tiff', '.tif'],
    'webp': ['.webp'],
    'ico': ['.ico'],
    'svg': ['.svg']
}

# Conversion mappings - what formats can be converted to what
CONVERSION_MATRIX = {
    'docx': ['pdf', 'txt', 'html', 'rtf'],
    'pdf': ['txt', 'docx', 'html'],
    'txt': ['docx', 'pdf', 'html', 'rtf'],
    'html': ['docx', 'pdf', 'txt'],
    'rtf': ['docx', 'pdf', 'txt'],
    'md': ['html', 'pdf', 'docx'],
    'xlsx': ['csv', 'pdf'],
    'csv': ['xlsx', 'pdf'],
    'png': ['jpg', 'pdf', 'gif', 'bmp', 'tiff', 'webp', 'ico'],
    'jpg': ['png', 'pdf', 'gif', 'bmp', 'tiff', 'webp'],
    'gif': ['png', 'jpg', 'pdf', 'bmp', 'tiff', 'webp'],
    'bmp': ['png', 'jpg', 'pdf', 'gif', 'tiff', 'webp'],
    'tiff': ['png', 'jpg', 'pdf', 'gif', 'bmp', 'webp'],
    'webp': ['png', 'jpg', 'pdf', 'gif', 'bmp', 'tiff'],
    'ico': ['png', 'jpg', 'pdf', 'gif', 'bmp'],
    'svg': ['png', 'jpg', 'pdf']
}

# Default output directory
DEFAULT_OUTPUT_DIR = os.path.join(os.getcwd(), 'converted_files')

# Application settings
APP_NAME = "Universal File Converter"
APP_VERSION = "1.1.0"
WINDOW_SIZE = "1000x700"
WINDOW_MIN_SIZE = (800, 500)

# Logging configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_FILE = "converter.log"

# File size limits (in MB)
MAX_FILE_SIZE = 100

# Batch processing settings
MAX_BATCH_SIZE = 50
