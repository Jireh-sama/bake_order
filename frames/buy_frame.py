import sys
sys.path.append('../utils/')
sys.path.append('../libs/')
import customtkinter as ctk
from utils.ctk_utils import create_frame, create_image, create_label, create_button
from utils.quantity_selector import QuantitySelector
from libs.order import Order
from libs.confirmed_order import ConfirmedOrder
from libs.item import Item

# Global variables
item1 = Item(name="Redvelvet Cake", price=399)
item2 = Item(name="Chocolate Cake", price=499)
item3 = Item(name="Carroot Cake", price=379)
item4 = Item(name="Lemon Drizzle Cake", price=499)
item5 = Item(name="Vanilla Sponge Cake", price=599)
item6 = Item(name="Coffee Cake", price=199)

customer_order = Order()
confirmed_order = ConfirmedOrder()

class BuyFrame(ctk.CTkFrame):
  def __init__(self, parent, go_back):
    super().__init__(parent)
    self.go_back = go_back
    self.configure(fg_color="#F8EDE3")
    self.total = 0

    self.create_widgets()

  def sample(self):
    console.log('Sample');

  def add_item(self, name, price, quantity):
    totalsum = price * quantity
    self.total += totalsum
    self.total_price_label.configure(text=f"Total Price: {self.total}")
    customer_order.add_item(name=name, price=price, quantity=quantity, total=totalsum)
    print(self.total)
    print(customer_order.item_list)

  def confirm_order(self):
    confirmed_order.confirm_order(customer_order.get_items())
    customer_order.clear_order()
    self.total_price_label.configure(text=f"Total Price: {customer_order.get_total()}")
    
  def create_widgets(self):
    # Label
    # self.text_label = create_label(parent=self, text="This is the Customer Frame")
    # self.text_label.pack()

    # Button to go back to main window
    # self.back_button = ctk.CTkButton(self, text="Back", command=self.go_back)
    # self.back_button.pack(pady=10)

    self.item_frame1 = create_frame(self, width=228, height=250, bg_color="#F8EDE3")
    self.item1_label = create_label(self.item_frame1, f"{item1.name} ₱{item1.price}")
    self.item1_label.configure(height=250)
    self.item1_label.pack()

    self.quantity_selector_item1 = QuantitySelector(self.item_frame1, width=100, height=30)
    self.quantity_selector_item1.place(relx=0.15, rely=0.95, anchor="s")
  
    self.item1_btn = create_button(self.item_frame1, "Order Now", command=lambda: self.add_item(name=item1.name,price=item1.price, quantity=self.quantity_selector_item1.get_quantity()), width=80, height=30, bg_color="#D0B8A8", b_raduis=15)
    self.item1_btn.place(relx=0.80, rely=0.95, anchor="s")

    ###################################################1
    self.item_frame2 = create_frame(self, width=228, height=250, bg_color="#F8EDE3")
    self.item2_label = create_label(self.item_frame2, f"{item2.name} ₱{item2.price}")
    self.item2_label.configure(height=250)
    self.item2_label.pack()

    self.quantity_selector_item2 = QuantitySelector(self.item_frame2, width=100, height=30)
    self.quantity_selector_item2.place(relx=0.15, rely=0.95, anchor="s")
  
    self.item2_btn = create_button(self.item_frame2, "Order Now", command=lambda: self.add_item(name=item2.name,price=item2.price, quantity=self.quantity_selector_item2.get_quantity()), width=80, height=30, bg_color="#D0B8A8", b_raduis=15)
    self.item2_btn.place(relx=0.80, rely=0.95, anchor="s")
    ###################################################1
    self.item_frame3 = create_frame(self, width=228, height=250, bg_color="#F8EDE3")
    self.item3_label = create_label(self.item_frame3, f"{item3.name} ₱{item3.price}")
    self.item3_label.configure(height=250)
    self.item3_label.pack()

    self.quantity_selector_item3 = QuantitySelector(self.item_frame3, width=100, height=30)
    self.quantity_selector_item3.place(relx=0.15, rely=0.95, anchor="s")
  
    self.item3_btn = create_button(self.item_frame3, "Order Now", command=lambda: self.add_item(name=item3.name,price=item3.price, quantity=self.quantity_selector_item3.get_quantity()), width=80, height=30, bg_color="#D0B8A8", b_raduis=15)
    self.item3_btn.place(relx=0.80, rely=0.95, anchor="s")
    ###################################################1
    self.item_frame4 = create_frame(self, width=228, height=250, bg_color="#F8EDE3")
    self.item4_label = create_label(self.item_frame4, f"{item4.name} ₱{item4.price}")
    self.item4_label.configure(height=250)
    self.item4_label.pack()

    self.quantity_selector_item4 = QuantitySelector(self.item_frame4, width=100, height=30)
    self.quantity_selector_item4.place(relx=0.15, rely=0.95, anchor="s")
  
    self.item4_btn = create_button(self.item_frame4, "Order Now", command=lambda: self.add_item(name=item4.name,price=item4.price, quantity=self.quantity_selector_item4.get_quantity()), width=80, height=30, bg_color="#D0B8A8", b_raduis=15)
    self.item4_btn.place(relx=0.80, rely=0.95, anchor="s")
    ###################################################1
    self.item_frame5 = create_frame(self, width=228, height=250, bg_color="#F8EDE3")
    self.item5_label = create_label(self.item_frame5, f"{item5.name} ₱{item5.price}")
    self.item5_label.configure(height=250)
    self.item5_label.pack()

    self.quantity_selector_item5 = QuantitySelector(self.item_frame5, width=100, height=30)
    self.quantity_selector_item5.place(relx=0.15, rely=0.95, anchor="s")
  
    self.item5_btn = create_button(self.item_frame5, "Order Now", command=lambda: self.add_item(name=item5.name,price=item5.price, quantity=self.quantity_selector_item5.get_quantity()), width=80, height=30, bg_color="#D0B8A8", b_raduis=15)
    self.item5_btn.place(relx=0.80, rely=0.95, anchor="s")
    ###################################################1
    self.item_frame6 = create_frame(self, width=228, height=250, bg_color="#F8EDE3")
    self.item6_label = create_label(self.item_frame6, f"{item6.name} ₱{item6.price}")
    self.item6_label.configure(height=250)
    self.item6_label.pack()

    self.quantity_selector_item6 = QuantitySelector(self.item_frame6, width=100, height=30)
    self.quantity_selector_item6.place(relx=0.15, rely=0.95, anchor="s")
  
    self.item6_btn = create_button(self.item_frame6, "Order Now", command=lambda: self.add_item(name=item6.name,price=item6.price, quantity=self.quantity_selector_item6.get_quantity()), width=80, height=30, bg_color="#D0B8A8", b_raduis=15)
    self.item6_btn.place(relx=0.80, rely=0.95, anchor="s")
    

    

   

 
    # Footer Section
    self.footer_frame = create_frame(self, width=1000, height=110, bg_color="#E49748")
    self.footer_frame.place(relx=0.5, rely=1.0, anchor="s", relwidth=1.0, relheight=0.10)

    self.back_btn = create_button(self.footer_frame, "Back", command=self.go_back, width=80, height=30, bg_color="#D0B8A8", b_raduis=15)
    self.back_btn.place(relx=0.06, rely=0.72, anchor="s")

    self.total_price_label = create_label(self.footer_frame, f"Total Price: {customer_order.get_total()}")
    self.total_price_label.place(relx=0.50, rely=0.72, anchor="s")

    self.confirm_order_btn = create_button(self.footer_frame, "Confirm Order", command=self.confirm_order, width=80, height=30, bg_color="#D0B8A8", b_raduis=15)
    self.confirm_order_btn.place(relx=0.93, rely=0.72, anchor="s")

    self.grid_rowconfigure(2, weight=1)  # Allow the row to expand vertically
    self.grid_columnconfigure((0, 1, 2), weight=1)  # Allow columns to expand horizontally

    # Pack the widgets inside the frame using grid-like layout
    self.item_frame1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    self.item_frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
    self.item_frame3.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
    self.item_frame4.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    self.item_frame5.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
    self.item_frame6.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)