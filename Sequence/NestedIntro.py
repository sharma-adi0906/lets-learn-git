meal_list = [
    ["egg", "bacon", "bread"],
    ["egg", "bacon", "spam"],
    ["egg", "egg plant", "spam", "potato", "spam"],
    ["egg plant", "egg", "bacon"],
    ["egg plant", "potato", "bacon"],
    ["potato", "spam", "spam", "bacon", "spam"],
]

for meal in meal_list:
    if "spam" not in meal:
        print(meal)
        # for item in meal:
        #     print(item)
    else:
        print("{0} has spam count {1} times".format(meal, meal.count("spam")))
