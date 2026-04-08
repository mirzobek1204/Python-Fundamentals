print("\n\n=== Gym Class Registration System ===")
print("Enter class level: beginner, intermediate, or advanced")
print("Type 'done' when finished registering\n")

beginner = 12.00
intermediate = 15.00
advanced = 18.00

total = 0.0  

while True:
    level = input("Enter class level: ")

    if level == "done":
        break
    elif level == "beginner":
        total += beginner
        print("Price: $12.00")
    elif level == "intermediate":
        total += intermediate
        print("Price: $15.00")
    elif level == "advanced":
        total += advanced
        print("Price: $18.00")
    else:
        print("Invalid input, please try again.\n")
        continue

    print(f"Current total: ${total:.2f}\n")

print("\n=== Registration Summary ===")

subtotal = total
print(f"Subtotal: ${subtotal:.2f}")

if subtotal >= 60.00:
    discount = 10.00
else:
    discount = 0.00

final_total = subtotal - discount

print(f"Multi-Class Discount: -${discount:.2f}")
print(f"Final Total: ${final_total:.2f}")
print("Thank you for registering!\n\n")
