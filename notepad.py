import tkinter as tk
from tkinter import Text, filedialog, messagebox

root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")

current_bg_color = "white"
current_fg_color = "black"

def new_file():
    text_area.delete(1.0, tk.END)
    root.title("New File - Notepad")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(1.0, file.read())
        root.title(f"{file_path} - Notepad")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"{file_path} - Notepad")

def save_file_as():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"{file_path} - Notepad")

def exit_app():
    if messagebox.askokcancel("Quit", "Are you sure?"):
        root.destroy()

def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def undo_action():
    try:
        text_area.edit_undo()
    except:
        pass

def redo_action():
    try:
        text_area.edit_redo()
    except:
        pass

def apply_light_theme():
    global current_bg_color, current_fg_color
    current_bg_color = "white"
    current_fg_color = "black"
    text_area.config(bg=current_bg_color, fg=current_fg_color)

def apply_dark_theme():
    global current_bg_color, current_fg_color
    current_bg_color = "#2b2b2b"
    current_fg_color = "white"
    text_area.config(bg=current_bg_color, fg=current_fg_color)

def show_about():
    messagebox.showinfo("About Simple Notepad", "Simple Notepad Version 1.0\nCreated using Python and Tkinter")

def show_help():
    messagebox.showinfo("Help", "This is a simple notepad application.\n\n- Use File menu to create, open, save files.\n- Use Edit menu to cut, copy, paste text.\n- Use Themes menu to switch between different color themes.")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=undo_action)
edit_menu.add_command(label="Redo", command=redo_action)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

theme_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Themes", menu=theme_menu)
theme_menu.add_command(label="Light Theme", command=apply_light_theme)
theme_menu.add_command(label="Dark Theme", command=apply_dark_theme)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Help", command=show_help)
help_menu.add_command(label="About", command=show_about)

text_area = Text(root, wrap="word", font=("Times", 12))
text_area.pack(expand=True, fill="both")

root.mainloop()
