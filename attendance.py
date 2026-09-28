# import pandas as pd

# attendance = pd.read_csv("attendance.csv")


# attendance["attendance_percentage"] = (
#     attendance["attended_classes"] / attendance["total_classes"]
# ) * 100


# attendance["attendance_status"] = attendance["attendance_percentage"].apply(
#     lambda x: "Good" if x >= 75 else "Low"
# )

# print(attendance)


# from sqlalchemy import create_engine
# from urllib.parse import quote_plus

# engine=create_engine(f"mysql+pymysql://root:@localhost:3306/Nirwan")

# attendance.to_sql(name="total_attendance",con=engine,if_exists="replace",index=False)

