from datetime import datetime as dt
bday = dt(2022, 8, 4)

print(bday.date())  # Output => "2022-08-04"
print(bday.strftime("%b %d,%Y"))  # Output => "Aug 04, 2022"
print(bday.strftime("%d - %b - %Y"))  # Output => "04 - Aug - 2022"
print(bday.strftime("%d / %b / %y"))  # Output => "04 / Aug / 22"
print(bday.strftime("%d / %B / %Y"))  # Output => 04 / August / 2022
print(bday.strftime("%a, %d %B %Y"))  # Output => "Thu, 04 August 2022"
