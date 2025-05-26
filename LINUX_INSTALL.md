# Linux Installation Guide - Universal File Converter v2.0

Complete installation instructions for Linux distributions including Ubuntu, Debian, Fedora, CentOS, RHEL, Arch Linux, and more.

**New in v2.0:** Full video/audio conversion support with FFmpeg integration and enhanced GUI interface.

## 🎬 What's New in v2.0

### ✨ **Video/Audio Conversion (35+ formats)**
- **Video formats**: MP4, AVI, MOV, WMV, FLV, MKV, WebM, M4V, 3GP
- **Audio formats**: MP3, WAV, AAC, FLAC, OGG, M4A, WMA
- **Video → Audio**: Extract audio tracks from any video
- **Video → GIF**: Create optimized animated GIFs
- **Audio conversion**: Between all supported audio formats

### 🔧 **Enhanced Linux Support**
- **FFmpeg integration**: System-level video/audio processing
- **Dual engine**: MoviePy + FFmpeg fallback for maximum compatibility
- **Package manager support**: Native installation for all major distributions
- **X11/Wayland**: Full GUI compatibility across desktop environments

### 🎨 **Improved Interface**
- **Cleaner sidebar**: Removed quick conversions for simplified workflow
- **Better organization**: Format buttons grouped by category
- **Enhanced drag & drop**: Batch file processing with visual feedback
- **Professional styling**: Modern design with hover effects

## 🐧 Quick Start (Ubuntu/Debian)

```bash
# 1. Update system
sudo apt update && sudo apt upgrade -y

# 2. Install system dependencies
sudo apt install -y python3 python3-pip python3-tk python3-dev build-essential ffmpeg wkhtmltopdf git

# 3. Clone repository
git clone <repository-url>
cd universal-file-converter

# 4. Install Python dependencies
pip3 install -r requirements.txt

# 5. Run the application
python3 file_converter_gui.py
```

## 📦 Distribution-Specific Instructions

### **Ubuntu 20.04+ / Debian 11+**

#### **Standard Installation**
```bash
# Update package list
sudo apt update

# Install Python and development tools
sudo apt install -y python3 python3-pip python3-venv python3-tk python3-dev

# Install multimedia tools
sudo apt install -y ffmpeg wkhtmltopdf

# Install build tools for Python packages
sudo apt install -y build-essential libffi-dev libssl-dev

# Clone and setup
git clone <repository-url>
cd universal-file-converter
pip3 install -r requirements.txt
```

#### **If FFmpeg is not available:**
```bash
# Enable universe repository
sudo add-apt-repository universe
sudo apt update
sudo apt install ffmpeg

# Alternative: Install via snap
sudo snap install ffmpeg
```

### **Fedora 35+ / RHEL 8+ / CentOS 8+**

#### **Standard Installation**
```bash
# Install system dependencies
sudo dnf install -y python3 python3-pip python3-tkinter python3-devel

# Install multimedia tools
sudo dnf install -y ffmpeg wkhtmltopdf

# Install development tools
sudo dnf groupinstall -y "Development Tools"
sudo dnf install -y openssl-devel libffi-devel

# Clone and setup
git clone <repository-url>
cd universal-file-converter
pip3 install -r requirements.txt
```

#### **Enable RPM Fusion for FFmpeg:**
```bash
# Enable RPM Fusion repositories
sudo dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install -y https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

# Install FFmpeg
sudo dnf install -y ffmpeg
```

### **Arch Linux / Manjaro**

```bash
# Update system
sudo pacman -Syu

# Install dependencies
sudo pacman -S python python-pip tk ffmpeg wkhtmltopdf git base-devel

# Clone and setup
git clone <repository-url>
cd universal-file-converter
pip install -r requirements.txt
```

### **openSUSE Leap / Tumbleweed**

```bash
# Install dependencies
sudo zypper install -y python3 python3-pip python3-tk python3-devel

# Install multimedia (may require Packman repository)
sudo zypper install -y ffmpeg wkhtmltopdf

# Install development tools
sudo zypper install -y gcc make

# Clone and setup
git clone <repository-url>
cd universal-file-converter
pip3 install -r requirements.txt
```

### **Alpine Linux**

```bash
# Install dependencies
sudo apk add python3 py3-pip python3-dev py3-tkinter

# Install multimedia tools
sudo apk add ffmpeg wkhtmltopdf

# Install build tools
sudo apk add gcc musl-dev libffi-dev openssl-dev

# Clone and setup
git clone <repository-url>
cd universal-file-converter
pip3 install -r requirements.txt
```

## 🔧 Advanced Installation Options

### **Using Virtual Environment (Recommended)**

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python file_converter_gui.py

# Deactivate when done
deactivate
```

### **User-Level Installation (No sudo required)**

```bash
# Install Python packages for user only
pip3 install --user -r requirements.txt

# Add user bin to PATH (add to ~/.bashrc)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Run application
python3 file_converter_gui.py
```

### **Docker Installation**

```bash
# Create Dockerfile
cat > Dockerfile << 'EOF'
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-tk \
    ffmpeg wkhtmltopdf \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
CMD ["python3", "file_converter_gui.py"]
EOF

# Build and run
docker build -t universal-file-converter .
docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix universal-file-converter
```

## 🛠️ Troubleshooting Linux Issues

### **GUI Won't Start**

#### **Missing tkinter:**
```bash
# Ubuntu/Debian
sudo apt install python3-tk

