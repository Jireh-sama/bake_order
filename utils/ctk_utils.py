import customtkinter as ctk
from PIL import Image, ImageTk
def create_label(parent, text):
  label = ctk.CTkLabel(parent, text=text)
  return label
  
def create_frame(parent, bg_color=None, width=None, height=None, b_radius=0):
  frame = ctk.CTkFrame(parent, corner_radius=b_radius)
  if bg_color is not None:
    frame.configure(fg_color=bg_color)
  if width is not None and height is not None:
    frame.configure(width=width, height=height)
  return frame
  
def create_image(parent, path, width, height):
    original_image = Image.open(path)
    new_size = (width, height)  # Specify the desired size (width, height)
    resized_image = original_image.resize(new_size)
    photo = ImageTk.PhotoImage(resized_image)
    image_label = ctk.CTkLabel(parent, image=photo, text="")
    image_label.image = photo
    return image_label


def create_button(parent, text, command, width, height, bg_color, color=None, b_raduis=0):
  btn = ctk.CTkButton(parent, text=text, command=command, width=width, height=height, fg_color=bg_color, corner_radius=b_raduis)
  if color is not None:
    btn.configure(text_color=color)
  return btn