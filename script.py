# Лабораторна №2 Варіант №2
def get_string():
    entered_string = input("Enter a string:").strip()

    if len(entered_string) == 0:
        print("   Ooops... Your string is empty. Try again")
        return get_string()
    else:
        return entered_string


string = get_string()

splitted = string.split(" ")

words = []
for v in splitted:
    word = v.strip()
    if word != "":
        words.append(word)

symbols = 0
for v in words:
    symbols += len(v)

words_number = len(words)    


if words_number == 1:
    print("There is only one word")
else:
    print("There are " + str(words_number) + " words")
    
if symbols == 1:
    print("There is only one symbol")
else:
    print("There are " + str(symbols) + " symbols")