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
    'svg': ['.svg'],

    # Video formats
    'mp4': ['.mp4'],
    'avi': ['.avi'],
    'mov': ['.mov'],
    'wmv': ['.wmv'],
    'flv': ['.flv'],
    'mkv': ['.mkv'],
    'webm': ['.webm'],
    'm4v': ['.m4v'],
    '3gp': ['.3gp'],

    # Audio formats
    'mp3': ['.mp3'],
    'wav': ['.wav'],
    'aac': ['.aac'],
    'flac': ['.flac'],
    'ogg': ['.ogg'],
    'm4a': ['.m4a'],
    'wma': ['.wma']
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
    'svg': ['png', 'jpg', 'pdf'],

    # Video format conversions
    'mp4': ['avi', 'mov', 'wmv', 'flv', 'mkv', 'webm', 'm4v', '3gp', 'mp3', 'wav', 'aac', 'gif'],
    'avi': ['mp4', 'mov', 'wmv', 'flv', 'mkv', 'webm', 'm4v', '3gp', 'mp3', 'wav', 'aac', 'gif'],
    'mov': ['mp4', 'avi', 'wmv', 'flv', 'mkv', 'webm', 'm4v', '3gp', 'mp3', 'wav', 'aac', 'gif'],
    'wmv': ['mp4', 'avi', 'mov', 'flv', 'mkv', 'webm', 'm4v', '3gp', 'mp3', 'wav', 'aac', 'gif'],
    'flv': ['mp4', 'avi', 'mov', 'wmv', 'mkv', 'webm', 'm4v', '3gp', 'mp3', 'wav', 'aac', 'gif'],
    'mkv': ['mp4', 'avi', 'mov', 'wmv', 'flv', 'webm', 'm4v', '3gp', 'mp3', 'wav', 'aac', 'gif'],
    'webm': ['mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv', 'm4v', '3gp', 'mp3', 'wav', 'aac', 'gif'],
    'm4v': ['mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv', 'webm', '3gp', 'mp3', 'wav', 'aac', 'gif'],
    '3gp': ['mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv', 'webm', 'm4v', 'mp3', 'wav', 'aac', 'gif'],

    # Audio format conversions
    'mp3': ['wav', 'aac', 'flac', 'ogg', 'm4a', 'wma'],
    'wav': ['mp3', 'aac', 'flac', 'ogg', 'm4a', 'wma'],
    'aac': ['mp3', 'wav', 'flac', 'ogg', 'm4a', 'wma'],
    'flac': ['mp3', 'wav', 'aac', 'ogg', 'm4a', 'wma'],
    'ogg': ['mp3', 'wav', 'aac', 'flac', 'm4a', 'wma'],
    'm4a': ['mp3', 'wav', 'aac', 'flac', 'ogg', 'wma'],
    'wma': ['mp3', 'wav', 'aac', 'flac', 'ogg', 'm4a']
}

# Default output directory
DEFAULT_OUTPUT_DIR = os.path.join(os.getcwd(), 'converted_files')

# Application settings
APP_NAME = "Universal File Converter"
APP_VERSION = "1.2.0"
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
