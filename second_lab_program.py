
classes_taken = []
number_of_classes = input("How many classes are you taking this semester: ")
total_number_of_classes = int(number_of_classes)
number_of_classes = int(number_of_classes)

while total_number_of_classes > 0:
    add_class = input("Please write the class you are taking this semester: ")
    classes_taken += add_class
    total_number_of_classes -= 1

while number_of_classes > 0:
    print(f"{classes_taken}\n")
    number_of_classes -= 1
