"""
Utility functions for the Document Converter Application
"""

import os
import logging
from pathlib import Path
from typing import List, Optional, Tuple
import config

def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        level=getattr(logging, config.LOG_LEVEL),
        format=config.LOG_FORMAT,
        handlers=[
            logging.FileHandler(config.LOG_FILE),
            logging.StreamHandler()
        ]
    )

def get_file_extension(file_path: str) -> str:
    """Get file extension from file path"""
    return Path(file_path).suffix.lower()

def get_file_format(file_path: str) -> Optional[str]:
    """Determine file format from extension"""
    ext = get_file_extension(file_path)
    for format_name, extensions in config.SUPPORTED_FORMATS.items():
        if ext in extensions:
            return format_name
    return None

def is_supported_format(file_path: str) -> bool:
    """Check if file format is supported"""
    return get_file_format(file_path) is not None

def can_convert(source_format: str, target_format: str) -> bool:
    """Check if conversion between formats is supported"""
    return (source_format in config.CONVERSION_MATRIX and 
            target_format in config.CONVERSION_MATRIX[source_format])

def validate_file(file_path: str) -> Tuple[bool, str]:
    """Validate if file exists and is within size limits"""
    if not os.path.exists(file_path):
        return False, "File does not exist"
    
    if not os.path.isfile(file_path):
        return False, "Path is not a file"
    
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    if file_size_mb > config.MAX_FILE_SIZE:
        return False, f"File size ({file_size_mb:.1f}MB) exceeds limit ({config.MAX_FILE_SIZE}MB)"
    
    if not is_supported_format(file_path):
        return False, "File format not supported"
    
    return True, "File is valid"

def create_output_directory(output_dir: str = None) -> str:
    """Create output directory if it doesn't exist"""
    if output_dir is None:
        output_dir = config.DEFAULT_OUTPUT_DIR
    
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def generate_output_filename(input_file: str, target_format: str, output_dir: str = None) -> str:
    """Generate output filename with target format"""
    if output_dir is None:
        output_dir = config.DEFAULT_OUTPUT_DIR
    
    input_path = Path(input_file)
    base_name = input_path.stem
    
    # Get the first extension for the target format
    target_ext = config.SUPPORTED_FORMATS[target_format][0]
    
    output_filename = f"{base_name}{target_ext}"
    return os.path.join(output_dir, output_filename)

def get_supported_formats_list() -> List[str]:
    """Get list of all supported formats"""
    return list(config.SUPPORTED_FORMATS.keys())

def get_convertible_formats(source_format: str) -> List[str]:
    """Get list of formats that source format can be converted to"""
    return config.CONVERSION_MATRIX.get(source_format, [])

def sanitize_filename(filename: str) -> str:
    """Remove invalid characters from filename"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename
