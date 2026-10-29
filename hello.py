
import tkinter as tk

root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("400x250")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 18))
label.pack(pady=30)

button = tk.Button(root, text="Click Me", command=lambda: label.config(text="It works!"))
button.pack()

root.mainloop()

