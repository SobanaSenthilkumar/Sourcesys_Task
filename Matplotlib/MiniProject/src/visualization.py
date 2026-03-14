import matplotlib.pyplot as plt

def plot_average_scores(df):

    subjects = ["math","science","english"]
    averages = [
        df["math"].mean(),
        df["science"].mean(),
        df["english"].mean()
    ]

    plt.bar(subjects, averages)

    plt.title("Average Scores by Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")

    plt.show()


def plot_student_scores(df):

    plt.plot(df["name"], df["average"], marker="o")

    plt.title("Student Average Scores")
    plt.xlabel("Students")
    plt.ylabel("Average Marks")

    plt.grid(True)

    plt.show()