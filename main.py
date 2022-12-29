import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import decomposition
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

    df['satisfied'] = df['satisfied'].replace(['Unsatisfied'], 1)
    df['satisfied'] = df['satisfied'].replace(['Very unsatisfied'], 2)
    df['satisfied'] = df['satisfied'].replace(['Neutral'], 3)
    df['satisfied'] = df['satisfied'].replace(['satisfied'], 4)
    df['satisfied'] = df['satisfied'].replace(['Very satisfied'], 5)

    df['web_or_mobile'] = df['web_or_mobile'].replace(['web developer'], 1)
    df['web_or_mobile'] = df['web_or_mobile'].replace(['Mobile application developer'], 1)
    df['spending_spare_time'] = df['spending_spare_time'].replace(['Gaiming'], 1)
    df['spending_spare_time'] = df['spending_spare_time'].replace(['Other'], 2)
    df['spending_spare_time'] = df['spending_spare_time'].replace(['Spending time with family and friends'], 3)
    df['spending_spare_time'] = df['spending_spare_time'].replace(['Sport'], 4)
    df['spending_spare_time'] = df['spending_spare_time'].replace(['Watching TV'], 5)

    df['salary'] = df['salary'].replace(['0$'], 0)
    df['salary'] = df['salary'].replace(['100 $ - 500 $'], 250)
    df['salary'] = df['salary'].replace(['500 $ - 1000 $'], 750)
    df['salary'] = df['salary'].replace(['1000 $ - 1500 $'], 1250)
    df['salary'] = df['salary'].replace(['1500 $ - 2000 $'], 1750)

    df['education level'] = df['education level'].replace(["I haven't studied"], 0)
    df['education level'] = df['education level'].replace(['Secondary School'], 1)
    df['education level'] = df['education level'].replace(['High School'], 2)
    df['education level'] = df['education level'].replace(['diploma degree student'], 3)
    df['education level'] = df['education level'].replace(['bachelor degree student'], 4)
    df['education level'] = df['education level'].replace(["master's degree"], 5)
    df['education level'] = df['education level'].replace(['doctorate degree'], 6)
education = df[['education level']]
employed = df[['employed']]
salary = df[['salary']]

root = tk.Tk()
root.geometry('500x500')
var = tk.StringVar()
label = tk.Label(root, textvariable=var, pady=10)
var.set(" Correlations ")

label.pack()
width = 800  # Width
height = 400  # Height

screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight()  # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

root.geometry('%dx%d+%d+%d' % (width, height, x, y))


def age_employment():

    plt.title('Correlation between employment and age')
    plt.ylabel('age')
    plt.xlabel('employment')
    bars = ('employed', 'unemployed')
    y_pos = np.arange(len(bars))
    plt.scatter(employed, age)
    plt.xticks(y_pos, bars)
    plt.show()
    plt.bar(employed, age, color=(0.2, 0.4, 0.6, 0.6))
    plt.show()


def hobby_developer():

    web_dev = df[['web_or_mobile']]
    web_dev['spending_spare_time'] = df[['spending_spare_time']]
    plt.title('Correlation between being a developer and their hobbies')
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
    print(age)
    print(salary)
    salary_age = salary
    salary_age['age'] = age
    plot = sns.lmplot(data=salary, x="salary", y="age", hue='salary')
    plot.set_axis_labels("Salary in dollars $", "Age")
    plot.fig.subplots_adjust(top=.95)
    plt.gca().set_title("correlation between age and salary")
    plt.show()


def satisfaction_age():
    print(age)
    satisfaction_agev = df[['satisfied']]
    print(satisfaction_agev)
    satisfaction_agev['age'] = age
    plot = sns.lmplot(data=satisfaction_agev, x="satisfied", y="age", hue='satisfied', height=5.5)
    plot.set_axis_labels("Satisfaction on scale 1 - 5", "Age")
    plot.fig.subplots_adjust(top=.95)
    plot.ax.set_title('Correlation between age and satisfaction with being a developer')
    plt.show()


def education_age_salary():
    print(age)
    print(salary)
    print(education)
    age_salary3 = age
    age_salary3['salary'] = df[['salary']]
    age_salary3 = StandardScaler().fit_transform(age_salary3)
    pca = decomposition.PCA(n_components=1)
    sklearn_pca_age_salary = pca.fit_transform(age_salary3)
    sklearn_result = pd.DataFrame(sklearn_pca_age_salary, columns=['age_salary3'])
    sklearn_result['education'] = education
    plot = sns.lmplot(data=sklearn_result, x="age_salary3", y="education", fit_reg=False, hue='education')
    plot.set_axis_labels("Age and salary", "education on scale 1 - 5")
    plot.fig.subplots_adjust(top=.95)
    plot.ax.set_title('Correlation between age ,salary and education')
    plt.show()


def satisfaction_age_salary():

    age_salary2 = df[['age']]
    age_salary2['salary'] = df[['salary']]
    age_salary1 = StandardScaler().fit_transform(age_salary2)
    pca = decomposition.PCA(n_components=1)
    sklearn_pca_age_salary = pca.fit_transform(age_salary1)
    # print(sklearn_pca_age_salary)
    sklearn_result = pd.DataFrame(sklearn_pca_age_salary, columns=['age_salary'])
    sklearn_result['satisfied'] = df[['satisfied']]
    print(sklearn_result)
    plot = sns.lmplot(data=sklearn_result, x="age_salary", y="satisfied", fit_reg=False, hue='satisfied')
    plot.set_axis_labels("Age and salary", "Satisfaction on scale 1 - 5")
    plot.fig.subplots_adjust(top=.95)
    plot.ax.set_title('Correlation between age ,salary and satisfaction')
    plt.show()


frame = tk.Frame(root)
frame.place(anchor="center", relx=.5, rely=.5)
frame.pack(pady=20, padx=5)
button1 = tk.Button(frame, text="Correlation between employment and age",
                    height=2, width=50, command=age_employment, background="royalblue", foreground="white")
button1.grid(row=0, column=0, padx=5, pady=30)

button2 = tk.Button(frame, text="Correlation between being a developer and their hobbies",
                    height=2, width=50, command=hobby_developer, background="royalblue", foreground="white")
button2.grid(row=0, column=1, padx=5, pady=30)

button3 = tk.Button(frame, text="correlation between age and salary",
                    height=2, width=50, command=age_salary, background="royalblue", foreground="white")
button3.grid(row=1, column=0, padx=5, pady=30)

button4 = tk.Button(frame, text="Correlation between age and satisfaction with being a developer",
                    height=2, width=50, command=satisfaction_age, background="royalblue", foreground="white")
button4.grid(row=1, column=1, padx=5, pady=30)

button5 = tk.Button(frame, text="Correlation between age ,salary and education",
                    height=2, width=50, command=education_age_salary, background="royalblue", foreground="white")
button5.grid(row=2, column=0, padx=5, pady=30)

button6 = tk.Button(frame, text="Correlation between age ,salary and satisfaction",
                    height=2, width=50, command=satisfaction_age_salary, background="royalblue", foreground="white")
button6.grid(row=2, column=1, padx=5, pady=30)

root.mainloop()
