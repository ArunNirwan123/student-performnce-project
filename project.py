# import pandas as pd


# def read_file():
#     attendance=pd.read_csv("attendance.csv")
#     courses=pd.read_csv("courses.csv")
#     marks=pd.read_csv("marks.csv")
#     payments=pd.read_csv("payments.csv")
#     students=pd.read_csv("students.csv")
#     trainers=pd.read_csv("trainers.csv")
   
#     return attendance,courses,marks,payments,students,trainers
# attendance,courses,marks,payments,students,trainers=read_file()

# from sqlalchemy import create_engine
# from urllib.parse import quote_plus

# engine=create_engine(f"mysql+pymysql://root:@localhost:3306/Nirwan")

# payments.to_sql(name="payment_status",con=engine,if_exists="replace",index=False)


# print(attendance.shape)
# print(courses.shape)
# print(marks.shape)
# print(payments.shape)
# print(students.shape)
# print(trainers.shape)


# print(attendance.columns)
# print(courses.columns)
# print(marks.columns)
# print(payments.columns)
# print(students.columns)
# print(trainers.columns)

# print(attendance.isnull().sum())
# print(courses.isnull().sum())
# print(marks.isnull().sum())
# print(payments.isnull().sum())
# print(students.isnull().sum())
# print(trainers.isnull().sum())

# print(attendance.duplicated().sum())
# print(courses.duplicated().sum())
# print(marks.duplicated().sum())
# print(payments.duplicated().sum())
# print(students.duplicated().sum())
# print(trainers.duplicated().sum())


# merger = pd.merge(students, courses, on="course_id", how="inner")
# print(merger)

