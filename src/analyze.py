import pandas as pd

# My averages
def gpa_per_term(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Term").apply(lambda x: weighted_gpa(x)).reset_index("TermGPA")

def gpa_per_year(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Year").apply(lambda x: weighted_gpa(x)).reset_index("YearGPA")

def gpa_per_dept(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Dept").apply(lambda x: weighted_gpa(x)).reset_index("DeptGPA")

def weighted_gpa(df: pd.DataFrame) -> float:
    total_grade_points = df["GradePoints"].sum()
    total_units = df["Units"].sum()
    return total_grade_points / total_units

# Class averages
def gpa_per_term_class_averages(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Term").apply(lambda x: weighted_gpa_class_averages(x)).reset_index("TermGPAAverages")

def gpa_per_year_class_averages(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Year").apply(lambda x: weighted_gpa_class_averages(x)).reset_index("YearGPAAverages")

def gpa_per_dept_class_averages(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Dept").apply(lambda x: weighted_gpa_class_averages(x)).reset_index("TermGPAAverages")

def weighted_gpa_class_averages(df: pd.DataFrame) -> float:
    total_grade_points_average = (df["ClassAvgGradePoint"] * df["Units"]).sum()
    total_units = df["Units"].sum()
    return total_grade_points_average / total_units