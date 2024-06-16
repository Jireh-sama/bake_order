import customtkinter as ctk
from frames.landing_frame import LandingFrame
from frames.buy_frame import BuyFrame
from frames.view_receipt_frame import ViewReceiptFrame


class MainApplication(ctk.CTk):
  def __init__(self):
    super().__init__()
    ctk.set_appearance_mode("light")  # Set window theme
    self.title("Bake Order")  # Set window title
    self.geometry("1000x650")  # Set window size
    
    self.create_main_frame()

  def create_main_frame(self):
    """
      When this function is called 
      check if both buy frame or view receipt frame exists
      if so hide it
    """
    if hasattr(self, 'buy_frame'):
        self.buy_frame.pack_forget() 
    if hasattr(self, 'view_receipt_frame'):
        self.view_receipt_frame.pack_forget() 

    # Open the landing frame
    self.main_frame = LandingFrame(self, open_buy=self.open_buy_frame, open_view_receipt=self.open_view_receipt_frame)
    self.main_frame.pack(fill="both", expand=True)

    
  def open_buy_frame(self):
    # Hide main frame and open buy frame
    self.main_frame.pack_forget()
    self.buy_frame = BuyFrame(self, self.create_main_frame)
    self.buy_frame.pack(fill="both", expand=True)

  def open_view_receipt_frame(self):
    # Hide main frame and open view receipt frame
    self.main_frame.pack_forget()
    self.view_receipt_frame = ViewReceiptFrame(self, self.create_main_frame)
    self.view_receipt_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()