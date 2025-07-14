import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        
        product = num1 * num2
        
        messagebox.showinfo("Product Result", f"The product is: {product}")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers in both fields.")
    except Exception as e:
        messagebox.showerror("An Error Occurred", f"Something went wrong: {e}")

root = tk.Tk()
root.title("Product Calculator")
root.geometry("350x200")

tk.Label(root, text="First Number:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
num1_entry = tk.Entry(root, width=25)
num1_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Second Number:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
num2_entry = tk.Entry(root, width=25)
num2_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate Product", width=20, command=calculate_product)
calculate_button.grid(row=2, column=0, columnspan=2, pady=15)

root.mainloop()