import os
import time
import csv
import google.generativeai as genai
from PyPDF2 import PdfReader
from datetime import datetime
import itertools
import threading
import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox

PDF_FOLDER_PATH = r'/Users/muhammadsarim/Desktop/NeurIPS_Papers-Python/pdfs'
LABELS = [
    "Machine Learning",
    "Deep Learning",
    "Computer Vision",
    "Natural Language Processing",
    "Reinforcement Learning",
    "Generative AI",
    "Algorithms",
    "Explainable AI"
]
GENERIC_LABELS_PROMPT = ", ".join(LABELS)
GEMINI_API_KEYS = [
    os.getenv("API_KEY1="),
    os.getenv("API_KEY2"),
    os.getenv("API_KEY3")
]
MODEL_NAME = "gemini-1.5-flash"
CSV_OUTPUT_FILE = r'/Users/muhammadsarim/Desktop/NeurIPS_Papers-Python/dataset.csv'
API_TIMEOUT_SECONDS = 90

# Filter out any None keys
GEMINI_API_KEYS = [key for key in GEMINI_API_KEYS if key is not None]
if not GEMINI_API_KEYS:
    print("Error: No Gemini API keys found. Please set up at least one API key.")

api_key_cycle = itertools.cycle(GEMINI_API_KEYS)
pdf_categories_global = {}
csv_header_written = False

class PDFCategorizerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Annotator")
        self.geometry("1000x600")
        self.configure(bg="#1C1C1C")
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TLabel", background="#1C1C1C", foreground="white", font=("Arial", 12))
        self.style.configure("TButton", background="#2ECC71", foreground="black", font=("Arial", 12, "bold"), padding=5)
        self.style.configure("TEntry", fieldbackground="#F0F0F0", font=("Arial", 12))
        self.style.configure("Treeview", background="#2C3E50", foreground="white", rowheight=25, font=("Arial", 11))
        self.style.configure("Treeview.Heading", background="#34495E", foreground="white", font=("Arial", 12, "bold"))
        self.style.configure("TFrame", background="#1C1C1C")
        
        self.pdf_folder = tk.StringVar(value=PDF_FOLDER_PATH)
        self.create_widgets()
    
    def create_widgets(self):
        top_frame = ttk.Frame(self, padding=10)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(top_frame, text="PDF Folder:").pack(side=tk.LEFT, padx=5)
        self.folder_entry = ttk.Entry(top_frame, textvariable=self.pdf_folder, width=60)
        self.folder_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(top_frame, text="Browse", command=self.browse_folder).pack(side=tk.LEFT, padx=5)
        ttk.Button(top_frame, text="Start", command=self.start_categorization).pack(side=tk.LEFT, padx=5)
        
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self, variable=self.progress_var, maximum=100, mode='determinate')
        self.progress_bar.pack(fill=tk.X, padx=10, pady=5)

        tree_frame = ttk.Frame(self)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        columns = ("PDF Name", "Category")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=450)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        log_frame = ttk.LabelFrame(self, text="Log", padding=10)
        log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.log_area = scrolledtext.ScrolledText(log_frame, height=10, wrap=tk.WORD, font=("Arial", 11))
        self.log_area.pack(fill=tk.BOTH, expand=True)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory(initialdir=self.pdf_folder.get())
        if folder_selected:
            self.pdf_folder.set(folder_selected)

    def start_categorization(self):
        folder = self.pdf_folder.get()
        if not os.path.isdir(folder):
            messagebox.showerror("Error", "Invalid PDF folder selected.")
            return
        self.tree.delete(*self.tree.get_children())
        threading.Thread(target=self.process_folder, args=(folder,), daemon=True).start()

    def process_folder(self, folder_path):
        pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]
        total = len(pdf_files)
        for idx, filename in enumerate(pdf_files, start=1):
            pdf_path = os.path.join(folder_path, filename)
            category = "Placeholder Category"  # Replace with actual categorization logic
            self.tree.insert("", tk.END, values=(filename, category))
            self.progress_var.set((idx / total) * 100)

if __name__ == "__main__":
    app = PDFCategorizerGUI()
    app.mainloop()