import tkinter as tk
from tkinter import ttk

def submit():
    try:
        v = float(e.get())
        t = c.get()

        if t == "Rupees to Dollars":
            res = f"{v} INR = {v * 0.012:.2f} USD"
        elif t == "Dollars to Rupees":
            res = f"{v} USD = {v / 0.012:.2f} INR"
        elif t == "Celsius to Fahrenheit":
            res = f"{v}°C = {(v * 9/5) + 32:.2f}°F"
        elif t == "Fahrenheit to Celsius":
            res = f"{v}°F = {(v - 32) * 5/9:.2f}°C"
        elif t == "Inches to Feet":
            res = f"{v} in = {v / 12:.2f} ft"
        elif t == "Feet to Inches":
            res = f"{v} ft = {v * 12:.2f} in"
        else:
            res = "Select a valid conversion type."

    except ValueError:
        res = "Please enter a valid number."

    o.delete("1.0", tk.END)
    o.insert(tk.END, res)

# GUI setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("320x320")
root.resizable(False, False)

tk.Label(root, text="Enter value:", font=("Arial", 12)).pack(pady=5)
e = tk.Entry(root, font=("Arial", 12))
e.pack()

tk.Label(root, text="Select conversion:", font=("Arial", 12)).pack(pady=5)
options = [
    "Rupees to Dollars",
    "Dollars to Rupees",
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius",
    "Inches to Feet",
    "Feet to Inches"
]
c = ttk.Combobox(root, values=options, state="readonly", font=("Arial", 11))
c.pack()

tk.Button(root, text="Submit", command=submit, font=("Arial", 12), bg="lightblue").pack(pady=10)

tk.Label(root, text="Output Box:", font=("Arial", 11)).pack()
o = tk.Text(root, height=2, width=30, font=("Arial", 11))
o.pack(pady=5)

root.mainloop()
