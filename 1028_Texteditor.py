import tkinter as tk
from tkinter import filedialog, colorchooser, font, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.filename = None
        
        self.current_font_family = "Arial"
        self.current_font_size = 12
        self.text_font = font.Font(family = self.current_font_family, size = self.current_font_size)
        
        self.menu = tk.Menu(self.root)
        self.root.config(menu = self.menu)
        self.file_menu = tk.Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(Label = "File", menu = self.file_menu)
        self.file_menu.add_command(Label = "Open", command = self.open_file)
        self.file_menu.add_command(Label = "Save", command = self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(Label = "Exit", command = self.root.quit)
        
        self.toolbar = tk.Frame(self.root)
        self.toolbar.pack(side = tk.TOP, fill = tk.X)
        
        self.bold_btn = tk.Button(self.toolbar, text = "Bold", command = self.make_bold)
        self.bold_btn.pack(side = tk.LEFT, padx = 2)
        self.italic_btn = tk.Button(self.toolbar, text = "Italic", command = self.make_italic)
        self.italic_btn.pack(side = tk.LEFT, padx = 2)
        self.underline_btn = tk.Button(self.toolbar, text = "Underline", command = self.make_underline)
        self.underline_btn.pack(side = tk.LEFT, padx = 2)
        
        self.increase_font_btn = tk.Button(self.toolbar, text = "A+", command = self.increase_font)
        self.increase_font_btn.pack(side = tk.LEFT, padx = 2)
        self.decrease_font_btn = tk.Button(self.toolbar, text = "A-", command = self.decrease_font)
        self.bold_btn.pack(side = tk.LEFT, padx = 2)
        
        self.color_btn = tk.Button(self.toolbar, text = "Text color", command = self.change_text_color)
        self.color_btn.pack(side = tk.LEFT, padx = 2)
        self.bg_color_btn = tk.Button(self.toolbar, text = "BG color", command = self.change_bg_color)
        self.bg_color_btn.pack(side = tk.LEFT, padx = 2)
        
        self.text_area = tk.Text(self.root, wrap = "word", font = self.text_font, undo = True)
        self.text_area.pack(expand = 1, fill = tk.BOTH)
        self.text_area.tag_configure("bold", font = (self.current_font_family, self.current_font_size, "bold"))
        self.text_area.tag_configure("italic", font = (self.current_font_family, self.current_font_size, "italic"))
        self.text_area.tag_configure("underline", font = (self.current_font_family, self.current_font_size, "underline"))
        
    def open_file(self):
        file = filedialog.askopenfilename(defaultextension = ".txt",
                                          filetypes = [("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file:
            self.filename = file
            with open(file, "r", encoding = "utf-8") as f:
                f.write(self.text_area.get(1.0, tk.END))
                
    def save_file(self):
        if not self.filename:
            file = filedialog.asksaveasfilename(defaultextension = ".txt",
                                                filetypes = [("Text Documents", "*.txt"), ("All Files", "*.*")])
            
            if not file:
                return
            self.filename = file
        with open(self.filename, "w", encomding = "utf-8") as f:
            f.write(self.text_area.get(1.0, tk.END))
            
    def make_bold(self):
        self.toggle_tag("bold")
   
    def make_italic(self):
        self.toggle_tag("italic")
   
    def make_underline(self):
        self.toggle_tag("underline")
        
    def toggle_tag(self, tag):
        try:
            start, end = self.text_area.index("sel.first"), self.text_area.index("sel.last")
            if tag in self.text_area.tag_names("sel.first"):
                self.text_area.tag_remove(tag, start, end)
            else:
                self.text_area.tag_add(tag, start, end)
        except tk.TclError:
            pass
        
    def increase_font(self):
        self.current_font_size += 2
        self.update_font()
        
    def decrease_font(self):
       if self.current_font_size > 6:
           self.current_font_size -= 2
           self.update_font
           
    def update_font(self):
        self.text_font.configure(size = self.current_font_size)
        self.text_area.configure(font = self.text_font)
        self.text_area.tag_configure("bold", font = (self.current_font_family, self.current_font_size, "bold"))
        self.text_area.tag_configure("italic", font = (self.current_font_family, self.current_font_size, "italic"))
        self.text_area.tag_configure("underline", font = (self.current_font_family, self.current_font_size, "underline"))
        
    def change_text_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            try:
                start, end = self.text_area.index("sel.first"), self.text_area.index("sel.last")
                self.text_area.tag_add("color", start, end)
                self.text_area.tag_configure("color", foreground = color)
            except tk.TclError:
                pass
            
    def change_bg_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.configure(bg = color)
            
if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()