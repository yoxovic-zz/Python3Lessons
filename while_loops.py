# for i in range(10):
#     print("The number is now {}".format(i))

# i=0
# while i < 10:
#     print("The number is now {}".format(i))
#     i += 1

available_exits = ["east", "west", "northeast"]
chosen_exits = ''
while chosen_exits not in available_exits:
    chosen_exits = input("Please choose your direction: ")
    if chosen_exits == "quit":
        print("Game Over!")
        break
else:
    print("aren't you glad you got out of there")
