import tkinter as tk
from tkinter import messagebox

class LengthConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Length Converter")
        master.geometry("450x250")
        master.resizable(False, False)

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)

        self.conversion_factors = {
            "Meters": 1.0,
            "Kilometers": 1000.0,
            "Centimeters": 0.01,
            "Millimeters": 0.001,
            "Miles": 1609.34,
            "Yards": 0.9144,
            "Feet": 0.3048,
            "Inches": 0.0254
        }

        self.units = sorted(list(self.conversion_factors.keys()))

        self.from_value_label = tk.Label(master, text="From Value:")
        self.from_value_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.from_value_entry = tk.Entry(master, width=15)
        self.from_value_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.from_value_entry.insert(0, "0.0")
        self.from_value_entry.bind("<KeyRelease>", self.convert_length)

        self.from_unit_var = tk.StringVar(master)
        self.from_unit_var.set("Meters")
        self.from_unit_menu = tk.OptionMenu(master, self.from_unit_var, *self.units)
        self.from_unit_menu.config(width=12)
        self.from_unit_menu.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.from_unit_var.trace_add("write", self.convert_length_trace)

        self.to_value_label = tk.Label(master, text="To Value:")
        self.to_value_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.to_value_entry = tk.Entry(master, width=15, state="readonly")
        self.to_value_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.to_unit_var = tk.StringVar(master)
        self.to_unit_var.set("Kilometers")
        self.to_unit_menu = tk.OptionMenu(master, self.to_unit_var, *self.units)
        self.to_unit_menu.config(width=12)
        self.to_unit_menu.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.to_unit_var.trace_add("write", self.convert_length_trace)

        self.convert_length()

    def convert_length_trace(self, *args):
        self.convert_length()

    def convert_length(self, event=None):
        try:
            value = float(self.from_value_entry.get())
            from_unit = self.from_unit_var.get()
            to_unit = self.to_unit_var.get()

            value_in_meters = value * self.conversion_factors[from_unit]
            converted_value = value_in_meters / self.conversion_factors[to_unit]

            self.to_value_entry.config(state="normal")
            self.to_value_entry.delete(0, tk.END)
            self.to_value_entry.insert(0, f"{converted_value:.4f}")
            self.to_value_entry.config(state="readonly")

        except ValueError:
            self.to_value_entry.config(state="normal")
            self.to_value_entry.delete(0, tk.END)
            self.to_value_entry.insert(0, "Invalid Input")
            self.to_value_entry.config(state="readonly")
            messagebox.showerror("Invalid Input", "Please enter a valid number for the value.")
        except KeyError:
            self.to_value_entry.config(state="normal")
            self.to_value_entry.delete(0, tk.END)
            self.to_value_entry.insert(0, "Error")
            self.to_value_entry.config(state="readonly")
            messagebox.showerror("Error", "Selected units are invalid. Please restart the app.")
        except Exception as e:
            self.to_value_entry.config(state="normal")
            self.to_value_entry.delete(0, tk.END)
            self.to_value_entry.insert(0, "Error")
            self.to_value_entry.config(state="readonly")
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LengthConverterApp(root)
    root.mainloop()
