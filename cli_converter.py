#!/usr/bin/env python3
"""
Command Line Interface for Universal File Converter
"""

import argparse
import sys
import os
from pathlib import Path
import logging
import config
import utils
from converter_core import DocumentConverter

def setup_cli_logging(verbose=False):
    """Setup logging for CLI"""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(levelname)s: %(message)s',
        handlers=[logging.StreamHandler()]
    )

def list_supported_formats():
    """List all supported formats"""
    print("Supported file formats:")
    for format_name, extensions in config.SUPPORTED_FORMATS.items():
        ext_list = ', '.join(extensions)
        print(f"  {format_name.upper()}: {ext_list}")

def list_conversions(source_format=None):
    """List available conversions"""
    if source_format:
        if source_format.lower() in config.CONVERSION_MATRIX:
            targets = config.CONVERSION_MATRIX[source_format.lower()]
            print(f"Available conversions from {source_format.upper()}:")
            for target in targets:
                print(f"  {source_format.upper()} → {target.upper()}")
        else:
            print(f"Format '{source_format}' is not supported or has no available conversions")
    else:
        print("Available conversions:")
        for source, targets in config.CONVERSION_MATRIX.items():
            for target in targets:
                print(f"  {source.upper()} → {target.upper()}")

def convert_file(input_file, output_file, target_format, verbose=False):
    """Convert a single file"""
    setup_cli_logging(verbose)
    logger = logging.getLogger(__name__)
    
    # Validate input file
    if not os.path.exists(input_file):
        logger.error(f"Input file does not exist: {input_file}")
        return False
    
    is_valid, message = utils.validate_file(input_file)
    if not is_valid:
        logger.error(f"Invalid input file: {message}")
        return False
    
    # Detect source format
    source_format = utils.get_file_format(input_file)
    if not source_format:
        logger.error(f"Could not determine format of input file: {input_file}")
        return False
    
    # Check if conversion is supported
    if not utils.can_convert(source_format, target_format):
        logger.error(f"Conversion from {source_format.upper()} to {target_format.upper()} is not supported")
        logger.info("Use --list-conversions to see available conversions")
        return False
    
    # Generate output filename if not provided
    if not output_file:
        output_dir = utils.create_output_directory()
        output_file = utils.generate_output_filename(input_file, target_format, output_dir)
    else:
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
    
    logger.info(f"Converting {source_format.upper()} to {target_format.upper()}")
    logger.info(f"Input: {input_file}")
    logger.info(f"Output: {output_file}")
    
    # Perform conversion
    converter = DocumentConverter()
    success = converter.convert(input_file, output_file, source_format, target_format)
    
    if success:
        logger.info("✓ Conversion completed successfully!")
        logger.info(f"Output saved to: {output_file}")
        return True
    else:
        logger.error("✗ Conversion failed!")
        return False

def batch_convert(input_dir, output_dir, target_format, verbose=False):
    """Convert all supported files in a directory"""
    setup_cli_logging(verbose)
    logger = logging.getLogger(__name__)
    
    if not os.path.exists(input_dir):
        logger.error(f"Input directory does not exist: {input_dir}")
        return False
    
    # Create output directory
    utils.create_output_directory(output_dir)
    
    # Find all supported files
    supported_files = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if utils.is_supported_format(file_path):
                source_format = utils.get_file_format(file_path)
                if utils.can_convert(source_format, target_format):
                    supported_files.append(file_path)
    
    if not supported_files:
        logger.warning(f"No supported files found in {input_dir} that can be converted to {target_format.upper()}")
        return False
    
    logger.info(f"Found {len(supported_files)} files to convert")
    
    # Check batch size limit
    if len(supported_files) > config.MAX_BATCH_SIZE:
        logger.warning(f"Too many files ({len(supported_files)}). Maximum batch size is {config.MAX_BATCH_SIZE}")
        response = input(f"Continue with first {config.MAX_BATCH_SIZE} files? (y/N): ")
        if response.lower() != 'y':
            return False
        supported_files = supported_files[:config.MAX_BATCH_SIZE]
    
    # Convert files
    converter = DocumentConverter()
    successful = 0
    failed = 0
    
    for i, input_file in enumerate(supported_files, 1):
        logger.info(f"[{i}/{len(supported_files)}] Converting {os.path.basename(input_file)}")
        
        source_format = utils.get_file_format(input_file)
        output_file = utils.generate_output_filename(input_file, target_format, output_dir)
        
        success = converter.convert(input_file, output_file, source_format, target_format)
        
        if success:
            successful += 1
            logger.info(f"  ✓ Success: {output_file}")
        else:
            failed += 1
            logger.error(f"  ✗ Failed: {input_file}")
    
    logger.info(f"Batch conversion completed: {successful} successful, {failed} failed")
    return failed == 0

def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description="Universal File Converter - Convert between various document formats",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s document.docx -t pdf                    # Convert DOCX to PDF
  %(prog)s document.pdf -t txt -o output.txt       # Convert PDF to TXT with custom output
  %(prog)s -b input_folder output_folder -t pdf    # Batch convert all files to PDF
  %(prog)s --list-formats                          # List supported formats
  %(prog)s --list-conversions                      # List all available conversions
  %(prog)s --list-conversions docx                 # List conversions from DOCX
        """
    )
    
    parser.add_argument('input', nargs='?', help='Input file or directory (for batch mode)')
    parser.add_argument('-o', '--output', help='Output file or directory')
    parser.add_argument('-t', '--target', help='Target format (e.g., pdf, docx, txt)')
    parser.add_argument('-b', '--batch', action='store_true', 
                       help='Batch mode: convert all files in input directory')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('--list-formats', action='store_true', help='List supported formats')
    parser.add_argument('--list-conversions', nargs='?', const='', metavar='FORMAT',
                       help='List available conversions (optionally for specific format)')
    parser.add_argument('--version', action='version', version=f'%(prog)s {config.APP_VERSION}')
    
    args = parser.parse_args()
    
    # Handle list commands
    if args.list_formats:
        list_supported_formats()
        return 0
    
    if args.list_conversions is not None:
        list_conversions(args.list_conversions if args.list_conversions else None)
        return 0
    
    # Validate required arguments
    if not args.input:
        parser.error("Input file or directory is required")
    
    if not args.target:
        parser.error("Target format is required (use -t/--target)")
    
    # Normalize target format
    target_format = args.target.lower()
    if target_format not in utils.get_supported_formats_list():
        print(f"Error: Unsupported target format '{args.target}'")
        print("Use --list-formats to see supported formats")
        return 1
    
    # Perform conversion
    try:
        if args.batch:
            if not args.output:
                args.output = config.DEFAULT_OUTPUT_DIR
            success = batch_convert(args.input, args.output, target_format, args.verbose)
        else:
            success = convert_file(args.input, args.output, target_format, args.verbose)
        
        return 0 if success else 1
        
    except KeyboardInterrupt:
        print("\nConversion interrupted by user")
        return 1
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
