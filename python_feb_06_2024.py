name1 = "bolaji"
name3 = "chichi"
name2 = "dayo"


print(name1 == name2)
print(name1 == name2)
print(ord('B'))
print("C" in  name3)


print(f'[{name1:10} {name2:10}]')
print(f'[{name1:>10}]')
print(f'[{name1:<10}]')
print(f'[{name1:^10}]')

print(name1 + name2 + name3)
print(f'{name1} + {name2} + {name3}')
        
print(name1 * 5)

sentence =  "welcome to semicolon"
name4 = "   Muhammed   "
print(len(name4))
print(len(name4.strip()))
print(len(name4))
print(name4)
print(name1.upper())
print(name3.lower())
print(name2.capitalize())
print(sentence.title())
print(name2.casefold())
print(sentence.coumt("e"))
print(sentence.rindex("e"))



name = input("enter your name: ").strip()
if name.isalpha():
        print("valid name")
else:
        print("invalid name")
