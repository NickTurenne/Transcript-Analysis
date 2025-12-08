import pandas as pd

LETTER_GRADES_TO_GPA_SFU = {
    "A+": 4.33, "A": 4.0, "A-": 3.67,
    "B+": 3.33, "B": 3.0, "B-": 2.67,
    "C+": 2.33, "C": 2.0, "C-": 1.67,
    "D": 1.0, "F": 0.0, "FD": 0.0,
    "N": 0.0, "P": 0.0
}

def clean(df: pd.DataFrame) -> pd.DataFrame:
    df["GradePoint"] = df["Grade"].apply(convert_grade_to_GPA)
    df["ClassAvgGradePoint"] = df["ClassAverage"].apply(convert_grade_to_GPA)
    df["Year"] = df["Term"].apply(convert_term_to_year)
    df["Dept"] = df["Course"].apply(convert_course_to_dept)
    df["CourseLevel"] = df["Course"].apply(convert_coures_to_level)
    df["Season"] = df["Term"].apply(convert_term_to_season)
    return df

def drop_non_GPA_courses(df: pd.DataFrame) -> pd.DataFrame:
     # Pass/fail courses do not count to GPA, EXCM means repeated and excluded
     return df[(df["Grade"] != "P") & (df["Repeated"] != "EXCM")]

def convert_grade_to_GPA(grade: str) -> int:
    grade_stripped = grade.strip()
    if LETTER_GRADES_TO_GPA_SFU.__contains__(grade_stripped):
        return LETTER_GRADES_TO_GPA_SFU[grade_stripped]
    else:
        return 0.0
    
def convert_term_to_year(term: str) -> int:
        year = term.split()[0]
        return int(year)

def convert_course_to_dept(course: str) -> str:
     dept = course.split()[0]
     return dept

def convert_coures_to_level(course: str) -> int:
     level = course.split()[1]
     match level[0]:
          case "1":
               return 100
          case "2":
               return 200
          case "3":
               return 300
          case "4":
               return 400
          case _:
               return 0
          
def convert_term_to_season(course: str) -> str:
     season = course.split()[1]
     return season