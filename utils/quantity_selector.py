import customtkinter as ctk

class QuantitySelector(ctk.CTkFrame):
    def __init__(self, parent, command=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(fg_color="#F8EDE3")
        self.quantity = 1
        self.command = command
        
        # Create decrement button
        self.decrement_btn = ctk.CTkButton(self, text="-", command=self.decrement, width=20, height=30, fg_color="white", text_color="black")
        self.decrement_btn.pack(side="left")
        
        # Create entry field for quantity display
        self.quantity_entry = ctk.CTkEntry(self, width=40)
        self.quantity_entry.insert(0, "1")
        self.quantity_entry.pack(side="left")
        
        # Create increment button
        self.increment_btn = ctk.CTkButton(self, text="+", command=self.increment, width=20, height=30, fg_color="white", text_color="black")
        self.increment_btn.pack(side="left")
        
    def decrement(self):
        if self.quantity > 1:
            self.quantity -= 1
            self.quantity_entry.delete(0, ctk.END)
            self.quantity_entry.insert(0, str(self.quantity))
            if self.command:
                self.command()
        
    def increment(self):
        self.quantity += 1
        self.quantity_entry.delete(0, ctk.END)
        self.quantity_entry.insert(0, str(self.quantity))
        if self.command:
            self.command()
        
    def get_quantity(self):
        return self.quantity


