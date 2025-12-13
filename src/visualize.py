import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns
import src.analyze as an

def plot_GPA_by_term(df: pd.DataFrame):
    df_term_gpa = an.gpa_per_term(df)
    df_term_gpa = df_term_gpa.sort_values("TermIndex").reset_index(drop=True)
    df_term_gpa["PlotIndex"] = range(len(df_term_gpa))
    plt.figure(figsize=(15,6))
    plt.rc('font', family='Arial')
    plt.title("GPA by Term Compared to Averages")
    plt.ylabel("GPA")
    plt.xlabel("Term")
    sns.lineplot(data=df_term_gpa, x="PlotIndex", y="TermGPA", label="My GPA", color='purple')
    sns.lineplot(data=df_term_gpa, x="PlotIndex", y="ClassAverageGPATerm", label="Class Average GPA", color='red')
    _ = plt.xticks(
        ticks=df_term_gpa["PlotIndex"],
        labels=df_term_gpa["Term"],
        rotation=45,
        ha='right'
    )

def plot_GPA_by_year(df: pd.DataFrame):
    df_year_gpa = an.gpa_per_year(df)
    plt.rc('font', family='Arial')
    plt.title("GPA by Year Compared to Averages")
    plt.ylabel("GPA")
    plt.xlabel("Year")
    sns.lineplot(data=df_year_gpa, x="Year", y="YearGPA", label="My GPA", color='purple')
    sns.lineplot(data=df_year_gpa, x="Year", y="YearGPAAverages", label="Class Average GPA", color='red')

def plot_GPA_by_dept(df: pd.DataFrame):
    palette = {
        "DeptGPA": "purple",
        "DeptGPAAverages": "red"
    }
    
    df_dept_gpa = an.gpa_per_dept(df)
    plt.rc('font', family='Arial')
    plt.figure(figsize=(15,6))
    plt.title("GPA by Department Compared to Averages")
    plt.ylabel("GPA")
    plt.xlabel("Department")
    
    chart = sns.barplot(data=df_dept_gpa, x="Dept", y="GPA", hue="Type", palette=palette)
    handles = [
        Patch(facecolor="purple", label="My GPA"),
        Patch(facecolor="red", label="Class Average GPA")
    ]
    chart.legend(handles=handles, title="")

def plot_GPA_by_course_level(df: pd.DataFrame):
    palette = {
        "LevelGPA": "purple",
        "LevelGPAAverages": "red"
    }
    
    df_course_gpa = an.gpa_by_course_level(df)
    plt.rc('font', family='Arial')
    plt.figure(figsize=(15,6))
    plt.title("GPA by Course Level Compared to Averages")
    plt.ylabel("GPA")
    plt.xlabel("Course Level")
    
    chart = sns.barplot(data=df_course_gpa, x="CourseLevel", y="GPA", hue="Type", palette=palette)
    handles = [
        Patch(facecolor="purple", label="My GPA"),
        Patch(facecolor="red", label="Class Average GPA")
    ]
    chart.legend(handles=handles, title="")

def plot_corr_matrix(df: pd.DataFrame):
    df_corr = an.get_corr_matrix(df)
    plt.rc('font', family='Arial')
    plt.title("Relationship between GPA and other Factors")
    sns.heatmap(df_corr, annot=True)
    plt.xticks(rotation=45, ha='right')

def plot_hardest_and_easiest_courses(df: pd.DataFrame):
    df_combined = pd.concat([df.nlargest(10, "DifficultyIndex"), df.nsmallest(10, "DifficultyIndex")])
    plt.rc('font', family='Arial')
    plt.figure(figsize=(15,6))
    plt.title("Ten Easiest and Hardest Courses Based on Difficulty Index")
    plt.ylabel("Difficulty")
    plt.xlabel("Course")
    sns.barplot(data=df_combined, x="Desc", y="DifficultyIndex", color='purple')
    plt.xticks(rotation=45, ha='right')

def plot_GPA_by_credit_load(df: pd.DataFrame):
    df_terms = an.gpa_by_credit_load(df)
    plt.rc('font', family='Arial')
    plt.figure(figsize=(10,6))
    plt.title("GPA by Credit Load per Term")
    plt.ylabel("GPA")
    plt.xlabel("Credit Load")
    sns.barplot(data=df_terms, x="TotalUnits", y="CreditLoadGPA", color='purple')
