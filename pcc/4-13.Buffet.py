# Buffet
#
# A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
# - Use a for loop to print each food the restaurant offers.
# - Try to modify one of the items, and make sure that Python rejects the change
# - The restaurant changes its menu replacing two of the items with different foods.
#   Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

#premise
buffet = ('bread','pasta','meat','ice-cream','coffee')

#first task
for food in buffet:
    print(food)

#second task
#buffet[1] = 'rice'

#third task
print()
buffet = (buffet[0], 'rice', 'fish', buffet[3], buffet[4])
for food in buffet:
    print(food)

