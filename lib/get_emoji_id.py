def get_emoji_id(emoji):
    num = "0123456789"

    if emoji[0] == "<" and emoji[3] not in num:
        id_start = 3
    else:
        id_start = 0

    while emoji[id_start] != ":":
        print(emoji[id_start])
        id_start += 1
    id_start += 1

    print(emoji[id_start:-1])
    return emoji[id_start:-1]
