import string
import random
letters = string.ascii_lowercase
print("yahoo"'\n'
      "gmail"'\n'
      "aol"'\n'
      "write any domail")
email = input("domain : ")
done = 0
li = 0
lst = open("email.txt", "w")
ranges = int(input("email characters range : "))
while li == 0:
    lst.write( ''.join(random.choice(letters) for i in range(ranges))+f'@{email}.com'+'\n')
    done += 1
    print(done)
