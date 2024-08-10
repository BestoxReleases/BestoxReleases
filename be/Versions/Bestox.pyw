import tkinter as tk
from tkinter import ttk, messagebox

class BestoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bestox Launcher")
        self.root.geometry("800x600")
        
        self.setup_styles()
        
        self.current_theme = tk.StringVar(value="System Default")
        self.themes = {
            "System Default": {"bg": root.cget("bg"), "fg": "black"},
            "Light": {"bg": "white", "fg": "black"},
            "Dark": {"bg": "black", "fg": "white"}
        }

        self.create_sidebar()
        self.show_home()

    def setup_styles(self):
        # Set up common styles for the application
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#ccc")
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))

    def create_sidebar(self):
        sidebar = tk.Frame(self.root, width=200, bg="#333")
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        buttons = [
            ("Home", self.show_home),
            ("Appearance", self.show_appearance),
            ("Mods", self.show_mods),
            ("FastFlags", self.show_fastflags)
        ]

        for text, command in buttons:
            button = tk.Button(sidebar, text=text, command=command, relief=tk.FLAT, bg="#444", fg="#fff", font=("Arial", 10))
            button.pack(fill=tk.X, pady=2, padx=10)

    def apply_theme(self):
        theme = self.themes[self.current_theme.get()]
        self.main_content.config(bg=theme["bg"])

        for widget in self.main_content.winfo_children():
            widget.config(bg=theme["bg"], fg=theme["fg"])

    def show_home(self):
        self.clear_main_content()
        self.create_title("Welcome to Bestox")
        self.apply_theme()

    def show_appearance(self):
        self.clear_main_content()
        self.create_title("Appearance Settings")

        theme_label = tk.Label(self.main_content, text="Select Theme:", font=("Arial", 14))
        theme_label.pack(anchor="w", padx=20, pady=10)

        theme_dropdown = ttk.OptionMenu(self.main_content, self.current_theme, *self.themes.keys())
        theme_dropdown.pack(anchor="w", padx=20)

        apply_button = ttk.Button(self.main_content, text="Apply Theme", command=self.apply_theme)
        apply_button.pack(anchor="e", padx=20, pady=20)

        self.apply_theme()

    def show_mods(self):
        self.clear_main_content()
        self.create_title("Mods Section")
        # You can add more features here
        self.apply_theme()

    def show_fastflags(self):
        self.clear_main_content()
        self.create_title("FastFlags Section")
        # You can add more features here
        self.apply_theme()

    def create_title(self, title):
        title_label = tk.Label(self.main_content, text=title, font=("Arial", 18, "bold"))
        title_label.pack(anchor="w", padx=20, pady=10)

    def clear_main_content(self):
        if hasattr(self, 'main_content'):
            self.main_content.destroy()
        self.main_content = tk.Frame(self.root)
        self.main_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = BestoxApp(root)
    root.mainloop()
