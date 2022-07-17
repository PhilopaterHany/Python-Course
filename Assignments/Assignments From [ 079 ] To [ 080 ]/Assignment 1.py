from datetime import datetime
my_date = datetime(2021, 6, 25).date()
today = datetime.now().date()
date_diff = str(today - my_date)
print(f"The Date is {my_date}")
print(f"Today's Date Is {today}")
print(f"Days Difference From {my_date} To {today} Is => {(today - my_date).days} Days.")

# Output => Days Difference From 2021-06-25 To 2022-07-14 Is => 384 Days.
