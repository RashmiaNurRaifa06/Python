import tkinter as tk
from tkinter import ttk, messagebox

class ResturauntOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Resturaunt Management App")
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESEBURGER MEAL": 2.5,
            "DRINKS": 1
        }
        
        self.exchange_rate = 120
        
        self.root.configure(bg = "#f2f2f2")
        
        frame = ttk.Frame(root)
        frame.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
        
        ttk.Label(frame, text = "Resturaunt Management System", font = ("Arial", 20, "bold")).grid(row = 0, columnspan = 3, padx = 10, pady = 10)
        
        self.menu_labels = {}
        self.menu_quantities = {}
        
        for i, (item, price) in enumerate(self.menu_items.items(), start = 1):
            label = ttk.Label(frame, text = f"{item} (${price}):", font = ("Arial", 12))
            label.grid(row = i, column = 0, padx = 10, pady = 5)
            self.menu_labels[item] = label
            
            quantity_entry = ttk.Entry(frame, width = 5)
            quantity_entry.grid(row = i, column = 1, padx = 10, pady = 5)
            self.menu_quantities[item] = quantity_entry
            
        self.currency_var = tk.StringVar()
        ttk.Label(frame, text = "Currency: ", font = ("Arial", 20,)).grid(row = len(self.menu_items) + 1, column = 0, padx = 10, pady = 5)
        
        currency_dropdown = ttk.Combobox(frame, textvariable = self.currency_var, state = "readonly", width = 18, values = ('USD', 'BDT') )
        currency_dropdown.grid(row = len(self.menu_items) + 1, column = 0, padx = 10, pady = 5)
        currency_dropdown.current(0)
        self.currency_var.trace('w', self.update_menu_prices)
        
        order_button = ttk.order(frame, text = "Place order: ", command = self.place_order)
        order_button.grid(row = len(self.menu_items) + 2, columnspan = 3, padx = 10, pady = 10)
        
    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "₹" if currency == "BDT" else "$"
        rate = self.exchange_rate if currency == "BDT" else 1
        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text = f"{item} ({symbol}{price}:)")
            
    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary: \n" 
        currency = self.currency_var.get();
        symbol = "₹" if currency == "BDT" else "$"
        rate = self.exchange_rate if currency == "BDT" else 1
        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost = quantity * price
                total_cost += cost
                if quantity > 0:
                    order_summary += f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least one item")
            
if __name__ == "__main__":
    root = tk.Tk()
    app = ResturauntOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()