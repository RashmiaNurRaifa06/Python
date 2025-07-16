import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        feet = int(feet_entry.get())
        inches = int(inches_entry.get())
        total_inches = feet * 12 + inches
        height_m = total_inches * 0.0254
        bmi_weight = weight / (height_m ** 2)
        bmi = round(bmi, 2)
        if bmi < 18.5:
            status = "Underweight"
            color = "#00BFFF"
        elif 18.5 <= bmi <= 24.9:
            status = "Normal weight"
            color = "#32CD32"
        elif 25 <= bmi <= 29.9:
            status = "Overweight"
            color = "#FFD700"
        else:
            status = "Obese"
            color = "#FF4500"
        result_label.config(text = f"BMI: {bmi}\nStatus: {status}", bg = color)
    except Exception:
        messagebox.showerror("Invalid number or input.", "Please enter valid numbers.")
        
root = tk.Tk()
root.title("Colorful BMI Calculator")
root.geometry("350x300")
root.configure(bg = "#f0e68c")

title = tk.Label(root, text = "BMI Calculator", font = ("Arial", 18, "bold"), bg = "#f0e68c", fg = "#4B0082")
title.pack(pady = 10)

frame = tk.Frame(root, bg = "#f0e68c")
frame.pack(pady = 10)

tk.Label(frame, text = "Weight(kg): ", font = ("Arial", 12) bg = "#f0e68c").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "e")
weight_entry = tk.Entry(frame, font = ("Arial", 12))
weight_entry.grid(row = 0, column = 1, padx = 5, pady = 5)

tk.Label(frame, text = "Height: ", font = ("Arial", 12) bg = "#f0e68c").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "e")
weight_entry = tk.Entry(frame, width = 5, font = ("Arial", 12))
weight_entry.grid(row = 0, column = 1, padx = 5, pady = 5)