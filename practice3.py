x = 0
while x <= 5:
    print(x)
    x = x + 1

counties_tuple = ("Arapahoe","Denver","Jefferson")
# Arapahoe
# Denver
# Jefferson

for i in range(len(counties_tuple)):
    print(counties_tuple[i])

# NAme County has number registered voters
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county,voters in counties_dict.items():
    print(county + ' County has ' + str(voters) + ' registered voters')


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]

for county in range(len(voting_data)):

     print(county)


range(len(voting_data))