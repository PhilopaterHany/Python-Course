# ----------------------
# ---  Control Flow  ---
# -- If & Elif & Else --
# --- Make Decisions ---
# ----------------------

u_name = "Osama"
u_country = "Kuwait"
c_name = "Python Course"
c_price = 100

if u_country == "Egypt":
    print(f"Hello {u_name}, Because You Are From {u_country}")
    print(f"The Course \"{c_name}\" Price Is: ${c_price - 80}")
elif u_country == "KSA":
    print(f"Hello {u_name}, Because You Are From {u_country}")
    print(f"The Course \"{c_name}\" Price Is: ${c_price - 60}")
elif u_country == "Kuwait":
    print(f"Hello {u_name}, Because You Are From {u_country}")
    print(f"The Course \"{c_name}\" Price Is: ${c_price - 50}")
else:
    print(f"Hello {u_name}, Because You Are From {u_country}")
    print(f"The Course \"{c_name}\" Price Is: ${c_price - 30}")
