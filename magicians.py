def show_magicians(names[:],title):
   while names:
       made_great = names.pop()
       
       print('making ' + made_great + ' great!')
       title.append(made_great)

def show_great_magicians(title):
    print("\nIs made great:")
    for make_great in title:
        print(make_great)

names = ['a','b','c']
title = []
show_magicians(names,title)
show_great_magicians(title)
