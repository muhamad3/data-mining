import pandas as pd
import tkinter as tk

df = pd.read_csv('web_vs_mobile.csv')
df = df.drop("Timestamp", axis=1)
df = df.drop("Full name", axis=1)
print(df)

root = tk.Tk()
root.geometry('500x500')

var = tk.StringVar()
label = tk.Label( root, textvariable=var, pady=10)
var.set(" Correlations ")

label.pack()

frame = tk.Frame(root)
frame.pack(pady=20, padx=5)

button1 = tk.Button(frame, text=df.columns[2]+" and "+df.columns[6], height=4, width=35)
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = tk.Button(frame, text="Button 2", height=2, width=15)
button2.grid(row=0, column=1, padx=5, pady=5)

button3 = tk.Button(frame, text="Button 3", height=2, width=15)
button3.grid(row=1, column=0, padx=5, pady=5)

button4 = tk.Button(frame, text="Button 4", height=2, width=15)
button4.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
