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

age = df[['age']]


for i in range(82):
    if age['age'][i] < 100:
        continue
    else:
        age['age'][i] = 2022-age['age'][i]

    df['employed'] = df['employed'].replace(['Yes'], 1)
    df['employed'] = df['employed'].replace(['No'], 0)

employed = df[['employed']]






root = tk.Tk()
root.geometry('500x500')
var = tk.StringVar()
label = tk.Label(root, textvariable=var, pady=10)
var.set(" Correlations ")

label.pack()


def age_employment():


    x_stn = StandardScaler().fit_transform(age)
    # sklearn_result = pd.DataFrame(data=x, columns=['age'])
    # sklearn_result['y'] = 0
    # sklearn_result['employed'] = y
    # sns.lmplot(data=sklearn_result, x="employed", y="age", hue='age')
    plt.title('is the age of a person correlated to them being employed ?')
    plt.ylabel('age')
    plt.xlabel('employment')
    # plt.plot(x, y)
    bars = ('employed', 'unemployed')
    y_pos = np.arange(len(bars))
    plt.scatter(employed, age)
    plt.xticks(y_pos, bars)
    # plt.hist(y, bins=[0, 0.5, 1])
    plt.show()



    # Basic plot
    plt.bar(employed, age, color=(0.2, 0.4, 0.6, 0.6))

    # use the plt.xticks function to custom labels

    plt.show()

def hobby_developer():
    df['web_or_mobile'] = df['web_or_mobile'].replace(['web developer'], 1)
    df['web_or_mobile'] = df['web_or_mobile'].replace(['Mobile application developer'], 1)
    df['spending_spare_time'] = df['spending_spare_time'].replace(['Gaiming'], 1)
    df['spending_spare_time'] = df['spending_spare_time'].replace(['Other'], 2)
    df['spending_spare_time'] = df['spending_spare_time'].replace(['Spending time with family and friends'], 3)
    df['spending_spare_time'] = df['spending_spare_time'].replace(['Sport'], 4)
    df['spending_spare_time'] = df['spending_spare_time'].replace(['Watching TV'], 5)
    web_dev = df[['web_or_mobile']]
    web_dev['spending_spare_time'] = df[['spending_spare_time']]
    plt.title('is the hobbies of a developer is correlated with being a developer ?')
    plt.xlabel('spending_spare_time')
    plt.ylabel('developer')
    height = [0, 0, 0, 0, 0]
    for i in range(82):
        if web_dev['spending_spare_time'][i] == 1:
            height[0] = height[0]+1
        elif web_dev['spending_spare_time'][i] == 2:
                height[1] = height[1] + 1
        elif web_dev['spending_spare_time'][i] == 3:
                height[2] = height[2] + 1
        elif web_dev['spending_spare_time'][i] == 4:
                height[3] = height[3] + 1
        elif web_dev['spending_spare_time'][i] == 5:
                height[4] = height[4] + 1

    df['employed'] = df['employed'].replace(['Yes'], 1)
    df['employed'] = df['employed'].replace(['No'], 0)
    # Data set
    # height = web_dev['spending_spare_time']
    bars = ('gaming', 'other', 'going out', 'sports', 'watching TV')
    y_pos = np.arange(len(bars))

    # Basic plot
    plt.bar(y_pos, height, color=(0.2, 0.8, 0.6, 0.6))

    # use the plt.xticks function to custom labels
    plt.xticks(y_pos, bars)
    plt.show()


def age_salary():

    df['salary'] = df['salary'].replace(['0$'], 0)
    df['salary'] = df['salary'].replace(['100 $ - 500 $'], 250)
    df['salary'] = df['salary'].replace(['500 $ - 1000 $'], 750)
    df['salary'] = df['salary'].replace(['1000 $ - 1500 $'], 1250)
    df['salary'] = df['salary'].replace(['1500 $ - 2000 $'], 1750)
    salary = df[['salary']]
    salary['age'] = age
    plot = sns.lmplot(data=salary, x="salary", y="age", hue='salary')
    plot.set_axis_labels("Salary in dollars $", "Age")
    plot.fig.subplots_adjust(top=.95)
    plt.gca().set_title("correlation between age and salary")
    plt.show()


def satisfaction_age():

    df['satisfied'] = df['satisfied'].replace(['Unsatisfied'], 1)
    df['satisfied'] = df['satisfied'].replace(['Very unsatisfied'], 2)
    df['satisfied'] = df['satisfied'].replace(['Neutral'], 3)
    df['satisfied'] = df['satisfied'].replace(['satisfied'], 4)
    df['satisfied'] = df['satisfied'].replace(['Very satisfied'], 5)

    satisfaction = df[['satisfied']]
    satisfaction['age'] = age
    plot = sns.lmplot(data=satisfaction, x="satisfied", y="age", hue='satisfied', height=5.5)
    plot.set_axis_labels("Satisfaction on scale 1 - 5", "Age")
    plot.fig.subplots_adjust(top=.95)
    plot.ax.set_title('Correlation between age and satisfaction with being a developer')
    plt.show()


frame = tk.Frame(root)
frame.pack(pady=20, padx=5)

button1 = tk.Button(frame, text="theory 1", height=2, width=15, command=age_employment)
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = tk.Button(frame, text="theory 2", height=2, width=15, command=hobby_developer)
button2.grid(row=0, column=1, padx=5, pady=5)

button3 = tk.Button(frame, text="theory 3", height=2, width=15, command=age_salary)
button3.grid(row=1, column=0, padx=5, pady=5)

button4 = tk.Button(frame, text="theory 4", height=2, width=15, command=satisfaction_age)
button4.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
