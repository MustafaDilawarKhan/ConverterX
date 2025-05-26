#!/bin/bash

# Universal File Converter - Linux Installation Script
# This script installs system dependencies and Python packages for Linux

set -e  # Exit on any error

echo "🚀 Universal File Converter - Linux Installation"
echo "================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠️${NC} $1"
}

print_error() {
    echo -e "${RED}❌${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ️${NC} $1"
}

# Detect Linux distribution
detect_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        DISTRO=$ID
        VERSION=$VERSION_ID
    else
        print_error "Cannot detect Linux distribution"
        exit 1
    fi
    
    print_info "Detected: $PRETTY_NAME"
}

# Install system dependencies based on distribution
install_system_deps() {
    echo -e "\n📦 Installing system dependencies..."
    
    case $DISTRO in
        "fedora"|"rhel"|"centos")
            print_info "Installing packages for Fedora/RHEL/CentOS..."
            sudo dnf update -y
            sudo dnf install -y python3 python3-pip python3-tkinter python3-devel
            
            # Ask about LibreOffice
            echo -e "\n${BLUE}LibreOffice provides the best DOCX→PDF conversion quality.${NC}"
            read -p "Install LibreOffice? (recommended) [Y/n]: " install_libreoffice
            if [[ $install_libreoffice != "n" && $install_libreoffice != "N" ]]; then
                sudo dnf install -y libreoffice
                print_status "LibreOffice installed"
            fi
            
            # Optional packages
            read -p "Install poppler-utils for better PDF handling? [Y/n]: " install_poppler
            if [[ $install_poppler != "n" && $install_poppler != "N" ]]; then
                sudo dnf install -y poppler-utils
                print_status "Poppler-utils installed"
            fi
            ;;
            
        "ubuntu"|"debian")
            print_info "Installing packages for Ubuntu/Debian..."
            sudo apt-get update
            sudo apt-get install -y python3 python3-pip python3-tk python3-dev
            
            # Ask about LibreOffice
            echo -e "\n${BLUE}LibreOffice provides the best DOCX→PDF conversion quality.${NC}"
            read -p "Install LibreOffice? (recommended) [Y/n]: " install_libreoffice
            if [[ $install_libreoffice != "n" && $install_libreoffice != "N" ]]; then
                sudo apt-get install -y libreoffice
                print_status "LibreOffice installed"
            fi
            
            # Optional packages
            read -p "Install poppler-utils for better PDF handling? [Y/n]: " install_poppler
            if [[ $install_poppler != "n" && $install_poppler != "N" ]]; then
                sudo apt-get install -y poppler-utils
                print_status "Poppler-utils installed"
            fi
            ;;
            
        "arch"|"manjaro")
            print_info "Installing packages for Arch Linux..."
            sudo pacman -Sy --noconfirm python python-pip tk
            
            # Ask about LibreOffice
            echo -e "\n${BLUE}LibreOffice provides the best DOCX→PDF conversion quality.${NC}"
            read -p "Install LibreOffice? (recommended) [Y/n]: " install_libreoffice
            if [[ $install_libreoffice != "n" && $install_libreoffice != "N" ]]; then
                sudo pacman -S --noconfirm libreoffice-fresh
                print_status "LibreOffice installed"
            fi
            
            # Optional packages
            read -p "Install poppler for better PDF handling? [Y/n]: " install_poppler
            if [[ $install_poppler != "n" && $install_poppler != "N" ]]; then
                sudo pacman -S --noconfirm poppler
                print_status "Poppler installed"
            fi
            ;;
            
        *)
            print_warning "Unsupported distribution: $DISTRO"
            print_info "Please install manually:"
            print_info "- python3, python3-pip, python3-tkinter"
            print_info "- libreoffice (recommended)"
            print_info "- poppler-utils (optional)"
            ;;
    esac
}

# Install Python dependencies
install_python_deps() {
    echo -e "\n🐍 Installing Python dependencies..."
    
    # Check if we should use virtual environment
    read -p "Create virtual environment? (recommended) [Y/n]: " use_venv
    if [[ $use_venv != "n" && $use_venv != "N" ]]; then
        print_info "Creating virtual environment..."
        python3 -m venv converter_env
        source converter_env/bin/activate
        print_status "Virtual environment created and activated"
        
        # Create activation script
        cat > activate_converter.sh << 'EOF'
#!/bin/bash
echo "Activating Universal File Converter environment..."
source converter_env/bin/activate
echo "Environment activated. Run 'deactivate' to exit."
EOF
        chmod +x activate_converter.sh
        print_status "Created activation script: ./activate_converter.sh"
    fi
    
    # Upgrade pip
    python3 -m pip install --upgrade pip
    
    # Install requirements
    if [ -f requirements.txt ]; then
        python3 -m pip install -r requirements.txt
        print_status "Python dependencies installed"
    else
        print_error "requirements.txt not found"
        exit 1
    fi
}

# Test installation
test_installation() {
    echo -e "\n🧪 Testing installation..."
    
    if python3 test_converter.py > /dev/null 2>&1; then
        print_status "Installation test passed"
    else
        print_warning "Some tests failed, but basic functionality should work"
    fi
}

# Create desktop entry
create_desktop_entry() {
    read -p "Create desktop entry for GUI? [Y/n]: " create_desktop
    if [[ $create_desktop != "n" && $create_desktop != "N" ]]; then
        DESKTOP_DIR="$HOME/.local/share/applications"
        mkdir -p "$DESKTOP_DIR"
        
        CURRENT_DIR=$(pwd)
        
        cat > "$DESKTOP_DIR/file-converter.desktop" << EOF
[Desktop Entry]
Name=Universal File Converter
Comment=Convert between various document formats
Exec=python3 $CURRENT_DIR/file_converter_gui.py
Icon=applications-office
Terminal=false
Type=Application
Categories=Office;Utility;
EOF
        
        # Update desktop database if available
        if command -v update-desktop-database > /dev/null; then
            update-desktop-database "$DESKTOP_DIR"
        fi
        
        print_status "Desktop entry created"
    fi
}

# Main installation process
main() {
    detect_distro
    install_system_deps
    install_python_deps
    test_installation
    create_desktop_entry
    
    echo -e "\n🎉 Installation completed!"
    echo -e "\n${GREEN}To get started:${NC}"
    echo "  • GUI: python3 file_converter_gui.py"
    echo "  • CLI: python3 cli_converter.py --help"
    echo "  • Test: python3 test_converter.py"
    
    if [ -f activate_converter.sh ]; then
        echo -e "\n${BLUE}Virtual environment created.${NC}"
        echo "  • Activate: source activate_converter.sh"
        echo "  • Or: source converter_env/bin/activate"
    fi
    
    echo -e "\n📚 See LINUX_INSTALL.md for detailed documentation"
}

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    print_error "Don't run this script as root (except for system package installation)"
    exit 1
fi

# Check if Python 3 is available
if ! command -v python3 > /dev/null; then
    print_error "Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Run main installation
main
