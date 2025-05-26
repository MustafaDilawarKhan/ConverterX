#!/usr/bin/env python3
"""
Demo script to showcase the enhanced GUI with modern sidebar and drag & drop
"""

import os
import sys
import tempfile
from PIL import Image, ImageDraw

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def create_demo_files():
    """Create demo files for testing the enhanced GUI"""
    demo_dir = tempfile.mkdtemp(prefix="enhanced_gui_demo_")
    print(f"📁 Creating demo files in: {demo_dir}")

    # Create sample images with different formats
    base_img = Image.new('RGB', (400, 300), color='lightblue')
    draw = ImageDraw.Draw(base_img)

    # Draw some attractive graphics
    draw.rectangle([30, 30, 370, 270], outline='darkblue', width=4)
    draw.ellipse([80, 80, 320, 220], fill='yellow', outline='orange', width=3)
    draw.rectangle([150, 120, 250, 180], fill='red', outline='darkred', width=2)

    # Save in multiple formats for testing
    formats = {
        'sample_image.png': 'PNG',
        'sample_photo.jpg': 'JPEG',
        'sample_graphic.gif': 'GIF',
        'sample_bitmap.bmp': 'BMP'
    }

    for filename, format_name in formats.items():
        filepath = os.path.join(demo_dir, filename)
        if format_name == 'GIF':
            # Convert to palette mode for GIF
            gif_img = base_img.convert('P', palette=Image.ADAPTIVE, colors=256)
            gif_img.save(filepath, format_name)
        else:
            base_img.save(filepath, format_name, quality=90 if format_name == 'JPEG' else None)
        print(f"  ✅ Created: {filename}")

    # Create sample documents
    documents = {
        'sample_document.txt': """Universal File Converter - Enhanced GUI Demo

This is a sample text document created for testing the enhanced GUI.

NEW FEATURES:
✨ Modern sidebar with categorized format selection
🎨 Beautiful styling with hover effects
📁 Drag & drop support for easy file selection
⚡ Quick conversion buttons for popular tasks
💡 Built-in tips and guidance

CONVERSION CATEGORIES:
📄 Documents: DOCX, PDF, TXT, HTML, RTF, MD
🖼️ Images: PNG, JPEG, GIF, BMP, TIFF, WebP, ICO, SVG
📊 Spreadsheets: XLSX, CSV

Try converting this file to different formats using the sidebar!
""",

        'sample_webpage.html': """<!DOCTYPE html>
<html>
<head>
    <title>Enhanced GUI Demo</title>
    <style>
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            margin: 40px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }
        h1 { color: #fff; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
        .feature {
            background: rgba(255,255,255,0.2);
            padding: 15px;
            margin: 10px 0;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Enhanced File Converter GUI</h1>

        <div class="feature">
            <h3>✨ Modern Design</h3>
            <p>Beautiful sidebar with categorized format selection</p>
        </div>

        <div class="feature">
            <h3>📁 Drag & Drop</h3>
            <p>Simply drag files into the application for instant conversion</p>
        </div>

        <div class="feature">
            <h3>⚡ Quick Conversions</h3>
            <p>One-click buttons for popular conversion tasks</p>
        </div>

        <div class="feature">
            <h3>🎨 Smart Styling</h3>
            <p>Hover effects, modern colors, and intuitive layout</p>
        </div>
    </div>
</body>
</html>"""
    }

    for filename, content in documents.items():
        filepath = os.path.join(demo_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Created: {filename}")

    return demo_dir

def main():
    """Create demo files and launch enhanced GUI"""
    print("🎨 Universal File Converter - Enhanced GUI Demo")
    print("=" * 55)

    # Create demo files
    demo_dir = create_demo_files()

    print(f"\n🎯 NEW FEATURES TO TEST:")
    print(f"┌─────────────────────────────────────────────────────┐")
    print(f"│ 🎨 MODERN SIDEBAR                                   │")
    print(f"│   • Categorized format buttons (Documents/Images)  │")
    print(f"│   • Beautiful hover effects and styling            │")
    print(f"│   • Clear visual hierarchy                          │")
    print(f"│                                                     │")
    print(f"│ 📁 MAIN WINDOW DRAG & DROP                         │")
    print(f"│   • Large drop zone in main content area           │")
    print(f"│   • Drop files directly for instant conversion     │")
    print(f"│   • Visual feedback and hover effects              │")
    print(f"│                                                     │")
    print(f"│ ⚡ QUICK CONVERSIONS                                │")
    print(f"│   • DOCX → PDF (most popular)                      │")
    print(f"│   • PNG → JPG (with transparency handling)         │")
    print(f"│   • Images → PDF (any image to PDF)                │")
    print(f"│                                                     │")
    print(f"│ 💡 SMART FEATURES                                  │")
    print(f"│   • Built-in tips and guidance                     │")
    print(f"│   • Format-specific recommendations                │")
    print(f"│   • Enhanced file type filtering                   │")
    print(f"└─────────────────────────────────────────────────────┘")

    print(f"\n📂 Demo Files Location: {demo_dir}")
    print(f"\n🚀 Instructions:")
    print(f"1. The enhanced GUI will open with the new sidebar")
    print(f"2. Try clicking format buttons in the sidebar categories")
    print(f"3. Use the MAIN WINDOW drag & drop zone for files")
    print(f"4. Test the quick conversion buttons")
    print(f"5. Notice the modern styling and hover effects")

    print(f"\n🎨 Visual Improvements:")
    print(f"• Modern color scheme with professional styling")
    print(f"• Categorized sidebar with clear sections")
    print(f"• Hover effects on buttons")
    print(f"• Drag & drop visual feedback")
    print(f"• Better typography and spacing")

    # Launch the enhanced GUI
    try:
        print(f"\n🚀 Launching Enhanced GUI...")
        import file_converter_gui
        file_converter_gui.main()
    except Exception as e:
        print(f"❌ Error launching GUI: {e}")
        print(f"Make sure all dependencies are installed:")
        print(f"  pip install tkinterdnd2")

if __name__ == "__main__":
    main()
