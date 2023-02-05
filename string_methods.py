text = "THERE is A MaN and HE lOves goBBLIN SOME pie"

print(text.count('e'))
print(text.upper())
print(text.lower())
print(text.capitalize())
print("Is x lowercase? ", text.islower())
print("Is test just letters? ",text.isalpha())
print(text.casefold())
print(text.title())
print(text.find("HE"))

x = '22222hi 2232hello22222 grasilis 23222222'
print(x.rstrip('2'))
print(x.lstrip('2'))
print(x.strip('2'))
print(x.strip())

name = input("yo dawg I dare you to type spaces").strip()
print(name)