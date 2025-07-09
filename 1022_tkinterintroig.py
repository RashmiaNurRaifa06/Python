import tkinter as tk
from tkinter import messagebox

def submit_info():
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()
    gender = gender_var.get()
    contact = entry_contact.get()
    info = f"Name: {name}\nAge: {age}\nGrade: {grade}\nGender: {gender}\nContact: {contact}"
    messagebox.showinfo("Submitted information:",info)
    
root = tk.Tk()
root.title("Student information")

tk.Label(root, text="Name:").grid(row = 0, column = 0, sticky = "e")
entry_name = tk.Entry(root)
entry_name.grid(row = 0, column = 1)

tk.Label(root, text="Age:").grid(row = 1, column = 0, sticky = "e")
entry_age = tk.Entry(root)
entry_age.grid(row = 1, column = 1)

tk.Label(root, text="Grade:").grid(row = 2, column = 0, sticky = "e")
entry_grade = tk.Entry(root)
entry_grade.grid(row = 2, column = 1)

tk.Label(root, text="Gender:").grid(row = 3, column = 0, sticky = "e")
gender_var = tk.StringVar(value = "Male")
tk.Radiobutton(root, text = "Male", variable = gender_var, value = "Male").grid(row = 3, column = 1, sticky = "w")
tk.Radiobutton(root, text = "Female", variable = gender_var, value = "Female").grid(row = 3, column = 2, sticky = "w")

tk.Label(root, text="Contact:").grid(row = 4, column = 0, sticky = "e")
entry_contact = tk.Entry(root)
entry_contact.grid(row = 4, column = 1)

tk.Button(root, text= "Submit", command = submit_info).grid(row = 5, column = 0, columnspan = 2, pady = 10)

root.mainloop()