# Fedora/RHEL
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk
```

#### **X11 Display Issues:**
```bash
# Check DISPLAY variable
echo $DISPLAY

# For SSH sessions, use X11 forwarding
ssh -X username@hostname

# For Wayland, install XWayland
sudo apt install xwayland  # Ubuntu/Debian
sudo dnf install xorg-x11-server-Xwayland  # Fedora
```

### **FFmpeg Issues**

#### **FFmpeg not found:**
```bash
# Check if FFmpeg is installed
which ffmpeg
ffmpeg -version

# Install from different sources
sudo apt install ffmpeg  # Ubuntu/Debian
sudo dnf install ffmpeg  # Fedora (with RPM Fusion)
sudo pacman -S ffmpeg    # Arch Linux
sudo snap install ffmpeg # Universal (snap)
```

#### **FFmpeg permission issues:**
```bash
# Check FFmpeg permissions
ls -la $(which ffmpeg)

# If needed, make executable
sudo chmod +x $(which ffmpeg)
```

### **Python Package Issues**

#### **Permission denied errors:**
```bash
# Use user installation
pip3 install --user -r requirements.txt

# Or fix permissions
sudo chown -R $USER:$USER ~/.local/
```

#### **Build failures:**
```bash
# Install development headers
sudo apt install python3-dev build-essential  # Ubuntu/Debian
sudo dnf install python3-devel gcc            # Fedora/RHEL
sudo pacman -S base-devel                      # Arch Linux
```

### **Audio/Video Codec Issues**

#### **Missing codecs:**
```bash
# Ubuntu/Debian - install restricted extras
sudo apt install ubuntu-restricted-extras

# Fedora - install multimedia codecs
sudo dnf install gstreamer1-plugins-{bad-*,good-*,base} gstreamer1-plugin-openh264 gstreamer1-libav --exclude=gstreamer1-plugins-bad-free-devel

# Install additional codecs
sudo apt install libavcodec-extra  # Ubuntu/Debian
```

## 🚀 Performance Optimization

### **System Optimization**
```bash
# Increase file descriptor limits
echo "* soft nofile 65536" | sudo tee -a /etc/security/limits.conf
echo "* hard nofile 65536" | sudo tee -a /etc/security/limits.conf

# Optimize for SSD (if applicable)
sudo systemctl enable fstrim.timer
```

### **Python Optimization**
```bash
# Use faster Python implementation (optional)
sudo apt install pypy3  # Ubuntu/Debian
sudo dnf install pypy3  # Fedora

# Run with PyPy (if compatible)
pypy3 file_converter_gui.py
```

## 📋 Verification

### **Test Installation**
```bash
# Test Python imports
python3 -c "import tkinter; print('✅ tkinter OK')"
python3 -c "import PIL; print('✅ Pillow OK')"
python3 -c "import pandas; print('✅ pandas OK')"

# Test system tools
ffmpeg -version && echo "✅ FFmpeg OK"
wkhtmltopdf --version && echo "✅ wkhtmltopdf OK"

# Test GUI (should open window)
python3 -c "import tkinter; tkinter.Tk().mainloop()"

# Create test files for video conversion
python3 create_test_video.py

# Test video conversion capabilities
python3 quick_video_test.py
```

### **Test Video Conversion Features**
```bash
# Test video to audio extraction
ffmpeg -i test_video.mp4 -vn -acodec mp3 -ab 192k test_audio.mp3

# Test video to GIF conversion
ffmpeg -i test_video.mp4 -vf "scale=320:-1:flags=lanczos,fps=10" test_animation.gif

# Test video format conversion
ffmpeg -i test_video.mp4 -c:v libx264 -c:a aac test_converted.avi

# Verify outputs
ls -la test_*.{mp3,gif,avi} 2>/dev/null && echo "✅ Video conversion working"
```

### **Run Application**
```bash
# Start the GUI
python3 file_converter_gui.py

# If successful, you should see the Universal File Converter window
```

## 🆘 Getting Help

If you encounter issues:

1. **Check system logs**: `journalctl -xe`
2. **Verify Python version**: `python3 --version` (3.8+ required)
3. **Check dependencies**: Run verification commands above
4. **Review error messages**: Look for specific missing packages
5. **Search package repositories**: Use your distribution's package search
6. **Community support**: Check distribution-specific forums

## 📚 Additional Resources

- **Ubuntu Packages**: https://packages.ubuntu.com/
- **Fedora Packages**: https://packages.fedoraproject.org/
- **Arch Packages**: https://archlinux.org/packages/
- **FFmpeg Documentation**: https://ffmpeg.org/documentation.html
- **Python Virtual Environments**: https://docs.python.org/3/tutorial/venv.html

---

## 🎉 **v2.0 Features Ready on Linux**

The Universal File Converter v2.0 now provides **full video/audio conversion capabilities** on Linux with:

- ✅ **35+ format support** including all major video and audio formats
- ✅ **FFmpeg integration** for professional-grade media processing
- ✅ **Batch conversion** with drag & drop interface
- ✅ **Cross-platform compatibility** across all major Linux distributions
- ✅ **Enhanced GUI** with categorized format selection
- ✅ **Robust error handling** with detailed diagnostics

**Ready to convert:** Videos, audio files, documents, images, and spreadsheets - all in one application! 🎬🎵📄🖼️📊

---

**Note**: This guide covers most common Linux distributions. For other distributions, adapt the package manager commands accordingly (e.g., `zypper` for openSUSE, `emerge` for Gentoo, etc.).
