# import pandas as pd
# marks=pd.read_csv("marks.csv")


# avg_marks = marks.set_index("student_id").mean(axis=1).reset_index(name="average_marks")

# print(avg_marks)


# sorted_students =avg_marks.sort_values("average_marks", ascending=False)

# print(sorted_students)

# students = marks[avg_marks["average_marks"] >= 80]

# print(students)

# avg_marks["performance"] = avg_marks["average_marks"].apply(
#     lambda x: "Excellent" if x >= 85
#     else "Good" if x >= 70
#     else "Needs Improvement"
# )

# print(marks)


# from sqlalchemy import create_engine
# from urllib.parse import quote_plus

# engine=create_engine(f"mysql+pymysql://root:@localhost:3306/Nirwan")

# marks.to_sql(name="avg_total",con=engine,if_exists="replace",index=False)