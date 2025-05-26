#!/usr/bin/env python3
"""
Test script specifically for image conversion functionality
"""

import os
import sys
import tempfile
from PIL import Image, ImageDraw, ImageFont
import logging

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from converter_core import DocumentConverter
import utils

def create_test_images():
    """Create test images in various formats"""
    test_dir = tempfile.mkdtemp(prefix="image_test_")
    print(f"Creating test images in: {test_dir}")
    
    # Create a simple test image
    img = Image.new('RGB', (400, 300), color='lightblue')
    draw = ImageDraw.Draw(img)
    
    # Draw some shapes and text
    draw.rectangle([50, 50, 350, 250], outline='darkblue', width=3)
    draw.ellipse([100, 100, 300, 200], fill='yellow', outline='orange', width=2)
    
    try:
        # Try to add text (may fail if no font available)
        draw.text((120, 140), "Test Image", fill='black')
    except:
        # If font loading fails, just continue without text
        pass
    
    # Save in different formats
    test_files = {}
    
    # PNG (with transparency)
    png_img = img.copy()
    png_img.putalpha(200)  # Semi-transparent
    png_file = os.path.join(test_dir, "test.png")
    png_img.save(png_file, 'PNG')
    test_files['png'] = png_file
    
    # JPEG
    jpg_file = os.path.join(test_dir, "test.jpg")
    img.save(jpg_file, 'JPEG', quality=90)
    test_files['jpg'] = jpg_file
    
    # BMP
    bmp_file = os.path.join(test_dir, "test.bmp")
    img.save(bmp_file, 'BMP')
    test_files['bmp'] = bmp_file
    
    # GIF
    gif_img = img.convert('P', palette=Image.ADAPTIVE, colors=256)
    gif_file = os.path.join(test_dir, "test.gif")
    gif_img.save(gif_file, 'GIF')
    test_files['gif'] = gif_file
    
    # TIFF
    tiff_file = os.path.join(test_dir, "test.tiff")
    img.save(tiff_file, 'TIFF')
    test_files['tiff'] = tiff_file
    
    # WebP (if supported)
    try:
        webp_file = os.path.join(test_dir, "test.webp")
        img.save(webp_file, 'WEBP', quality=90)
        test_files['webp'] = webp_file
    except Exception as e:
        print(f"  ⚠ WebP not supported: {e}")
    
    # ICO
    try:
        ico_img = img.resize((64, 64), Image.Resampling.LANCZOS)
        ico_file = os.path.join(test_dir, "test.ico")
        ico_img.save(ico_file, 'ICO')
        test_files['ico'] = ico_file
    except Exception as e:
        print(f"  ⚠ ICO creation failed: {e}")
    
    # Create a simple SVG file
    svg_content = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
  <rect x="50" y="50" width="300" height="200" fill="lightblue" stroke="darkblue" stroke-width="3"/>
  <circle cx="200" cy="150" r="50" fill="yellow" stroke="orange" stroke-width="2"/>
  <text x="120" y="155" font-family="Arial" font-size="16" fill="black">Test SVG</text>
