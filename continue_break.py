# shopping_list = ["milk", "pasta", "egg", "spam", "bread", "rice"]
shopping_list = ["milk", "pasta", "egg", "tomato", "bread", "rice"]
# for item in shopping_list:
#     if item is "spam":
#         continue
#     print("Buy " + item)

# for item in shopping_list:
#     if item is "spam":
#         break
#     print("Buy " + item)

for item in shopping_list:
    if item is "spam":
        break
    print("Buy " + item)
else:
    print("I'll have this with that!")