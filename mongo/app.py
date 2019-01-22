from db import MongoRepository

repo = MongoRepository()

try:

    repo.addEntry('Kolar', {
        'category': 'Spiritual',
        'section' : 'Temples',
        'name' : 'Anjaneya Swamy Gudi',
        'address' : 'KN Raod, Near Fire Station, Tadepalligudem - 534101, West Godavari Dt, Andhra Pradesh, India'
    });

    print (repo.getCities());
    print (repo.getCategories('Tadepalligudem'));
    print (repo.getSections('Tadepalligudem', 'Temples'));
    for entry in repo.getEntries('Tadepalligudem', 'Health', 'Pharmacy'):
        print (entry['name'])
        print (entry['address'])
except Exception as e:
    print (e)