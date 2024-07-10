from convertor import *
import tkinter as tk
from tkinter import Button, Label, filedialog, Entry
from PIL import Image, ImageTk



png_to_gcode = PngToGcode()

def resize_image(image_path, size_mm=(100, 100)):
    image = Image.open(image_path)
    dpi = 300
    size_in_pixels = (int(size_mm[0] / 25.4 * dpi), int(size_mm[1] / 25.4 * dpi))
    resized_image = image.resize(size_in_pixels, Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)


def load_image(img):
    file_path = filedialog.askopenfilename(defaultextension=".png",
    filetypes=[("Image files", "*.png")])
    if file_path:
        photo = resize_image(file_path, size_mm=(20, 20))
        label.config(image=photo)
        label.photo = photo
        png_to_gcode.input = file_path


def save_gcode():
    file_path = filedialog.asksaveasfilename()
    png_to_gcode.output = file_path
    png_to_gcode.gen_all()

def save_settings():
    try:
        png_to_gcode.gcode_height = float(height_entry.get())
        png_to_gcode.gcode_width = float(width_entry.get())
        png_to_gcode.pen_up = pen_up_entry.get()
        png_to_gcode.pen_down = pen_down_entry.get()
        button_gcode.config(state="normal")
    except ValueError:
        print("Invalid input. Please enter valid numbers for height and width.")


# Create the main window
root = tk.Tk()
root.title("PNG → G-code")


# Create buttons
button_load = Button(root, text="Load Image", command= lambda: load_image(label))
button_load.grid(row=0, column=0, pady=5, padx=5)

button_gcode = Button(root, text="Save G-code", command= lambda: save_gcode())
button_gcode.grid(row=0, column=1, pady=5, padx=5)
button_gcode.config(state="disabled")

height_label = Label(root, text="Height (mm):")
height_label.grid(row=1, column=0, padx=5)
height_entry = Entry(root, width=10)
height_entry.grid(row=1, column=1, padx=5)

width_label = Label(root, text="Width (mm):")
width_label.grid(row=2, column=0, padx=5)
width_entry = Entry(root, width=10)
width_entry.grid(row=2, column=1, padx=5)

pen_up_label = Label(root, text="Pen Up command:")
pen_up_label.grid(row=3, column=0, padx=5)
pen_up_entry = Entry(root, width=10)
pen_up_entry.grid(row=3, column=1, padx=5)

pen_down_label = Label(root, text="Pen Down command:")
pen_down_label.grid(row=4, column=0, padx=5)
pen_down_entry = Entry(root, width=10)
pen_down_entry.grid(row=4, column=1, padx=5)


button_save = Button(root, text="Save", command= lambda: save_settings())
button_save.grid(row=5, column=0, padx=5, pady=5, columnspan=2)



label = Label(root)
label.grid(row=0, column=3, rowspan=6, pady=5, padx=5)
image_path = 'placeholder.png'
photo = resize_image(image_path, size_mm=(20, 20))
label.config(image=photo)
label.photo = photo


root.mainloop()