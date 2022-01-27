def banner(string=" ", screen_width=80):
    if len(string) > screen_width:
        raise ValueError("string length {0} is more than screen width {1}".format(len(string), screen_width))
    elif string == "*":
        print("*" * screen_width)
    else:
        string_center = string.center(screen_width - 4)
        output_string = "**{0}**".format(string_center)
        print(output_string)


banner("*", 60)
banner("Always look on the light side of life", 60)
banner("If life seems jolly rotten", 60)
banner("There's something you've forgotten", 60)
banner("And that's to laugh and smile and dance and sing", 60)
banner(screen_width=60)
banner("When you're feeling in the dumps", 60)
banner("Don't be silly chumps", 60)
banner("Just purse your lips and whistle, that's the thing", 60)
banner("And", 60)
banner("Always look on the bright side of life", 60)
banner("(Come on)", 60)
banner("Always look on the right side of life", 60)
banner("*", 60)
