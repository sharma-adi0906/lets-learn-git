from nested_data import albums

while True:
    for index, value in enumerate(albums):
        print(index + 1, value[0])
    choice = int(input("Please select the album (invalid choices exist)\t"))
    print()
    if 1 <= choice <= len(albums):
        song_list = albums[choice - 1][3]
        for index,song in enumerate(song_list):
            print(index + 1, song[1])
        print()
        print("Choose the song number from above: ")
        song_no = int(input())
        if 1 <= song_no <= len(song_list):
            print("playing: {}".format(song_list[song_no - 1][1]))
            print("=" * 400)
        else:
            continue
    else:
        continue
    break