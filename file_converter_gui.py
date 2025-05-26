"""
GUI Application for Universal File Converter
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
from pathlib import Path
import config
import utils
from converter_core import DocumentConverter

class FileConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(config.APP_NAME)
        self.root.geometry(config.WINDOW_SIZE)
        self.root.minsize(*config.WINDOW_MIN_SIZE)

        self.converter = DocumentConverter()
        self.setup_logging()
        self.create_widgets()

    def setup_logging(self):
        """Setup logging for the application"""
        utils.setup_logging()

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
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Input file selection
        ttk.Label(main_frame, text="Input File:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.input_file_var = tk.StringVar()
        self.input_entry = ttk.Entry(main_frame, textvariable=self.input_file_var, width=50)
        self.input_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(5, 5), pady=5)
        ttk.Button(main_frame, text="Browse",
                  command=self.browse_input_file).grid(row=1, column=2, pady=5)

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
                                        command=self.convert_file, style="Accent.TButton")
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
        """Create sidebar with conversion categories"""
        # Sidebar frame with background
        sidebar = ttk.Frame(parent, padding="10", relief="raised", borderwidth=1)
        sidebar.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        sidebar.configure(style="Sidebar.TFrame")

        # Sidebar title
        sidebar_title = ttk.Label(sidebar, text="Conversion Categories",
                                 font=('Arial', 12, 'bold'))
        sidebar_title.grid(row=0, column=0, sticky=tk.W, pady=(0, 15))

        # Category sections
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

        # Quick conversion buttons
        ttk.Separator(sidebar, orient='horizontal').grid(row=4, column=0, sticky=(tk.W, tk.E), pady=15)

        quick_title = ttk.Label(sidebar, text="Quick Conversions",
                               font=('Arial', 11, 'bold'))
        quick_title.grid(row=5, column=0, sticky=tk.W, pady=(0, 10))

        # Popular conversion buttons
        quick_conversions = [
            ("DOCX → PDF", self.quick_docx_to_pdf),
            ("PDF → TXT", self.quick_pdf_to_txt),
            ("PNG → JPG", self.quick_png_to_jpg),
            ("JPG → PNG", self.quick_jpg_to_png),
            ("Images → PDF", self.quick_images_to_pdf)
        ]

        for i, (text, command) in enumerate(quick_conversions):
            btn = ttk.Button(sidebar, text=text, command=command, width=15)
            btn.grid(row=6+i, column=0, sticky=(tk.W, tk.E), pady=2)

        # Tips section
        ttk.Separator(sidebar, orient='horizontal').grid(row=12, column=0, sticky=(tk.W, tk.E), pady=15)

        tips_title = ttk.Label(sidebar, text="💡 Tips",
                              font=('Arial', 11, 'bold'))
        tips_title.grid(row=13, column=0, sticky=tk.W, pady=(0, 5))

        tips_text = tk.Text(sidebar, height=6, width=25, wrap=tk.WORD,
                           font=('Arial', 9), bg='#f0f0f0', relief='flat')
        tips_text.grid(row=14, column=0, sticky=(tk.W, tk.E), pady=5)

        tips_content = """• Drag & drop files for quick selection
• Use batch mode for multiple files
• PNG preserves transparency
• JPEG is smaller for photos
• PDF is great for documents
• SVG is vector graphics"""

        tips_text.insert('1.0', tips_content)
        tips_text.config(state='disabled')

    def create_category_section(self, parent, title, formats, row):
        """Create a category section in the sidebar"""
        # Category title
        category_label = ttk.Label(parent, text=title, font=('Arial', 10, 'bold'))
        category_label.grid(row=row, column=0, sticky=tk.W, pady=(10, 5))

        # Format list
        formats_frame = ttk.Frame(parent)
        formats_frame.grid(row=row, column=0, sticky=(tk.W, tk.E), padx=(15, 0), pady=(25, 0))

        for i, (format_code, format_name) in enumerate(formats):
            format_btn = ttk.Button(formats_frame, text=f"{format_code}",
                                   command=lambda f=format_code.lower(): self.set_target_format(f),
                                   width=8)
            format_btn.grid(row=i//2, column=i%2, sticky=tk.W, padx=2, pady=1)

            # Tooltip-like label
            if i % 2 == 1 or i == len(formats) - 1:
                ttk.Label(formats_frame, text="", font=('Arial', 1)).grid(row=i//2, column=2)

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
    root = tk.Tk()
    app = FileConverterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