</svg>'''
    
    svg_file = os.path.join(test_dir, "test.svg")
    with open(svg_file, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    test_files['svg'] = svg_file
    
    return test_dir, test_files

def test_image_conversions():
    """Test various image format conversions"""
    print("🖼️  Testing Image Conversions")
    print("=" * 50)
    
    # Setup logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
    test_dir, test_files = create_test_images()
    output_dir = os.path.join(test_dir, "converted")
    os.makedirs(output_dir, exist_ok=True)
    
    converter = DocumentConverter()
    
    # Define conversion test cases
    conversion_tests = [
        # Basic raster conversions
        ('png', 'jpg', 'PNG to JPEG'),
        ('jpg', 'png', 'JPEG to PNG'),
        ('png', 'gif', 'PNG to GIF'),
        ('gif', 'png', 'GIF to PNG'),
        ('bmp', 'png', 'BMP to PNG'),
        ('png', 'bmp', 'PNG to BMP'),
        ('tiff', 'jpg', 'TIFF to JPEG'),
        ('jpg', 'tiff', 'JPEG to TIFF'),
        
        # WebP conversions (if available)
        ('png', 'webp', 'PNG to WebP'),
        ('webp', 'png', 'WebP to PNG'),
        ('jpg', 'webp', 'JPEG to WebP'),
        ('webp', 'jpg', 'WebP to JPEG'),
        
        # ICO conversions
        ('png', 'ico', 'PNG to ICO'),
        ('ico', 'png', 'ICO to PNG'),
        
        # Image to PDF
        ('png', 'pdf', 'PNG to PDF'),
        ('jpg', 'pdf', 'JPEG to PDF'),
        ('gif', 'pdf', 'GIF to PDF'),
        ('bmp', 'pdf', 'BMP to PDF'),
        ('tiff', 'pdf', 'TIFF to PDF'),
        
        # SVG conversions
        ('svg', 'png', 'SVG to PNG'),
        ('svg', 'jpg', 'SVG to JPEG'),
        ('svg', 'pdf', 'SVG to PDF'),
    ]
    
    successful = 0
    failed = 0
    skipped = 0
    
    for source_format, target_format, description in conversion_tests:
        if source_format not in test_files:
            print(f"  ⏭️  {description}: Skipped (source file not available)")
            skipped += 1
            continue
            
        input_file = test_files[source_format]
        output_file = utils.generate_output_filename(input_file, target_format, output_dir)
        
        print(f"  🔄 Testing {description}...")
        
        try:
            success = converter.convert(input_file, output_file, source_format, target_format)
            
            if success and os.path.exists(output_file):
                file_size = os.path.getsize(output_file)
                print(f"    ✅ Success: {os.path.basename(output_file)} ({file_size} bytes)")
                successful += 1
            else:
                print(f"    ❌ Failed: Conversion unsuccessful")
                failed += 1
                
        except Exception as e:
            print(f"    ❌ Error: {str(e)}")
            failed += 1
    
    print(f"\n📊 Image Conversion Test Results:")
    print(f"  ✅ Successful: {successful}")
    print(f"  ❌ Failed: {failed}")
    print(f"  ⏭️  Skipped: {skipped}")
    print(f"  📁 Test files: {test_dir}")
    
    return successful, failed, skipped

def test_image_quality():
    """Test image quality and format-specific features"""
    print("\n🎨 Testing Image Quality Features")
    print("=" * 50)
    
    test_dir, test_files = create_test_images()
    output_dir = os.path.join(test_dir, "quality_test")
    os.makedirs(output_dir, exist_ok=True)
    
    converter = DocumentConverter()
    
    # Test transparency handling
    if 'png' in test_files:
        print("  🔍 Testing transparency handling...")
        
        # PNG to JPEG (should add white background)
        png_file = test_files['png']
        jpg_output = os.path.join(output_dir, "transparency_test.jpg")
        
        success = converter.convert(png_file, jpg_output, 'png', 'jpg')
        if success:
            print("    ✅ PNG with transparency → JPEG: Success")
        else:
            print("    ❌ PNG with transparency → JPEG: Failed")
    
    # Test ICO multi-size generation
    if 'png' in test_files:
        print("  🔍 Testing ICO multi-size generation...")
        
        png_file = test_files['png']
        ico_output = os.path.join(output_dir, "multi_size.ico")
        
        success = converter.convert(png_file, ico_output, 'png', 'ico')
        if success:
            print("    ✅ PNG → ICO with multiple sizes: Success")
        else:
            print("    ❌ PNG → ICO with multiple sizes: Failed")
    
    # Test SVG conversion quality
    if 'svg' in test_files:
        print("  🔍 Testing SVG conversion...")
        
        svg_file = test_files['svg']
        
        # Test different SVG outputs
        for target_format in ['png', 'jpg', 'pdf']:
            output_file = os.path.join(output_dir, f"svg_test.{target_format}")
            success = converter.convert(svg_file, output_file, 'svg', target_format)
            
            if success:
                print(f"    ✅ SVG → {target_format.upper()}: Success")
            else:
                print(f"    ❌ SVG → {target_format.upper()}: Failed")

def check_optional_dependencies():
    """Check for optional image processing dependencies"""
    print("\n📦 Checking Optional Image Dependencies")
    print("=" * 50)
    
    dependencies = [
        ('cairosvg', 'High-quality SVG conversion'),
        ('wand', 'ImageMagick Python binding for advanced image processing'),
    ]
    
    available = []
    missing = []
    
    for module, description in dependencies:
        try:
            __import__(module)
            print(f"  ✅ {module}: Available - {description}")
            available.append(module)
        except ImportError:
            print(f"  ❌ {module}: Missing - {description}")
            missing.append(module)
    
    if missing:
        print(f"\n💡 To install missing dependencies:")
        for module in missing:
            print(f"  pip install {module}")
        print("\nNote: These are optional. Basic image conversion will work without them.")
    
    return available, missing

def main():
    """Run image conversion tests"""
    print("🖼️  Universal File Converter - Image Conversion Test Suite")
    print("=" * 60)
    
    # Check dependencies
    available, missing = check_optional_dependencies()
    
    # Test basic image conversions
    successful, failed, skipped = test_image_conversions()
    
    # Test quality features
    test_image_quality()
    
    print(f"\n🎯 Summary:")
    print(f"  • Basic conversions: {successful} successful, {failed} failed, {skipped} skipped")
    print(f"  • Optional dependencies: {len(available)} available, {len(missing)} missing")
    
    if failed == 0:
        print(f"\n🎉 All image conversion tests passed!")
    else:
        print(f"\n⚠️  Some tests failed. Check the output above for details.")
    
    print(f"\n📚 Supported image formats:")
    formats = ['PNG', 'JPEG', 'GIF', 'BMP', 'TIFF', 'WebP', 'ICO', 'SVG']
    print(f"  {' • '.join(formats)}")

if __name__ == "__main__":
    main()
