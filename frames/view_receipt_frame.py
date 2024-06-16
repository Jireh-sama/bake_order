import customtkinter as ctk
from utils.ctk_utils import create_frame, create_label, create_image, create_button
from frames.buy_frame import confirmed_order

class CustomTopBorderFrame(ctk.CTkFrame):
    def __init__(self, parent, border_color="black", border_width=2, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        # Main frame to hold everything
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent", height=10)
        self.main_frame.pack(fill="both", expand=True)

        # Top border frame
        self.top_border = ctk.CTkFrame(self.main_frame,  fg_color=border_color, height=border_width)
        self.top_border.pack(side="top", fill="x")
        
        # Inner frame for content
        self.inner_frame = ctk.CTkFrame(self.main_frame, fg_color="#F8EDE3", height=10)
        self.inner_frame.pack(fill="both", expand=True)

    def add_widget(self, widget, **kwargs):
        widget.pack(in_=self.inner_frame, **kwargs)

class ViewReceiptFrame(ctk.CTkFrame):
    def __init__(self, parent, go_back):
        super().__init__(parent)
        self.go_back = go_back
        self.configure(fg_color="#F8EDE3")  
        self.create_widgets()
        
    def create_block(self, parent, item_name, item_quantity, item_price):
        # Create a frame for each item
        item_block = ctk.CTkFrame(parent, fg_color="#F8EDE3", width=50, height=25)
        item_block.pack(fill="x", pady=5)  # Add some padding between items

        # Create labels for item name and price
        block_text1 = ctk.CTkLabel(item_block, text=f"{item_name} x{item_quantity}", fg_color="#F8EDE3")
        block_text1.pack(side="left", padx=(50, 0))

        block_text2 = ctk.CTkLabel(item_block, text=item_price, fg_color="#F8EDE3")
        block_text2.pack(side="right", padx=(0, 50))

    def create_item_blocks(self, parent, items, limit=7):
        for i, item in enumerate(items):
          if i >= limit:
            break
          self.create_block(parent=parent, item_name=item['name'], item_quantity=item['quantity'], item_price=item['price'])

        if len(items) > limit:
          # Add a label to indicate there are more items not shown
          overflow_label = ctk.CTkLabel(parent, text=f"...and {len(items) - limit} more items", fg_color="#F8EDE3")
          overflow_label.pack(fill="x", side="left", padx=(50, 0))

    def get_total(self):
      if not confirmed_order.confirmed_order_list:
        return 0
      sum = 0
      for total in confirmed_order.confirmed_order_list:
        sum += total['total']
      return sum

    def create_widgets(self):
        # Content Frame
        self.content_frame = create_frame(self, bg_color="#F8EDE3", width=400, height=400)
        self.content_frame.pack(side="top", fill="y", expand=True)
        self.content_frame.pack_propagate(False)

        self.logo_img = create_image(parent=self.content_frame, path="./assets//media//bake-order-logo.png", width=130, height=100)
        self.logo_img.pack(pady=(10, 0))

        self.table_header_frame = create_frame(parent=self.content_frame,bg_color="#F8EDE3", width=400, height=30)
        self.table_header_frame.pack(fill="x")
        
        self.table_header_text1 = create_label(parent=self.table_header_frame, text="Item Name")
        self.table_header_text1.pack(side="left", padx=(50, 0))
        self.table_header_text2 = create_label(parent=self.table_header_frame, text="Price")
        self.table_header_text2.pack(side="right", padx=(0, 50))

        self.line1 = CustomTopBorderFrame(parent=self.content_frame, border_color="black", border_width=3, height=10)
        self.line1.pack(fill="x")

        self.table_content = create_frame(self.content_frame, bg_color="#F8EDE3", width=100, height=300)
        self.table_content.pack(fill="x")
        self.table_content.pack_propagate(False)
        # Dynamic Content Here
        
        items = [
          {'name': 'Redvelvet Cake', 'price': 399},
          {'name': 'Chocolate Cake', 'price': 299},
          {'name': 'Vanilla Cake', 'price': 199},
          {'name': 'Strawberry Cake', 'price': 349},
          {'name': 'Cheesecake', 'price': 279},
          {'name': 'Carrot Cake', 'price': 219},
          {'name': 'Lemon Cake', 'price': 259},
          {'name': 'Blueberry Muffin', 'price': 149},
          {'name': 'Apple Pie', 'price': 189},
        ]
        self.create_item_blocks(parent=self.table_content, items=confirmed_order.confirmed_order_list)

        self.line2 = CustomTopBorderFrame(parent=self.content_frame, border_color="black", border_width=3, height=10)
        self.line2.pack(fill="x")

        self.table_footer_frame = create_frame(parent=self.content_frame,bg_color="#F8EDE3", width=400, height=30)
        self.table_footer_frame.pack(fill="x")
        
        self.table_footer_text1 = create_label(parent=self.table_footer_frame, text="Total")
        self.table_footer_text1.pack(side="left", padx=(50, 0))
        self.table_footer_text2 = create_label(parent=self.table_footer_frame, text=self.get_total())
        self.table_footer_text2.pack(side="right", padx=(0, 50))



        # Footer Frame
        self.footer_frame = create_frame(self, bg_color="#E49748", width=110, height=110)
        self.footer_frame.pack(side="top", fill="x")
        self.footer_frame.pack_propagate(False)

        self.back_btn = create_button(parent=self.footer_frame, text="Back", command=self.go_back, width=80, height=30, bg_color="#D0B8A8", b_raduis=15)
        self.back_btn.pack(side="left", padx=(15, 0))


        