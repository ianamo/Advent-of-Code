
for x in nums:
	for y in nums:
		if not x == y or (x + y) > 2020:
			diff = 2020 - (x + y)
			if diff in nums:
				print(x)
				print(y)
				print(diff)
				print(x * y * diff)
