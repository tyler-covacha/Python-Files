def repl(string,numberOfRepetitions):
    string1 = ""
    for i in range(numberOfRepetitions):
        string1 = string1 + string
    print(string,"->",string1)

#sample output
repl('hello',3)

#if number of repetitions is zero or less
repl('hello',-1)
repl('hello',0)
