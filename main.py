import os
from tkinter import Tk, filedialog, Entry, Button, Label, StringVar

def select_directory():
    folder_selected = filedialog.askdirectory()
    path_var.set(folder_selected)

def create_file():
    directory = path_var.get()
    label.config(text="")
    if directory:
        # desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        output_file = os.path.join(directory, 'requirements.txt')
        with open(output_file, 'w') as file:
            for item in os.listdir(directory):
                if os.path.isdir(os.path.join(directory, item)):
                    file.write(item + '\n')
        label.config(text="File created successfully")
    else:
        label.config(text="Select a directory")

def open_file():
    directory = path_var.get()
    output_file = os.path.join(directory, 'requirements.txt')
    if directory:
        if not os.path.exists(output_file):
            label.config(text="File not found")
        else:
            os.startfile(output_file)
    else:
        label.config(text="Select a directory")

app = Tk()
app.title("Path requirements")

path_var = StringVar()

entry = Entry(app, textvariable=path_var, width=50)
entry.grid(row=0, column=0, padx=10, pady=20)

btn_select = Button(app, text="Open", command=select_directory, width=8)
btn_select.grid(row=0, column=1, padx=10, pady=20)

btn_create = Button(app, text="Create", command=create_file, width=62)
btn_create.grid(row=1, column=0, columnspan=2, pady=10)

btn_create = Button(app, text="Open File", command=open_file, width=62)
btn_create.grid(row=2, column=0, columnspan=2, pady=10)

label = Label(app, text="")
label.grid(row=3, column=0, columnspan=2, pady=10)

app.geometry("400x200")
app.resizable(False, False)
app.mainloop()
