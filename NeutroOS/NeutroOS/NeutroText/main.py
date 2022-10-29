from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

root = Tk()

p1 = PhotoImage(file = 'NeutroTexticon.png')

root.title('NeutroText')
root.iconphoto(False, p1)
root.geometry("1200x700")


global open_status_name
open_status_name = False

global selected
selected = False

# New file
def new_file():
    my_text.delete("1.0", END)
    # Set StatusBar
    root.title('New File - NeutroText')
    status_bar.config(text="New File          ")

    global open_status_name
    open_status_name = False


# Open file
def open_file():
    my_text.delete("1.0", END)
    # Grab filename
    text_file = filedialog.askopenfilename(initialdir="/NeutroOS/NeutroText/saves", title="Open File", filetypes = (("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))

    # Check for Filename
    if text_file:
        # Globalize
        global open_status_name
        open_status_name = text_file
    # Set Status Bars
    name = text_file
    status_bar.config(text=f'{name}          ')
    name = name.replace("/NeutroOS/NeutroText/saves", "")
    root.title(f'{name} - NeutroText')

    # Open the file
    text_file = open(text_file, 'r')
    details = text_file.read()
    # Add file
    my_text.insert(END, details)
    # Close the file
    text_file.close()

# Save As file
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="/NeutroOS/NeutroText/saves", title="Save File", filetypes = (("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        # Set StatusBars
        name = text_file
        status_bar.config(text=f'Saved: {name}          ')
        name = name.replace("/NeutroOS/NeutroText/saves", "")
        root.title(f'{name} - NeutroText')

        # Save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close the file
        text_file.close()


# Save file
def save_file():
    global open_status_name
    if open_status_name:
        # Save the file
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close the file
        text_file.close()

        status_bar.config(text=f'Saved: {open_status_name}          ')
    else:
        save_as_file()


def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            # Get selected text
            selected = my_text.selection_get()
            # Delete text
            my_text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)


def copy_text(e):
    global selected
    # Check keyboard
    if e:
        selected = root.clipboard_get()

    if my_text.selection_get():
        # Get selected text
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)


def paste_text(e):
    global selected

    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)


def bold():
    # Create font
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    # Configure tag
    my_text.tag_configure("bold", font=bold_font)

    # Define current tags
    current_tags = my_text.tag_names("sel.first")

    # check for tag
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")


def italics():
    # Create font
    italic_font = font.Font(my_text, my_text.cget("font"))
    italic_font.configure(slant="italic")

    # Configure tag
    my_text.tag_configure("italic", font=italic_font)

    # Define current tags
    current_tags = my_text.tag_names("sel.first")

    # check for tag
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")


# Change text color
def text_color():

    my_color = colorchooser.askcolor()[1]
    if my_color:
        status_bar.config(text=my_color)

        # Create font
        color_font = font.Font(my_text, my_text.cget("font"))

        # Configure tag
        my_text.tag_configure("colored", font=color_font, foreground=my_color)

        # Define current tags
        current_tags = my_text.tag_names("sel.first")

        # check for tag
        if "colored" in current_tags:
            my_text.tag_remove("colored", "sel.first", "sel.last")
        else:
            my_text.tag_add("colored", "sel.first", "sel.last")


# Change bg color
def bg_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)

# Change all text color
def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color)


# Create toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

# Create main frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create scroll bar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Horizontal bar
hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

# Create text box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="blue", selectforeground="white", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
my_text.pack()

# Configure scrollbar
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# File menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste", command=lambda: paste_text(False), accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="(Ctrl+y)")

# Color menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Selected Text", command=text_color)
color_menu.add_command(label="All Text", command=all_text_color)
color_menu.add_command(label="Background", command=bg_color)


# Status bar
status_bar = Label(root, text='Ready          ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)

# Edit Bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)

# Buttons

# Bold
bold_button = Button(toolbar_frame, text="Bold", command=bold)
bold_button.grid(row=0, column=0, sticky=W, padx=5)
# Italics
italics_button = Button(toolbar_frame, text="Italics", command=italics)
italics_button.grid(row=0, column=1, stick=W, padx=5)
# Undo
undo_button = Button(toolbar_frame, text="Undo", command=my_text.edit_undo)
undo_button.grid(row=0, column=2, padx=5)
# Redo
redo_button = Button(toolbar_frame, text="Redo", command=my_text.edit_redo)
redo_button.grid(row=0, column=3, padx=5)

# Text color
color_text_button = Button(toolbar_frame, text="Text Color", command=text_color)
color_text_button.grid(row=0, column=4, padx=5)


root.mainloop()