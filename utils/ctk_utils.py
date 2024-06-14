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
  # Load the image
  bake_order_logo_path = "./assets//media//bake-order-logo.png"
  original_image = Image.open(path)

  # Resize the image
  new_size = (width, height)  # Specify the desired size (width, height)
  resized_image = original_image.resize(new_size)

  # Convert resized image to PhotoImage
  photo = ImageTk.PhotoImage(resized_image)

  # Create a label to display the image
  image_label = ctk.CTkLabel(parent, image=photo)
  return image_label