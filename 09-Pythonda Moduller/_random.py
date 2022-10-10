import random

# result = dir(random)
# result = help(random)

result = random.random()  # 0.0 - 1.0
result = random.random() * 100 
result = random.uniform(1,10)
result = random.randint(1,10)

greeting = 'Hello There'
names = ['Ali','Yağmur','Cenk','Deniz','Ahmet','Efe']
# result = names[random.randint(0,len(names))]

result = random.choice(names)
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)
result = liste

liste = range(100)
result = random.sample(liste, 3)
result = random.sample(names, 2)

print(result)