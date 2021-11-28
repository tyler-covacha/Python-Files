def word_count(s):
    next1 = ""
    prev = ""
    wordcount = 0
    string = s
    s = " " + s
    s = s + " "
    for i in range(len(s)):
        next1 = s[i]
        prev = s[i-1]
        if next1 != " " and prev == " ":
            wordcount += 1
    print(string,"->",wordcount)
    
word_count("hello")
word_count("how are you?")
word_count(" this string has wide spaces ")
word_count(" ")
