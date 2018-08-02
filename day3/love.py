 #string = list of char

 #Bracket notation

# a = 'happy'

# print(a[2]) #p
# print(a[-1]) #y

##############FOR LOOP
# name = "Arcalis Bellanueve"
# result = ""

# for i in range(0, len(name)):
#   # print(name[i])
#   if i % 2 == 0: #every second letter
#     print(name[i])
#     result = result + name[i]
#     print('result just changed to: ' + result)

#############INPUT()
# age = input("What is your age")
# age = int(age)
# print(age)

########RANDOM NUMBER GENERATOR
import random
for x in range(10):
  print(random.randint(1,21)*5),
print()
########RANDOM STRING generator
import string
# import random
def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

print(random_generator())
#'G5G74W'
print(random_generator(3, "6793YUIO"))
# 'Y3U'

## ex 2

min_char = 8
max_char = 12
allchar = string.ascii_letters + string.punctuation + string.digits
password = "".join(random.choice(allchar) for x in range(random.randint(min_char, max_char)))
print("This is your password : ",password)