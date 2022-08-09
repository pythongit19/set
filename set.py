sea_animals = {'shark', 'whale', 'seal'}
for animal in sea_animals :
    print(animal)

sea_animals.add("sea lion")
print(sea_animals)

sea_animals.update(["tuna"])
print(sea_animals)

print(len(sea_animals))

sea_animals.add('orca')
print(sea_animals)

sea_animals.discard('tuna')
print(sea_animals)

sea_animals.pop()
print(sea_animals)

sea_animals.pop()
print(sea_animals)


sea_animals.pop()
print(sea_animals)