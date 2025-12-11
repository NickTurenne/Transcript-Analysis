import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import src.analyze as an

def plot_GPA_by_term(df: pd.DataFrame):
    df_term_gpa = an.gpa_per_term(df)
    df_term_gpa = df_term_gpa.sort_values("TermIndex").reset_index(drop=True)
    df_term_gpa["PlotIndex"] = range(len(df_term_gpa))
    df_term_gpa_class = an.gpa_per_term_class_averages(df)
    df_term_gpa_class = df_term_gpa_class.sort_values("TermIndex").reset_index(drop=True)
    df_term_gpa_class["PlotIndex"] = range(len(df_term_gpa_class))
    plt.figure(figsize=(18,6))
    plt.title("GPA by Term Compared to Averages")
    plt.ylabel("GPA")
    plt.xlabel("Term")
    sns.lineplot(data=df_term_gpa, x="PlotIndex", y="TermGPA", label="My GPA", color='purple')
    sns.lineplot(data=df_term_gpa_class, x="PlotIndex", y="ClassAverageGPATerm", label="Class Average GPA", color='red')
    _ = plt.xticks(
        ticks=df_term_gpa["PlotIndex"],
        labels=df_term_gpa["Term"],
        rotation=45
    )