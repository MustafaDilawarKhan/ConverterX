#!/usr/bin/env python3
"""
Demo script to showcase the enhanced GUI with sidebar
"""

import os
import sys
import tempfile
from PIL import Image, ImageDraw

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def create_demo_files():
    """Create some demo files for testing the GUI"""
    demo_dir = tempfile.mkdtemp(prefix="gui_demo_")
    print(f"Creating demo files in: {demo_dir}")
    
    # Create a sample image
    img = Image.new('RGB', (300, 200), color='lightblue')
    draw = ImageDraw.Draw(img)
    draw.rectangle([20, 20, 280, 180], outline='darkblue', width=3)
    draw.ellipse([50, 50, 250, 150], fill='yellow', outline='orange', width=2)
    
    # Save as PNG
    png_file = os.path.join(demo_dir, "sample_image.png")
    img.save(png_file, 'PNG')
    
    # Save as JPEG
    jpg_file = os.path.join(demo_dir, "sample_photo.jpg")
    img.save(jpg_file, 'JPEG', quality=90)
    
    # Create a sample text document
    txt_file = os.path.join(demo_dir, "sample_document.txt")
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write("""Universal File Converter Demo

This is a sample text document that you can use to test the file converter.

Features:
- Convert between multiple formats
- Easy-to-use sidebar navigation
- Quick conversion buttons
- Batch processing support

Try converting this file to different formats using the GUI!
""")
    
    # Create a sample HTML file
    html_file = os.path.join(demo_dir, "sample_webpage.html")
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write("""<!DOCTYPE html>
<html>
<head>
    <title>Sample Webpage</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #333; }
        .highlight { background-color: #ffff99; }
    </style>
</head>
<body>
    <h1>Universal File Converter</h1>
    <p>This is a <span class="highlight">sample HTML file</span> for testing conversions.</p>
    <ul>
        <li>Convert HTML to PDF</li>
        <li>Convert HTML to TXT</li>
        <li>Convert HTML to DOCX</li>
    </ul>
    <p>The sidebar makes it easy to select your target format!</p>
</body>
</html>""")
    
    print(f"✅ Created demo files:")
    print(f"  📄 {txt_file}")
    print(f"  🌐 {html_file}")
    print(f"  🖼️ {png_file}")
    print(f"  📸 {jpg_file}")
    print(f"\n🚀 Now launching the GUI...")
    
    return demo_dir

def main():
    """Create demo files and launch GUI"""
    print("🎨 Universal File Converter - GUI Demo")
    print("=" * 50)
    
    # Create demo files
    demo_dir = create_demo_files()
    
    print(f"\n💡 Demo Instructions:")
    print(f"1. The GUI will open with a new sidebar")
    print(f"2. Use 'Browse' to select files from: {demo_dir}")
    print(f"3. Try the sidebar buttons to set target formats")
    print(f"4. Use the 'Quick Conversion' buttons")
    print(f"5. Check the conversion log for feedback")
    
    print(f"\n🎯 New Features to Try:")
    print(f"  📄 Documents section - Click format buttons")
    print(f"  🖼️ Images section - Quick format selection")
    print(f"  ⚡ Quick Conversions - One-click popular conversions")
    print(f"  💡 Tips section - Helpful conversion tips")
    
    # Launch the GUI
    try:
        import file_converter_gui
        print(f"\n🚀 Launching GUI...")
        file_converter_gui.main()
    except Exception as e:
        print(f"❌ Error launching GUI: {e}")
        print(f"Make sure all dependencies are installed.")

if __name__ == "__main__":
    main()
