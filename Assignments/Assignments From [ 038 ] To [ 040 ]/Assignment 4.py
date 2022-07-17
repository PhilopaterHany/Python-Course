email = input("Enter Your E-mail Address: ").strip()

name = email[:email.index("@")]
service_provider = email[email.index("@") + 1:email.index(".")].lower()
top_level_domain = email[email.index(".") + 1:].lower()

print(f"Your Name Is: {name}")
print(f"Your E-mail Service Provider Is: {service_provider}")
print(f"Your Top Level Domain Is: {top_level_domain}")
