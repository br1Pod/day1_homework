# print("Stop! /n Who would cross the Bridge of Death must answer me these questions three, /n ere the other side he see",)
# cannot get the print to print line breaks? Have commented out and will research further.


print("Stop!")
print("Who would cross the Bridge of Death must answer me these questions three,")
print("ere the other side he see  ")

name = input("What is your name? ")
quest = input("What is your quest? ")
colour = input("What is your favourite colour? ")

if colour == "blue":
    print("Right then.., off you go")
    print("***", name, "crosses the bridge safely, and continues to", quest, "***")
else:
    print(name, "is cast into the Gorge of Eternal Peril!")
