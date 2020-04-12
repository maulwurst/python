guest_list = ["John Cleese", "Albert Einstein", "Larry David"]
message_to_list = "You are invited"
cant_come = "John Cleese"
still_invited = "You are still invited"

guest_list.remove(cant_come)
print(message_to_list,guest_list)
guest_list.insert(0,"Max")
guest_list.insert(2,"Fug")
guest_list.insert(4,"Me")

guest_list.pop(4)
guest_list.pop(2)


print(sorted(guest_list),still_invited)
print(len(guest_list))
