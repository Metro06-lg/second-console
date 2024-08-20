print("welcome to  Mr AI whole day's restaurant\n")
print("i will be your management system today\n")
print("In here we serve you from the morning to the evening\n")
print("A menu will be provided shortly\n")


name = input("can kindly give me your name? ")

answer = input(name + " would like to enjoy :"
                      " (breakfast),(launch) or (supper)? ").lower()

if answer == "yes" or "":
    print(name +" thanks you made the right choice,\n"
                " we have a hostel for you to relax if"
                " you want to realy enjoy your self :)")

else:
    print(name + " :(  i am sorry but i have to ask you to live this building")

print("moving on to the menu we have\n")
print("we have as follows for breakfast\n")

breakfast = ["Tea with bread and egg",
             " coffe with french bread",
             " salad with bread",
             " black coffe",
             " pri fried egg with pie and milk",
             " milk with cookies"]
print(breakfast)
print("\n")
print("NB : in order to select the food,>>> type in the exact thing you see in the menu")
choice = input("from the above select your choice: ").lower()

print("your " + choice + ' will ready in a minute\n')

print("pleas go and have fan to make space for the next round\n")


print("it's time for lunch")
lunch = ["stew with rice and egg",
             " beef stew with banku",
             " salad with jollof and chicken",
             " banku with green peper",
             " fried rice with beef"
             " fufu with goat meat"]
print(lunch)
next_choice = input("from the above select your choice: ")

print("your " + next_choice + 'WILL ready in a minute\n').lower()

print("it's time for supper")
snucks = ["chips",
             " ice cream",
             " pork",
             " potato chips",
             " cork tile",
             " coca cola"]
print(snucks)
answer = input("from the above select your choice: ")

print("your " + answer + 'WILL ready in a minute\n').lower()


supper = ["hot soup with chicken",
             " tea with short cake",
             " plantain with egg stew",
             " scrambled eggs",
             " cake with a soft drink",
             " porage with chocolate bread"]
print(supper)
last = input("from the above select your choice: ")

print("your " + last + 'WILL ready in a minute\n').lower()

print("ok so all will cost 1289$$")
print("thank you and have a nice day")
