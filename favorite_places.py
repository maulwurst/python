places_to_go = ["Kerela","Buenes Aires","Barcelona","Uruguay","London"]
print(places_to_go)
print("Original list")

print(sorted(places_to_go))
print("sorted but order not changed")


places_to_go.reverse()
print(places_to_go)
print("temporary reverse index order")

places_to_go.sort()
print(places_to_go)
print("sorted alphabetically")

places_to_go.sort(reverse=True)
print(places_to_go)
print("sorted reverse alphabetically")
