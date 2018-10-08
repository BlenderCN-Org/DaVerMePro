days = ["Monday", "Tuesday", "Wednesday", "Thurstday", "Friday", "Saturday", "Sunday"]

# a = 0
# while a < days.count():
#     print(days[a])
#     a = a + 1 
for a in range(7):
    print(days[a] + " ist der " + str(a+1) + ". day")

print("########")

for day in days:
    print(day)