
favorite_str = "Hi Mom"
favorite_int = 24601

#print(favorite_str * favorite_int)

#user_name = input("What is your name: ")
#user_age = input("How old are you: ")
#user_age = int(user_age)

#if "we don't indent":
#print("what will happen?")

#if user_age > 17:
#    print("Please Vote")
#    print("register for the selective service")
#    print("go see an R rated movie")
#    print("drive after 9")
#else:
#    print("Please don't skip school")
my_list = []

while True:
    user_in = input("say something: ")
    if user_in == "quit":
        break
    else:
        my_list.append(user_in)

print(my_list)
for item in my_list:
    print(item)
