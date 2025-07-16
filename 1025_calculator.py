import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(screen.get())))
            screen.delete = (0, tk.END)
            screen.insert = (0, result)
        except:
            screen.delete = (0, tk.END)
            screen.insert = (0, "Error")
    elif text == "C":
        screen.delete = (0, tk.END)
    else:
        screen.insert = (tk.END, text)
        
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.resizable(0, 0)
root.configure(bg = "#222831")

screen = tk.Entry(root, font = "Arial 24", borderwidth = 5, relief = tk.RIDGE, justify = "right", bg = "#393e46",fg = "#eeeeee")
screen.pack(fill = tk.BOTH, ipadx = 8, ipady = 20, padx = 10, pady = 20)

btns_frame = tk.Frame(root, bg = "#222831")
btns_frame.pack()

btn_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

btn_colors = [
    ["#00adb5", "#00adb5", "#00adb5", "#ff5722"],
    ["#00adb5", "#00adb5", "#00adb5", "#ff5722"],
    ["#00adb5", "#00adb5", "#00adb5", "#ff5722"],
    ["#00adb5", "#00adb5", "#f44336", "#ff5722"],
    ["#4caf50"]
]

for i, row in enumerate(btn_texts):
    frame = tk.Frame(btns_frame, bg = "#222831")
    frame.pack(expand = True, fill = "both")
    for j, text in enumerate(row):
        btn = tk.Button(
            frame,
            text = text,
            font = "Arial 20 bold",
            width = 5,
            height = 2,
            bg = btn_colors[i][j],
            fg = "#eeeeee",
            activebackground = "#393e46",
            activeforeground = "#00adb5",
            borderwidth = 0   
        )
        btn.pack(side = "left", expand = True, fill = "both", padx = 5, pady = 5)
        btn.bind("<Button - 1>", click)
        
root.mainloop()