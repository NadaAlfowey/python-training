numberofwords=int(input())
for l in range(0,numberofwords):
    word = input()
    if len(word) > 10:
        print(word[0]+str(len(word)-2)+word[-1])
    else:
        print(word)
