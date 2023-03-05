import os
import glob
import shutil
import tkinter as tk
from tkinter import filedialog
 
def move_files(source, destination, search_term):
    # gather all files
    allfiles = glob.glob(os.path.join(source, f'*{search_term}*'), recursive=True)
    print("Files to move:", allfiles)
 
    # iterate on all files to move them to destination folder
    for file_path in allfiles:
        dst_path = os.path.join(destination, os.path.basename(file_path))
        shutil.move(file_path, dst_path)
        print(f"Moved {file_path} -> {dst_path}")
 
def browse_button(entry):
    filename = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, filename)
 
def main():
    # create the main window
    root = tk.Tk()
    root.title("File Mover")
 
    # create the source directory entry
    source_label = tk.Label(root, text="Source Directory:")
    source_label.grid(row=0, column=0)
    source_entry = tk.Entry(root, width=50)
    source_entry.grid(row=0, column=1)
    source_button = tk.Button(root, text="Browse...", command=lambda: browse_button(source_entry))
    source_button.grid(row=0, column=2)
 
    # create the destination directory entry
    dest_label = tk.Label(root, text="Destination Directory:")
    dest_label.grid(row=1, column=0)
    dest_entry = tk.Entry(root, width=50)
    dest_entry.grid(row=1, column=1)
    dest_button = tk.Button(root, text="Browse...", command=lambda: browse_button(dest_entry))
    dest_button.grid(row=1, column=2)
 
    # create the search term entry
    search_label = tk.Label(root, text="Search Term:")
    search_label.grid(row=2, column=0)
    search_entry = tk.Entry(root, width=50)
    search_entry.insert(0, "Suits") # default search term
    search_entry.grid(row=2, column=1)
 
    # create the move button
    move_button = tk.Button(root, text="Move Files", command=lambda: move_files(source_entry.get(), dest_entry.get(), search_entry.get()))
    move_button.grid(row=3, column=1)
 
    # start the main loop
    root.mainloop()
 
if __name__ == "__main__":
    main()
