char_1 = input().lower()
char_2 = input().lower()


def anagram(string1, string2):
    global result

    if len(string1) == len(string2):
        sort1 = ''.join(sorted(string1))
        sort2 = ''.join(sorted(string2))

        if sort1 == sort2:
            result = True
        else:
            result = False
    else:
        result = False

    return result


print(anagram(char_1, char_2))
