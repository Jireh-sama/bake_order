import customtkinter as ctk
from frames.landing_frame import LandingFrame
from frames.customer_frame import CustomerFrame
from frames.owner_frame import OwnerFrame

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
      check if both customer frame or owner frame exist
      if so hide it
    """
    if hasattr(self, 'customer_frame'):
        self.customer_frame.pack_forget() 
    if hasattr(self, 'owner_frame'):
        self.owner_frame.pack_forget() 

    # Open the landing frame
    self.main_frame = LandingFrame(self, open_customer=self.open_customer_frame, open_owner=self.open_owner_frame)
    self.main_frame.pack(fill="both", expand=True)


  def open_customer_frame(self):
    # Hide main frame and open customer frame
    self.main_frame.pack_forget()
    self.customer_frame = CustomerFrame(self, self.create_main_frame)
    self.customer_frame.pack(fill="both", expand=True)

  def open_owner_frame(self):
    # Hide main frame and open owner frame
    self.main_frame.pack_forget()
    self.owner_frame = OwnerFrame(self, self.create_main_frame)
    self.owner_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()