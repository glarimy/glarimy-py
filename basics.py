cities = {
    'Tadepalligudem': {
        'Education': [{
            'name': 'Dr. YSR Horticultural University',
            'address': 'Pedatadepalli'
        }, {
            'name': 'National Institute of Technology',
            'address' : 'kadakatla'
        }, {
            'name': 'Vasavi College of Engineering',
            'address': 'Pedatadepalli'
        }, {
            'name': 'Sasi Institute of Technology',
            'address': 'kadakatla'
        }]
    },
    'Manipal': {
        'Education': [{
            'name': 'Kasturba Medical College',
            'address': ''
        }, {
            'name': 'Manipal Institute of Technology',
            'address': ''
        }, {
            'name': 'TA Pai Management Institute',
            'address': ''
        }]
    }
}

def add(city, category, entry):
    if city in cities: 
        if category in cities[city]:
            if not entry in cities[city][category]:
                cities[city][category].append(entry);
        else:
            cities[city][category] = [entry];
    else:
        cities[city] = {
            category: [entry]
        }

def find(city=None, category=None):
    if(city is None):
        return cities.keys();
    else: 
        if(category is not None):
            return cities[city][category];
        else:
            return cities[city].keys();

print ('Welcome to Glarimy Cities');
lcities = find();
lcity = input ('Choose the city: ' + str(list(lcities)));
lcategories = find(lcity);
lcategory = input ('Choose the category: ' + str(list(lcategories)));
lentries = find(lcity, lcategory);
for lentry in lentries:
    print('Name: ', lentry['name']);
    print('Address: ', lentry['address']);
    print();