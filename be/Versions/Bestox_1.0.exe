import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog, colorchooser
import json
import os
import logging
from datetime import datetime
import getpass

# Define the logs directory path
logs_dir = r"C:\Users\ajast\Downloads\be\Logs"

# Ensure the Logs folder exists
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Get the current user's name
username = getpass.getuser()

# Ensure the user's log directory exists
user_log_dir = os.path.join(logs_dir, username)
if not os.path.exists(user_log_dir):
    os.makedirs(user_log_dir)

# Get the current date and time for the log file name
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = os.path.join(user_log_dir, f"bestox_{current_time}.log")

# Set up logging to the user's log directory with the date and time in the file name
logging.basicConfig(filename=log_filename, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class BestoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bestox Menu")
        self.root.geometry("800x600")

        # Initialize settings and theme colors
        self.settings_file = "bestox_settings.json"
        self.load_settings()

        self.theme_colors = {
            "System Default": {"bg": "#f0f0f0", "fg": "#000000", "button_bg": "#e0e0e0", "button_fg": "#000000"},
            "Light": {"bg": "#ffffff", "fg": "#000000", "button_bg": "#e0e0e0", "button_fg": "#000000"},
            "Dark": {"bg": "#333333", "fg": "#ffffff", "button_bg": "#444444", "button_fg": "#ffffff"}
        }

        self.create_sidebar()
        self.create_main_content()

    def apply_theme(self):
        theme = self.settings.get("theme", "System Default")
        colors = self.theme_colors.get(theme, self.theme_colors["System Default"])
        self.root.configure(bg=colors["bg"])
        self.sidebar.configure(bg=colors["bg"])
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.configure(bg=colors["bg"])
        self.update_widgets_colors(colors)

    def update_widgets_colors(self, colors):
        for widget in self.sidebar.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg=colors["button_bg"], fg=colors["button_fg"])
        for widget in self.main_content.winfo_children():
            widget.configure(bg=colors["bg"], fg=colors["fg"])
            if isinstance(widget, tk.Button):
                widget.configure(bg=colors["button_bg"], fg=colors["button_fg"])
            elif isinstance(widget, tk.Label):
                widget.configure(bg=colors["bg"], fg=colors["fg"])

    def create_sidebar(self):
        self.sidebar = tk.Frame(self.root, width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        buttons = [
            ("Integrations", self.show_integrations),
            ("Mods", self.show_mods),
            ("FastFlags", self.show_fastflags),
            ("Appearance", self.show_appearance),
            ("Behavior", self.show_behavior),
            ("Installation", self.show_installation),
            ("About", self.show_about)
        ]

        for text, command in buttons:
            b = tk.Button(self.sidebar, text=text, relief=tk.FLAT, command=command)
            b.pack(fill=tk.X, pady=2, padx=10)

    def create_main_content(self):
        self.main_content = tk.Frame(self.root)
        self.main_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.show_integrations()  # Default tab

    def load_settings(self):
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, "r") as file:
                    self.settings = json.load(file)
                logging.info("Settings loaded successfully.")
            except json.JSONDecodeError:
                self.settings = {}
                logging.warning("Error decoding JSON from settings file. Using default settings.")
        else:
            self.settings = {}
            logging.info("No settings file found. Using default settings.")

    def save_settings(self):
        try:
            self.settings.update({
                "theme": self.selected_theme.get(),
                "custom_bg_color": self.custom_bg_color.get(),
                "install_path": self.install_path.get()
            })
            with open(self.settings_file, "w") as file:
                json.dump(self.settings, file, indent=4)
            logging.info("Settings saved successfully.")
            messagebox.showinfo("Success", "Settings have been saved successfully!")
        except Exception as e:
            logging.error(f"Failed to save settings: {e}")
            messagebox.showerror("Error", f"Failed to save settings: {e}")

    def cancel_settings(self):
        self.load_settings()
        self.apply_theme()
        self.show_integrations()
        logging.info("Changes canceled, settings reverted to the last saved state.")

    def choose_color(self, variable):
        color = colorchooser.askcolor()[1]
        if color:
            variable.set(color)
            self.apply_theme()
            logging.info(f"Color selected: {color}")

    def clear_main_content(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

    def create_title(self, text):
        title_label = tk.Label(self.main_content, text=text, font=("Arial", 18))
        title_label.pack(pady=10)

    def create_subtitle(self, text):
        subtitle_label = tk.Label(self.main_content, text=text, font=("Arial", 10))
        subtitle_label.pack(pady=5)

    def create_section(self, text):
        section_frame = tk.Frame(self.main_content)
        section_frame.pack(fill=tk.X, padx=20, pady=10)
        section_label = tk.Label(section_frame, text=text, font=("Arial", 12, "bold"))
        section_label.pack(anchor='w')
        return section_frame

    def create_toggle(self, parent, text, variable):
        toggle = ttk.Checkbutton(parent, text=text, variable=variable)
        toggle.pack(anchor='w', padx=40)

    def create_dropdown(self, parent, text, options, variable):
        frame = tk.Frame(parent)
        frame.pack(anchor='w', padx=40)
        label = tk.Label(frame, text=text)
        label.pack(side=tk.LEFT)
        dropdown = ttk.Combobox(frame, textvariable=variable, values=options, state="readonly")
        dropdown.pack(side=tk.LEFT)

    def create_entry(self, parent, text, variable):
        frame = tk.Frame(parent)
        frame.pack(anchor='w', padx=40)
        label = tk.Label(frame, text=text)
        label.pack(side=tk.LEFT)
        entry = tk.Entry(frame, textvariable=variable)
        entry.pack(side=tk.LEFT)

    def create_color_picker(self, parent, text, variable):
        frame = tk.Frame(parent)
        frame.pack(anchor='w', padx=40)
        label = tk.Label(frame, text=text)
        label.pack(side=tk.LEFT)
        color_button = tk.Button(frame, text="Pick Color", command=lambda: self.choose_color(variable))
        color_button.pack(side=tk.LEFT)

    def create_save_cancel_buttons(self):
        button_frame = tk.Frame(self.main_content)
        button_frame.pack(side=tk.BOTTOM, pady=20)

        save_button = tk.Button(button_frame, text="Save", command=self.save_settings)
        save_button.pack(side=tk.RIGHT, padx=10)

        cancel_button = tk.Button(button_frame, text="Cancel", command=self.cancel_settings)
        cancel_button.pack(side=tk.RIGHT, padx=10)

    def show_integrations(self):
        self.clear_main_content()
        self.create_title("Integrations")
        self.create_subtitle("Manage third-party integrations.")

        self.create_section("Discord Integration")
        self.discord_integration = tk.BooleanVar(value=self.settings.get("discord_integration", False))
        self.create_toggle(self.main_content, "Enable Discord Integration", self.discord_integration)

        self.create_save_cancel_buttons()

    def show_mods(self):
        self.clear_main_content()
        self.create_title("Mods")
        self.create_subtitle("Select and manage your Roblox mods.")

        mod_options = ["Mod1", "Mod2", "Mod3"]
        self.selected_mods = tk.StringVar(value=self.settings.get("selected_mods", mod_options[0]))
        mod_frame = self.create_section("Choose Mod")
        self.create_dropdown(mod_frame, "Choose Mod", mod_options, self.selected_mods)

        self.create_save_cancel_buttons()

    def show_fastflags(self):
        self.clear_main_content()
        self.create_title("FastFlags Editor")
        self.create_subtitle("Manage your FastFlags.")

        self.fastflags_enable = tk.BooleanVar(value=self.settings.get("fastflags_enable", False))
        self.fastflags_list = self.settings.get("fastflags_list", [])

        fastflags_frame = self.create_section("FastFlags List")
        self.fastflags_listbox = tk.Listbox(fastflags_frame, selectmode=tk.SINGLE)
        for flag in self.fastflags_list:
            self.fastflags_listbox.insert(tk.END, flag)
        self.fastflags_listbox.pack(anchor='w', padx=40, pady=10)

        self.create_save_cancel_buttons()

    def show_appearance(self):
        self.clear_main_content()
        self.create_title("Appearance")
        self.create_subtitle("Customize the appearance of Bestox.")

        theme_options = ["System Default", "Light", "Dark"]
        self.selected_theme = tk.StringVar(value=self.settings.get("theme", "System Default"))
        theme_frame = self.create_section("Theme")
        self.create_dropdown(theme_frame, "Select Theme", theme_options, self.selected_theme)

        self.custom_bg_color = tk.StringVar(value=self.settings.get("custom_bg_color", "#ffffff"))
        color_frame = self.create_section("Custom Background Color")
        self.create_color_picker(color_frame, "Background Color", self.custom_bg_color)

        self.create_save_cancel_buttons()

    def show_behavior(self):
        self.clear_main_content()
        self.create_title("Behavior")
        self.create_subtitle("Customize the behavior of Bestox.")

        behavior_frame = self.create_section("Startup Behavior")
        self.startup_behavior = tk.StringVar(value=self.settings.get("startup_behavior", "None"))
        self.create_dropdown(behavior_frame, "Select Startup Behavior", ["None", "Open Last Project", "Start New Project"], self.startup_behavior)

        self.create_save_cancel_buttons()

    def show_installation(self):
        self.clear_main_content()
        self.create_title("Installation")
        self.create_subtitle("Manage your installation settings.")

        self.install_path = tk.StringVar(value=self.settings.get("install_path", ""))
        install_frame = self.create_section("Installation Path")
        self.create_entry(install_frame, "Installation Path", self.install_path)

        self.create_save_cancel_buttons()

    def show_about(self):
        self.clear_main_content()
        self.create_title("About Bestox")
        self.create_subtitle("Learn more about Bestox.")

        about_text = tk.Label(self.main_content, text="Bestox is a customizable application that allows you to manage Roblox mods and integrations.", wraplength=500)
        about_text.pack(pady=20)

        self.create_save_cancel_buttons()

if __name__ == "__main__":
    root = tk.Tk()
    app = BestoxApp(root)
    root.mainloop()
