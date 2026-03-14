from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.analysis import perform_analysis
from src.visualization import plot_average_scores, plot_student_scores

def main():

    print("Student Performance Analysis Project")

    df = load_data(r"C:\Users\VICKY\OneDrive\Desktop\Sourcesys\Matplotlib\MiniProject\Data\Students.csv")

    df = preprocess_data(df)

    perform_analysis(df)

    plot_average_scores(df)

    plot_student_scores(df)

if __name__ == "__main__":
    main()