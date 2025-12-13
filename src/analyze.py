import pandas as pd

# Averages
def gpa_per_term(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Term", as_index=False).agg(
        TermGPA=("GradePoints", lambda x: x.sum() / df.loc[x.index, "Units"].sum()),
        ClassAverageGPATerm=("ClassAvgGradePoint", lambda x: (x * df.loc[x.index, "Units"]).sum() / df.loc[x.index, "Units"].sum()),
        TermIndex=("TermIndex", "mean"),
        TotalUnits=("Units", "sum")
    )

def gpa_per_year(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Year", as_index=False).agg(
        YearGPA=("GradePoints", lambda x: x.sum() / df.loc[x.index, "Units"].sum()),
        YearGPAAverages=("ClassAvgGradePoint", lambda x: (x * df.loc[x.index, "Units"]).sum() / df.loc[x.index, "Units"].sum())
    )

def gpa_per_dept(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Dept", as_index=False).agg(
        DeptGPA=("GradePoints", lambda x: x.sum() / df.loc[x.index, "Units"].sum()),
        DeptGPAAverages=("ClassAvgGradePoint", lambda x: (x * df.loc[x.index, "Units"]).sum() / df.loc[x.index, "Units"].sum())
        ).melt(id_vars="Dept",
           value_vars=["DeptGPA", "DeptGPAAverages"],
           var_name="Type",
           value_name="GPA")

def gpa_by_course_level(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("CourseLevel", as_index=False).agg(
        LevelGPA=("GradePoints", lambda x: x.sum() / df.loc[x.index, "Units"].sum()),
        LevelGPAAverages=("ClassAvgGradePoint", lambda x: (x * df.loc[x.index, "Units"]).sum() / df.loc[x.index, "Units"].sum())
        ).melt(id_vars="CourseLevel",
           value_vars=["LevelGPA", "LevelGPAAverages"],
           var_name="Type",
           value_name="GPA")

def gpa_by_credit_load(df: pd.DataFrame):
    df_term = gpa_per_term(df)
    return df_term.groupby("TotalUnits", as_index=False).agg(CreditLoadGPA=("TermGPA", "mean"))


# Correlation
def get_corr_matrix(df: pd.DataFrame) -> pd.DataFrame:
    renames = {"GradePoint": "My Grades", 
               "CourseLevel": "Course Level",
               "ClassAvgGradePoint": "Class Average Grades"}
    df_ret = df.rename(columns=renames)
    return df_ret[["My Grades", "Units", "Course Level", "Year", "Class Average Grades"]].corr().map(lambda x: x*10)