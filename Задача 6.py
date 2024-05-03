number = 292

if number < 10:
    description = "однозначное число"
elif number < 100:
    description = "двузначное число"
else:
    description = "трехзначное число"

if number % 2 == 0:
    description = "четное " + description
else:
    description = "нечетное " + description

print( description)
