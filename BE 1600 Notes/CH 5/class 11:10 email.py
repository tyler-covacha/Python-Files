emails = {}

f = open("email.txt",'r')
for line in f:
    line = line.split()
    emails[line[0]] = line[1]
f.close()
name = input("Enter name")
email = input("Enter email")
emails[name] = email
print(emails)

f = open("email.txt",'w')
for key,value in emails.items():
    f.write(key+ " " + value + '\n')
    f.write("")

f.close()
w
