import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import tkinter as tk

df = pd.read_csv('web_vs_mobile.csv')
df = df.drop("Timestamp", axis=1)
df = df.drop("Full name", axis=1)
df.drop_duplicates()
print(df)

root = tk.Tk()
root.geometry('500x500')
var = tk.StringVar()
label = tk.Label(root, textvariable=var, pady=10)
var.set(" Correlations ")

label.pack()


def button_clicked():
    x = df[['age']]
    for i in range(82):
        if x['age'][i] < 100:
            continue
        else:
            x['age'][i] = 2022-x['age'][i]

    df['employed'] = df['employed'].replace(['Yes'], 1)
    df['employed'] = df['employed'].replace(['No'], 0)
    y = df[['employed']]
    x_stn = StandardScaler().fit_transform(x)
    sklearn_result = pd.DataFrame(data=x, columns=['age'])
    sklearn_result['y'] = 0
    sklearn_result['employed'] = y
    # sns.lmplot(data=sklearn_result, x="employed", y="age", hue='age')
    plt.title('employment')
    plt.xlabel('age')
    plt.ylabel('employment')
    # plt.plot(x, y)
    plt.scatter(x, y)
    plt.show()



frame = tk.Frame(root)
frame.pack(pady=20, padx=5)

button1 = tk.Button(frame, text="theory 1", height=2, width=15, command=button_clicked)
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = tk.Button(frame, text="theory 2", height=2, width=15)
button2.grid(row=0, column=1, padx=5, pady=5)

button3 = tk.Button(frame, text="theory 3", height=2, width=15)
button3.grid(row=1, column=0, padx=5, pady=5)

button4 = tk.Button(frame, text="theory 4", height=2, width=15)
button4.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
