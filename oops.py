class Entry:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Category: 
    def __init__(self, name):
        self.__name = name
        self.__entries = dict()
    def getName(self): 
        return self.__name
    def addEntry(self, entry):
        self.__entries[entry.name] = entry
    def getEntries(self):
        return self.__entries

class City: 
    def __init__(self, name):
        self.__name = name;
        self.__categories = dict()
    def getName(self):
        return self.__name
    def addCategory(self, name):
        self.__categories[name]= Category(name)
    def getCategory(self, name):
        return self.__categories[name]
    def getCategories(self):
        return list(self.__categories.keys())
    def addEntry(category, entry):
        self.__categories[category].add(entry)

class Directory :
    def __init__(self):
        self.__cities = dict()
    def addCity(self, name):
        self.__cities[name] = City(name)
    def addCategory(self, city, name):
        self.__cities[city].addCategory(name)
    def addEntry(self, city, category, entry):
        self.__cities[city].getCategory(category).addEntry(entry)
    def getCities(self):
        return list(self.__cities.keys())
    def getCity(self, name):
        return self.__cities[name]
    

directory = Directory();
directory.addCity('Tadepalligudem');
directory.addCategory('Tadepalligudem', 'Education');
directory.addEntry('Tadepalligudem', 'Education', Entry('Dr. YSR Horticultural University', 'Pedatadepalli'));
directory.addEntry('Tadepalligudem', 'Education', Entry('National Institute of Technology', 'kadakatla'));
directory.addEntry('Tadepalligudem', 'Education', Entry('Vasavi College of Engineering', 'Pedatadepalli'));
directory.addEntry('Tadepalligudem', 'Education', Entry('Sasi Institute of Technology', 'kadakatla'));
directory.addCity('Manipal');
directory.addCategory('Manipal', 'Education');
directory.addEntry('Manipal', 'Education', Entry('Kasturba Medical College', ''));
directory.addEntry('Manipal', 'Education', Entry('Manipal Institute of Technology', ''));
directory.addEntry('Manipal', 'Education', Entry('TA Pai Management Institute', ''));

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