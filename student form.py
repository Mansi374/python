import tkinter as tk
from tkinter import ttk

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    subjects = []
    if math_var.get():
        subjects.append("Math")
    if science_var.get():
        subjects.append("Science")
    if history_var.get():
        subjects.append("History")
    grade = grade_combobox.get()

    textbox.insert(tk.END, f"Name: {name}\n")
    textbox.insert(tk.END, f"Age: {age}\n")
    textbox.insert(tk.END, f"Gender: {gender}\n")
    textbox.insert(tk.END, f"Subjects: {', '.join(subjects)}\n")
    textbox.insert(tk.END, f"Grade: {grade}\n")
    textbox.insert(tk.END, "-" * 30 + "\n")

root = tk.Tk()
root.title("Student Form")

tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

tk.Label(root, text="Age:").pack(pady=5)
age_entry = tk.Entry(root, width=30)
age_entry.pack(pady=5)

tk.Label(root, text="Gender:").pack(pady=5)
gender_var = tk.StringVar(value="None")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

tk.Label(root, text="Subjects:").pack(pady=5)
math_var = tk.BooleanVar()
science_var = tk.BooleanVar()
history_var = tk.BooleanVar()
tk.Checkbutton(root, text="Math", variable=math_var).pack()
tk.Checkbutton(root, text="Science", variable=science_var).pack()
tk.Checkbutton(root, text="History", variable=history_var).pack()

tk.Label(root, text="Grade:").pack(pady=5)
grade_combobox = ttk.Combobox(root, values=["A", "B", "C", "D", "F"], state="readonly")
grade_combobox.pack()

tk.Button(root, text="Submit", command=submit_form).pack(pady=10)

textbox = tk.Text(root, height=10, width=40)
textbox.pack(pady=10)

root.mainloop()
