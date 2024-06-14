import customtkinter as ctk
from utils.ctk_utils import create_frame, create_label, create_image

class CustomerFrame(ctk.CTkFrame):
  def __init__(self, parent, go_back):
    super().__init__(parent)
    self.go_back = go_back
    
    self.create_widgets()

    
  def create_widgets(self):
    # Label
    text_label = create_label(parent=self, text="This is the Customer Frame")
    text_label.pack()

    # Button to go back to main window
    back_button = ctk.CTkButton(self, text="Back", command=self.go_back)
    back_button.pack(pady=10)