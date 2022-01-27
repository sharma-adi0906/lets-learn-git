i = "-"
computer_parts = []
available_parts = ["Computer",
                   "mouse",
                   "Keyboard",
                   "Joystick",
                   "HDMI cable",
                   "USB drive"]

# valid_choices = [str(i) for i in range(1, len(available_parts) +1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

while i != '0':
    if i in valid_choices:

        index = int(i) - 1
        chosen_parts = available_parts[index]
        if chosen_parts in computer_parts:
            computer_parts.remove(chosen_parts)
            print("removing {} from the list".format(i))
        else:
            computer_parts.append(chosen_parts)
            print("adding {} to the list".format(i))
        print("parts in your cart: {}".format(computer_parts))
    elif i == '0':
        print("ok")
        break
    else:
        for part in available_parts:
            print("{0} : {1}".format(available_parts.index(part) + 1, part))
    print("enter the number to add items")
    i = input(int())

print("computer parts to buy are {}".format(computer_parts))
