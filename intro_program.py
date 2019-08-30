current_month = "august"
name = input("What is your name?: ")
birth_month = input("What month were you born in?: ")
name_length = len(name)

print(f"Hello {name}!")
if birth_month == current_month:
    print(f"Happy birthday {name}!")
else:
    print(f"You birthday month is in {birth_month} ")
print(f"You have {name_length} letters in your name")
