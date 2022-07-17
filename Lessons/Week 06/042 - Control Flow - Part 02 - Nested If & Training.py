# ---------------
# -- Nested If --
# ---------------

u_name = "Osama"
is_student = "Yes"
u_country = "Egypt"
c_name = "Python Course"
c_price = 100

if u_country == "Egypt" or u_country == "KSA" or u_country == "Qatar":
    if is_student == "Yes":
        print(f"Hi {u_name}, Because You Are From {u_country} And You Are A Student")
        print(f"The Course \"{c_name}\" Price Is: ${c_price - 90}")
    else:
        print(f"Hi {u_name}, Because You Are From {u_country}")
        print(f"The Course \"{c_name}\" Price Is: ${c_price - 80}")
elif u_country == "Kuwait" or u_country == "Bahrain":
    print(f"Hi {u_name}, Because You Are From {u_country}")
    print(f"The Course \"{c_name}\" Price Is: ${c_price - 50}")
else:
    print(f"Hi {u_name}, Because You Are From {u_country}")
    print(f"The Course \"{c_name}\" Price Is: ${c_price - 30}")
