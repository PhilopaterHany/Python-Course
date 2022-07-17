# -----------------------------
# -- Practical - Slice Email --
# -----------------------------

the_name = input("Write Your Name: ").strip().capitalize()
the_email = input("Write Your E-mail Address: ").strip()

the_username = the_email[:the_email.index("@")]
service_provider = the_email[the_email.index("@") + 1:]

print(f"Hello {the_name}, Your Email Is: {the_email}")
print(f"Your Username Is {the_username} \nYour E-mail Service Provider Is {service_provider}")

# email = "osama@elzero.org"
# print(email[:email.index("@")])
