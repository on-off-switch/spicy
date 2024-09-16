import random
rickroll = random.randint(0, 999)
randominte = random.randint(0,9)
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '•', '+', '=', '*', '^', '%', '@', '!', '-', '_', '+', '|', '/', '?', '¿', '`', '~', '.']
list = []
if rickroll == 2:
  list = ['Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you'] 
else:
  for counter in range(random.randint(10, 20)):
    randominte = random.randint(0,9)
    list.append(randominte)
    e = random.choice(characters)
    list.append(e)
  egg = list
print(*list, sep = '')
