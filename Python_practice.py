# message = "Hello World"
# print(message)
counties = ['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
# counties.insert(2,"El Paso")
counties.insert(1,"El Paso")
counties.remove("Arapahoe")
counties.insert(1,"Jefferson")
my_tuple = ("Arapahoe","Denver","Jefferson")
#print(my_tuple[:2])

counties_dict = {}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
#print(counties_dict)
print(counties_dict[('Arapahoe')])