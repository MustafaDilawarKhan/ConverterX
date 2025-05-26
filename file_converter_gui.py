"""
GUI Application for Universal File Converter
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import tkinter.dnd as dnd
import threading
import os
from pathlib import Path
import config
import utils
from converter_core import DocumentConverter

class FileConverterGUI:
    def __init__(self, root):
        # Setup drag and drop first (creates root if needed)
        self.setup_drag_drop()

        # If root was provided, use it; otherwise use the one created in setup_drag_drop
        if root is not None:
            self.root = root
            self.root.title(config.APP_NAME)
            self.root.geometry(config.WINDOW_SIZE)
            self.root.minsize(*config.WINDOW_MIN_SIZE)

        # Configure modern styling
        self.setup_styles()

        self.converter = DocumentConverter()
        self.setup_logging()
        self.create_widgets()

    def setup_logging(self):
        """Setup logging for the application"""
        utils.setup_logging()

    def setup_styles(self):
        """Setup modern styling for the application"""
        style = ttk.Style()

        # Configure modern theme
        style.theme_use('clam')

        # Sidebar styling
        style.configure('Sidebar.TFrame',
                       background='#f8f9fa',
                       relief='solid',
                       borderwidth=1)

        # Category button styling
        style.configure('Category.TButton',
                       background='#e9ecef',
                       foreground='#495057',
                       borderwidth=1,
                       focuscolor='none',
                       font=('Segoe UI', 9))

        style.map('Category.TButton',
                 background=[('active', '#dee2e6'),
                           ('pressed', '#ced4da')])

        # Format button styling
        style.configure('Format.TButton',
                       background='#ffffff',
                       foreground='#212529',
                       borderwidth=1,
                       focuscolor='none',
                       font=('Segoe UI', 8, 'bold'))

        style.map('Format.TButton',
                 background=[('active', '#e3f2fd'),
                           ('pressed', '#bbdefb')])

        # Quick conversion button styling
        style.configure('Quick.TButton',
                       background='#007bff',
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none',
                       font=('Segoe UI', 9, 'bold'))

        style.map('Quick.TButton',
                 background=[('active', '#0056b3'),
                           ('pressed', '#004085')])

        # Drop zone styling
        style.configure('DropZone.TFrame',
                       background='#f8f9fa',
                       relief='dashed',
                       borderwidth=2)

    def setup_drag_drop(self):
        """Setup drag and drop functionality"""
        try:
            # Try to enable drag and drop using tkinterdnd2 if available
            import tkinterdnd2
            # Initialize tkinterdnd2 for the existing root
            self.root = tkinterdnd2.TkinterDnD.Tk()
            self.root.title(config.APP_NAME)
            self.root.geometry(config.WINDOW_SIZE)
            self.root.minsize(*config.WINDOW_MIN_SIZE)

            self.root.drop_target_register(tkinterdnd2.DND_FILES)
            self.root.dnd_bind('<<Drop>>', self.on_drop)
            # Delay the log message until after GUI is created
            self.root.after(100, lambda: self.log_message("✅ Drag & drop enabled - you can drop files directly into the window!"))
        except (ImportError, Exception) as e:
            # Fallback: create regular Tk window
            self.root = tk.Tk()
            self.root.title(config.APP_NAME)
            self.root.geometry(config.WINDOW_SIZE)
            self.root.minsize(*config.WINDOW_MIN_SIZE)
            # Delay the log message until after GUI is created
            self.root.after(100, lambda: self.log_message("ℹ️ Drag & drop not available - use Browse button to select files"))

    def on_drop(self, event):
        """Handle dropped files"""
        try:
            files = event.data.split()
            if files:
                # Take the first file
                file_path = files[0].strip('{}')  # Remove braces if present
                self.input_file_var.set(file_path)
                self.log_message(f"File dropped: {os.path.basename(file_path)}")
        except Exception as e:
            self.log_message(f"Error handling dropped file: {str(e)}")

    def create_widgets(self):
        """Create and arrange GUI widgets"""
        # Create main container with sidebar and content
        container = ttk.Frame(self.root)
        container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)
        container.rowconfigure(0, weight=1)

        # Create sidebar
        self.create_sidebar(container)

        # Create main content area
        main_frame = ttk.Frame(container, padding="10")
        main_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.columnconfigure(1, weight=1)

        # Title
        title_label = ttk.Label(main_frame, text=config.APP_NAME,
                               font=('Segoe UI', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 15))

        # Add drag & drop zone in main area
        self.create_main_drop_zone(main_frame, 1)

        # Initialize input file variable (no UI display needed)
        self.input_file_var = tk.StringVar()

        # Source format (auto-detected)
        ttk.Label(main_frame, text="Source Format:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.source_format_var = tk.StringVar()
        self.source_format_label = ttk.Label(main_frame, textvariable=self.source_format_var,
                                            foreground="blue")
        self.source_format_label.grid(row=2, column=1, sticky=tk.W, padx=(5, 0), pady=5)

        # Target format selection
        ttk.Label(main_frame, text="Target Format:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.target_format_var = tk.StringVar()
        self.target_format_combo = ttk.Combobox(main_frame, textvariable=self.target_format_var,
                                               state="readonly", width=20)
        self.target_format_combo.grid(row=3, column=1, sticky=tk.W, padx=(5, 0), pady=5)

        # Output directory selection
        ttk.Label(main_frame, text="Output Directory:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.output_dir_var = tk.StringVar(value=config.DEFAULT_OUTPUT_DIR)
        self.output_dir_entry = ttk.Entry(main_frame, textvariable=self.output_dir_var, width=50)
        self.output_dir_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), padx=(5, 5), pady=5)
        ttk.Button(main_frame, text="Browse",
                  command=self.browse_output_dir).grid(row=4, column=2, pady=5)

        # Convert button
        self.convert_button = ttk.Button(main_frame, text="Convert File",
                                        command=self.convert_file, style="Quick.TButton")
        self.convert_button.grid(row=5, column=0, columnspan=3, pady=20)

        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(main_frame, variable=self.progress_var,
                                           mode='indeterminate')
        self.progress_bar.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)

        # Status label
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(main_frame, textvariable=self.status_var)
        self.status_label.grid(row=7, column=0, columnspan=3, pady=5)

        # Log area
        ttk.Label(main_frame, text="Conversion Log:").grid(row=8, column=0, sticky=tk.W, pady=(20, 5))
        self.log_text = scrolledtext.ScrolledText(main_frame, height=10, width=80)
        self.log_text.grid(row=9, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        # Configure grid weights for resizing
        main_frame.rowconfigure(9, weight=1)

        # Bind events
        self.input_file_var.trace('w', self.on_input_file_change)

    def create_sidebar(self, parent):
        """Create modern sidebar with conversion categories"""
        # Create scrollable sidebar
        sidebar_canvas = tk.Canvas(parent, width=200, bg='#f8f9fa', highlightthickness=0)
        sidebar_scrollbar = ttk.Scrollbar(parent, orient="vertical", command=sidebar_canvas.yview)
        sidebar_frame = ttk.Frame(sidebar_canvas, style="Sidebar.TFrame")

        # Configure scrolling
        sidebar_frame.bind(
            "<Configure>",
            lambda e: sidebar_canvas.configure(scrollregion=sidebar_canvas.bbox("all"))
        )

        sidebar_canvas.create_window((0, 0), window=sidebar_frame, anchor="nw")
        sidebar_canvas.configure(yscrollcommand=sidebar_scrollbar.set)

        # Grid the canvas and scrollbar
        sidebar_canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        sidebar_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Configure the actual sidebar content
        sidebar = ttk.Frame(sidebar_frame, padding="10")
        sidebar.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        sidebar.columnconfigure(0, weight=1)

        # Sidebar title with modern styling
        title_frame = ttk.Frame(sidebar)
        title_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 20))
        title_frame.columnconfigure(0, weight=1)

        sidebar_title = ttk.Label(title_frame, text="🔄 File Converter",
                                 font=('Segoe UI', 14, 'bold'),
                                 foreground='#212529')
        sidebar_title.grid(row=0, column=0, sticky=tk.W)

        subtitle = ttk.Label(title_frame, text="Choose your conversion type",
                            font=('Segoe UI', 9),
                            foreground='#6c757d')
        subtitle.grid(row=1, column=0, sticky=tk.W, pady=(2, 0))

        # Category sections with compact styling
        self.create_category_section(sidebar, "📄 Documents", [
            ("DOCX", "Word Documents"),
            ("PDF", "PDF Files"),
            ("TXT", "Text Files"),
            ("HTML", "Web Pages"),
            ("RTF", "Rich Text"),
            ("MD", "Markdown")
        ], 1)

        self.create_category_section(sidebar, "🖼️ Images", [
            ("PNG", "PNG Images"),
            ("JPG", "JPEG Images"),
            ("GIF", "GIF Images"),
            ("BMP", "Bitmap Images"),
            ("TIFF", "TIFF Images"),
            ("WebP", "WebP Images"),
            ("ICO", "Icon Files"),
            ("SVG", "Vector Graphics")
        ], 2)

        self.create_category_section(sidebar, "📊 Spreadsheets", [
            ("XLSX", "Excel Files"),
            ("CSV", "CSV Files")
        ], 3)

        # Quick conversion buttons with modern styling
        ttk.Separator(sidebar, orient='horizontal').grid(row=4, column=0, sticky=(tk.W, tk.E), pady=(10, 5))

        quick_title = ttk.Label(sidebar, text="⚡ Quick Conversions",
                               font=('Segoe UI', 10, 'bold'),
                               foreground='#212529')
        quick_title.grid(row=5, column=0, sticky=tk.W, pady=(0, 5))

        # Popular conversion buttons with compact styling
        quick_conversions = [
            ("DOCX → PDF", self.quick_docx_to_pdf),
            ("PDF → TXT", self.quick_pdf_to_txt),
            ("PNG → JPG", self.quick_png_to_jpg),
            ("JPG → PNG", self.quick_jpg_to_png),
            ("Images → PDF", self.quick_images_to_pdf)
        ]

        for i, (text, command) in enumerate(quick_conversions):
            btn = ttk.Button(sidebar, text=text, command=command,
                           style="Quick.TButton", width=16)
            btn.grid(row=6+i, column=0, sticky=(tk.W, tk.E), pady=1)

        # Tips section
        ttk.Separator(sidebar, orient='horizontal').grid(row=11, column=0, sticky=(tk.W, tk.E), pady=(10, 5))

        tips_title = ttk.Label(sidebar, text="💡 Tips",
                              font=('Segoe UI', 10, 'bold'),
                              foreground='#212529')
        tips_title.grid(row=12, column=0, sticky=tk.W, pady=(0, 5))

        tips_text = tk.Text(sidebar, height=4, width=22, wrap=tk.WORD,
                           font=('Segoe UI', 8), bg='#f8f9fa', relief='flat',
                           borderwidth=0, highlightthickness=0)
        tips_text.grid(row=13, column=0, sticky=(tk.W, tk.E), pady=5)

        tips_content = """• Drag & drop files for quick selection
