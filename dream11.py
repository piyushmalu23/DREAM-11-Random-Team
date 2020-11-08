import random

NUM_WKT = 4
NUM_BAT = 6
NUM_ALL = 3
NUM_BOWL = 9

wkt = []
bat = []
_all = []
bowl = []
total = 0


# Add a wicket keeper
wkt.append(random.randint(1, NUM_WKT))
total = total + 1

# Add three batsmen
while total < 4:
	r = random.randint(1, NUM_BAT)
	if r not in bat:
		total = total + 1
		bat.append(r)


# Add an all rounder
_all.append(random.randint(1, NUM_ALL))
total = total + 1

# Add three bowlers
while total < 8:
	r = random.randint(1, NUM_BOWL)
	if r not in bowl:
		total = total + 1
		bowl.append(r)

while total < 11:
	r = random.randint(1, 4)
	if r == 1:
		r = random.randint(1, NUM_WKT)
		if r not in wkt:
			total += 1
			wkt.append(r)
	elif r == 2:
		r = random.randint(1, NUM_BAT)
		if r not in bat:
			total = total + 1
			bat.append(r)
	elif r == 3:
		r = random.randint(1, NUM_ALL)
		if r not in _all:
			total += 1
			_all.append(r)
	else:
		r = random.randint(1, NUM_BOWL)
		if r not in bowl:
			total = total + 1
			bowl.append(r)



print("WKT: " + str(sorted(wkt)))
print("BAT: " + str(sorted(bat)))
print("ALL: " + str(sorted(_all)))
print("BOWL: " + str(sorted(bowl)))

print(random.sample(range(1, 12), 2))
