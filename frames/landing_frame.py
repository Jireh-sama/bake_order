import customtkinter as ctk
from utils.ctk_utils import create_frame, create_label, create_image

class LandingFrame(ctk.CTkFrame):
  def __init__(self, parent, open_buy, open_view_receipt):
    super().__init__(parent)

    self.open_buy = open_buy
    self.open_view_receipt = open_view_receipt

    self.create_widgets()

  def create_widgets(self):
    self.cover_frame = create_frame(parent=self, width=600, height=650, bg_color="#F8EDE3")
    self.cover_frame.pack(side="left", fill="both", expand=True)

    self.login_frame = create_frame(parent=self, width=400, height=650, bg_color="#E49748")
    self.login_frame.pack(side="left", fill="both", expand=True)

    self.header_label = create_label(self.login_frame, "Shop Now")
    self.header_label.configure(font=("Arial", 34))
    self.header_label.pack(pady=(25, 0))

    self.customer_btn = ctk.CTkButton(self.login_frame, text="Buy", command=self.open_buy, width=241, height=50, fg_color="#6C3A30", corner_radius=20)
    self.customer_btn.pack(pady=(195, 0))

    self.owner_btn = ctk.CTkButton(self.login_frame, text="View Receipt", command=self.open_view_receipt, width=241, height=50, fg_color="#6C3A30", corner_radius=20)
    self.owner_btn.pack(pady=(25, 0))

    self.image_label = create_image(self.cover_frame, path="./assets//media//bake-order-logo.png", width=280, height=200)
    self.image_label.pack(expand=True)
