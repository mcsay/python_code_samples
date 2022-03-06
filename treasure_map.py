row1= ["🔳️", "🔳", "🔳"]
row2= ["🔳", "🔳", "🔳"]
row3= ["🔳", "🔳", "🔳"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0]) #2
vertical = int(position[1]) #3

map[vertical -1][horizontal -1] = "X"

#selected_row = map[vertical -1] --> This two line same with above code
#selected_row[horizontal -1] = "X"


print(f"{row1}\n{row2}\n{row3}")