string = "alan curke benjamin"
name = string.split()
result = ""

for item in name:
	if(name.index(item) > 0):
		item = item.capitalize()
		result = result+" "+item
	else:
		item = item.capitalize()
		result = item

print(result)