• PNG preserves transparency
• JPEG is smaller for photos
• PDF is great for documents"""

        tips_text.insert('1.0', tips_content)
        tips_text.config(state='disabled')

    def create_main_drop_zone(self, parent, row):
        """Create main drag & drop zone in the content area"""
        drop_frame = ttk.Frame(parent, style="DropZone.TFrame", padding="20")
        drop_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        drop_frame.columnconfigure(0, weight=1)

        # Drop zone content with larger, more prominent design
        drop_icon = ttk.Label(drop_frame, text="📁", font=('Segoe UI', 32))
        drop_icon.grid(row=0, column=0, pady=(10, 5))

        drop_title = ttk.Label(drop_frame, text="Drag & Drop Files Here",
                              font=('Segoe UI', 14, 'bold'),
                              foreground='#495057')
        drop_title.grid(row=1, column=0, pady=(0, 5))

        drop_subtitle = ttk.Label(drop_frame, text="or use the Browse button below",
                                 font=('Segoe UI', 10),
                                 foreground='#6c757d')
        drop_subtitle.grid(row=2, column=0, pady=(0, 10))

        # Supported formats hint
        formats_hint = ttk.Label(drop_frame,
                               text="Supports: DOCX, PDF, TXT, HTML, PNG, JPG, GIF, BMP, TIFF, WebP, ICO, SVG, XLSX, CSV",
                               font=('Segoe UI', 8),
                               foreground='#adb5bd')
        formats_hint.grid(row=3, column=0, pady=(0, 10))

        # Bind drag and drop events to the entire drop zone
        self.setup_drop_zone_events(drop_frame)
        self.setup_drop_zone_events(drop_icon)
        self.setup_drop_zone_events(drop_title)
        self.setup_drop_zone_events(drop_subtitle)
        self.setup_drop_zone_events(formats_hint)

        # Enable drag and drop on the drop zone
        try:
            import tkinterdnd2
            # Only register if tkinterdnd2 was properly initialized
            if hasattr(self.root, 'tk') and hasattr(self.root.tk, 'call'):
                drop_frame.drop_target_register(tkinterdnd2.DND_FILES)
                drop_frame.dnd_bind('<<Drop>>', self.on_drop)
        except (ImportError, Exception):
            pass

    def setup_drop_zone_events(self, widget):
        """Setup events for drop zone widgets"""
        widget.bind('<Button-1>', lambda e: self.browse_input_file())
        widget.bind('<Enter>', self.on_drop_zone_enter)
        widget.bind('<Leave>', self.on_drop_zone_leave)

    def on_drop_zone_enter(self, event):
        """Handle mouse enter on drop zone"""
        event.widget.configure(cursor='hand2')

    def on_drop_zone_leave(self, event):
        """Handle mouse leave on drop zone"""
        event.widget.configure(cursor='')

    def create_drop_zone(self, parent, row):
        """Create drag & drop zone"""
        drop_frame = ttk.Frame(parent, style="DropZone.TFrame", padding="10")
        drop_frame.grid(row=row, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        drop_frame.columnconfigure(0, weight=1)

        # Drop zone icon and text
        drop_icon = ttk.Label(drop_frame, text="📁", font=('Segoe UI', 24))
        drop_icon.grid(row=0, column=0, pady=(5, 0))

        drop_title = ttk.Label(drop_frame, text="Drag & Drop Files Here",
                              font=('Segoe UI', 10, 'bold'),
                              foreground='#6c757d')
        drop_title.grid(row=1, column=0, pady=(0, 2))

        drop_subtitle = ttk.Label(drop_frame, text="or click Browse below",
                                 font=('Segoe UI', 8),
                                 foreground='#adb5bd')
        drop_subtitle.grid(row=2, column=0, pady=(0, 5))

        # Bind drag and drop events
        drop_frame.bind('<Button-1>', lambda e: self.browse_input_file())
        drop_icon.bind('<Button-1>', lambda e: self.browse_input_file())
        drop_title.bind('<Button-1>', lambda e: self.browse_input_file())
        drop_subtitle.bind('<Button-1>', lambda e: self.browse_input_file())

    def create_category_section(self, parent, title, formats, row):
        """Create a compact category section in the sidebar"""
        # Category title with compact styling
        category_label = ttk.Label(parent, text=title,
                                  font=('Segoe UI', 9, 'bold'),
                                  foreground='#495057')
        category_label.grid(row=row, column=0, sticky=tk.W, pady=(8, 3))

        # Format grid with compact buttons
        formats_frame = ttk.Frame(parent)
        formats_frame.grid(row=row, column=0, sticky=(tk.W, tk.E), padx=(0, 0), pady=(20, 5))
        formats_frame.columnconfigure(0, weight=1)
        formats_frame.columnconfigure(1, weight=1)

        for i, (format_code, _) in enumerate(formats):
            format_btn = ttk.Button(formats_frame, text=f"{format_code}",
                                   command=lambda f=format_code.lower(): self.set_target_format(f),
                                   style="Format.TButton",
                                   width=8)
            format_btn.grid(row=i//2, column=i%2, sticky=(tk.W, tk.E), padx=1, pady=1)

            # Add hover effect
            format_btn.bind('<Enter>', lambda e, btn=format_btn: btn.configure(style="Format.TButton"))
            format_btn.bind('<Leave>', lambda e, btn=format_btn: btn.configure(style="Format.TButton"))

    def browse_input_file(self):
        """Open file dialog to select input file"""
        filetypes = [
            ("All Supported", "*.docx;*.pdf;*.txt;*.html;*.rtf;*.md;*.xlsx;*.csv;*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff;*.tif;*.webp;*.ico;*.svg"),
            ("Word Documents", "*.docx"),
            ("PDF Files", "*.pdf"),
            ("Text Files", "*.txt"),
            ("HTML Files", "*.html;*.htm"),
            ("RTF Files", "*.rtf"),
            ("Markdown Files", "*.md"),
            ("Excel Files", "*.xlsx"),
            ("CSV Files", "*.csv"),
            ("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff;*.tif;*.webp;*.ico;*.svg"),
            ("PNG Images", "*.png"),
            ("JPEG Images", "*.jpg;*.jpeg"),
            ("GIF Images", "*.gif"),
            ("BMP Images", "*.bmp"),
            ("TIFF Images", "*.tiff;*.tif"),
            ("WebP Images", "*.webp"),
            ("Icon Files", "*.ico"),
            ("SVG Images", "*.svg"),
            ("All Files", "*.*")
        ]

        filename = filedialog.askopenfilename(
            title="Select Input File",
            filetypes=filetypes
        )

        if filename:
            self.input_file_var.set(filename)
            self.log_message(f"File selected: {os.path.basename(filename)}")

    def browse_output_dir(self):
        """Open directory dialog to select output directory"""
        directory = filedialog.askdirectory(
            title="Select Output Directory",
            initialdir=self.output_dir_var.get()
        )

        if directory:
            self.output_dir_var.set(directory)

    def on_input_file_change(self, *args):
        """Handle input file change event"""
        input_file = self.input_file_var.get()

        if input_file and os.path.exists(input_file):
            # Detect source format
            source_format = utils.get_file_format(input_file)
            if source_format:
                self.source_format_var.set(source_format.upper())

                # Update target format options
                convertible_formats = utils.get_convertible_formats(source_format)
                self.target_format_combo['values'] = [fmt.upper() for fmt in convertible_formats]

                if convertible_formats:
                    self.target_format_var.set(convertible_formats[0].upper())
                    self.convert_button['state'] = 'normal'
                else:
                    self.convert_button['state'] = 'disabled'

                # Validate file
                is_valid, message = utils.validate_file(input_file)
                if not is_valid:
                    self.log_message(f"Warning: {message}")
            else:
                self.source_format_var.set("Unknown format")
                self.target_format_combo['values'] = []
                self.convert_button['state'] = 'disabled'
        else:
            self.source_format_var.set("")
            self.target_format_combo['values'] = []
            self.convert_button['state'] = 'disabled'

    def convert_file(self):
        """Convert the selected file"""
        input_file = self.input_file_var.get()
        target_format = self.target_format_var.get().lower()
        output_dir = self.output_dir_var.get()

        if not input_file or not os.path.exists(input_file):
            messagebox.showerror("Error", "Please select a valid input file")
            return

        if not target_format:
            messagebox.showerror("Error", "Please select a target format")
            return

        # Validate input file
        is_valid, message = utils.validate_file(input_file)
        if not is_valid:
            messagebox.showerror("Error", f"Invalid input file: {message}")
            return

        # Create output directory
        try:
            utils.create_output_directory(output_dir)
        except Exception as e:
            messagebox.showerror("Error", f"Could not create output directory: {str(e)}")
            return

        # Generate output filename
        output_file = utils.generate_output_filename(input_file, target_format, output_dir)

        # Start conversion in a separate thread
        self.start_conversion_thread(input_file, output_file, target_format)

    def start_conversion_thread(self, input_file, output_file, target_format):
        """Start conversion in a separate thread to prevent GUI freezing"""
        self.convert_button['state'] = 'disabled'
        self.progress_bar.start()
        self.status_var.set("Converting...")

        def conversion_worker():
            try:
                source_format = utils.get_file_format(input_file)

                self.log_message(f"Starting conversion: {source_format.upper()} → {target_format.upper()}")
                self.log_message(f"Input: {input_file}")
                self.log_message(f"Output: {output_file}")

                success = self.converter.convert(input_file, output_file, source_format, target_format)

                # Update GUI in main thread
                self.root.after(0, self.conversion_complete, success, output_file)

            except Exception as e:
                self.root.after(0, self.conversion_error, str(e))

        thread = threading.Thread(target=conversion_worker)
        thread.daemon = True
        thread.start()

    def conversion_complete(self, success, output_file):
        """Handle conversion completion"""
        self.progress_bar.stop()
        self.convert_button['state'] = 'normal'

        if success:
            self.status_var.set("Conversion completed successfully!")
            self.log_message(f"✓ Conversion completed: {output_file}")

            # Ask if user wants to open the output file
            if messagebox.askyesno("Success",
                                 f"Conversion completed successfully!\n\nOutput: {output_file}\n\nWould you like to open the output file?"):
                try:
                    os.startfile(output_file)  # Windows
                except:
                    try:
                        os.system(f'open "{output_file}"')  # macOS
                    except:
                        os.system(f'xdg-open "{output_file}"')  # Linux
        else:
            self.status_var.set("Conversion failed!")
            self.log_message("✗ Conversion failed. Check the log for details.")
            messagebox.showerror("Error", "Conversion failed. Please check the log for details.")

    def conversion_error(self, error_message):
        """Handle conversion error"""
        self.progress_bar.stop()
        self.convert_button['state'] = 'normal'
        self.status_var.set("Conversion failed!")
        self.log_message(f"✗ Error: {error_message}")
        messagebox.showerror("Error", f"Conversion failed: {error_message}")

    def log_message(self, message):
        """Add message to log area"""
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()

    def set_target_format(self, format_code):
        """Set target format from sidebar button"""
        self.target_format_var.set(format_code.upper())
        self.log_message(f"Target format set to: {format_code.upper()}")

    def quick_docx_to_pdf(self):
        """Quick conversion: DOCX to PDF"""
        self.set_target_format('pdf')
        self.log_message("Quick conversion: DOCX → PDF selected")
        if self.input_file_var.get():
            self.convert_file()

    def quick_pdf_to_txt(self):
        """Quick conversion: PDF to TXT"""
        self.set_target_format('txt')
        self.log_message("Quick conversion: PDF → TXT selected")
        if self.input_file_var.get():
            self.convert_file()

    def quick_png_to_jpg(self):
        """Quick conversion: PNG to JPG"""
        self.set_target_format('jpg')
        self.log_message("Quick conversion: PNG → JPG selected")
        if self.input_file_var.get():
            self.convert_file()

    def quick_jpg_to_png(self):
        """Quick conversion: JPG to PNG"""
        self.set_target_format('png')
        self.log_message("Quick conversion: JPG → PNG selected")
        if self.input_file_var.get():
            self.convert_file()

    def quick_images_to_pdf(self):
        """Quick conversion: Images to PDF"""
        self.set_target_format('pdf')
        self.log_message("Quick conversion: Images → PDF selected")
        if self.input_file_var.get():
            self.convert_file()

def main():
    """Main function to run the GUI application"""
    app = FileConverterGUI(None)
    app.root.mainloop()

if __name__ == "__main__":
    main()
