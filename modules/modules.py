from bootstrap import directory

print ('Welcome to Glarimy Cities');
cities = directory.getCities();
city = input ('Choose the city: ' + str(cities));
categories = directory.getCity(city).getCategories();
category = input ('Choose the category: ' + str(categories));
entries = directory.getCity(city).getCategory(category).getEntries();
for entry in entries:
    print('Name: ', entries[entry].name);
    print('Address: ', entries[entry].address);
    print();