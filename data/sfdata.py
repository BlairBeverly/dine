import urllib
import zipfile
import csv
import mysqlconnection
import sqlalchemy

db = mysqlconnection.MySQLConnector('teamdb')


# Get the zipped SF food inspection data from the url
zipped, headers = urllib.urlretrieve(
    'https://extxfer.sfdph.org/food/SFFoodProgram_Complete_Data.zip')

# There are three files zipped up- one for violations, businesses and
# inspections. Iterate through each and store the data for each 
# into lists of dictionaries. One dictionary per row of data.
with zipfile.ZipFile(zipped, 'r') as myzip:
    for file in myzip.namelist():
        unzippedfile = myzip.open(file)

        if file == 'violations_plus.csv':
            violations = []
            csvReader = csv.reader(unzippedfile)

            # skip header
            csvReader.next()

            for row in csvReader:
                violations_dict = {}
                (restaurant_id, date, violation_id, violation_severity, description) = row
                violations_dict['restaurant_id'] = restaurant_id
                violations_dict['date'] = date
                violations_dict['violation_severity'] = violation_severity
                violations_dict['description'] = description
        
                violations.append(violations_dict)


        if file == 'businesses_plus.csv':
            csvReader = csv.reader(unzippedfile)
            header = csvReader.next()
            businesses = []
            for row in csvReader:
                business_dict = {}
                business_dict['restaurant_id'] = row[header.index('business_id')]
                business_dict['name'] = row[header.index('name')]
                business_dict['address'] = row[header.index('address')]
                business_dict['city'] = row[header.index('city')]
                business_dict['zipcode'] = row[header.index('postal_code')]
                business_dict['latitude'] = row[header.index('latitude')]
                business_dict['longitude'] = row[header.index('longitude')]
                business_dict['phone_number'] = row[header.index('phone_number')]
                business_dict['owner_name'] = row[header.index('owner_name')]

                businesses.append(business_dict)


        if file == 'inspections_plus.csv':
            inspections = []
            csvReader = csv.reader(unzippedfile)

            # skip header
            csvReader.next()

            for row in csvReader:
                inspection_dict = {}
                (restaurant_id, score, date, complaint_type) = row
                inspection_dict['restaurant_id'] = restaurant_id
                inspection_dict['score'] = score
                inspection_dict['date'] = date
                inspection_dict['complaint_type'] = complaint_type
        
                inspections.append(inspection_dict)

# Given a violation dict, upload the row to the violations table
def add_violation(violation):
    query = "INSERT INTO violations (date, risk_category, description, "\
            "created_at, updated_at, restaurant_id) VALUES (:date, "\
            ":risk_category, :description, NOW(), NOW(), :restaurant_id)"

    data = {'restaurant_id': violation['restaurant_id'],
            'date': violation['date'],
            'risk_category': violation['violation_severity'],
            'description': violation['description']}

    try:
        db.query_db(query, data)

    except sqlalchemy.exc.IntegrityError:
        print "some error occurred with id: {}".format(data['restaurant_id'])

# Given a business dict, upload the row to the businesses table
def add_business(business):
    query = "INSERT INTO restaurants (id, name, address, city, state, "\
            "postal_code, latitude, longitude, phone_number, owner_name, "\
            "created_at, updated_at) VALUES (:id, :name, :address, :city, "\
            ":state, :postal_code, :latitude, :longitude, :phone_number, "\
            ":owner_name, NOW(), NOW())"

    data = {'id': business['restaurant_id'],
            'name': business['name'],
            'address': business['address'],
            'city': business['city'],
            'state': 'CA',
            'postal_code': business['zipcode'],
            'latitude': business['latitude'],
            'longitude': business['longitude'],
            'phone_number': business['phone_number'],
            'owner_name': business['owner_name']}

    try:
        db.query_db(query, data)

    except sqlalchemy.exc.IntegrityError:
        print "there was an error writing this restaurant id: {}".format(data['id'])

# Given a inspection dict, upload the row to the inspections table
def add_inspection(inspection):
    query = "INSERT INTO inspections (restaurant_id, score, date, type, "\
            "created_at, updated_at) VALUES (:restaurant_id, :score, :date, "\
            ":type, NOW(), NOW())"

    data = {'restaurant_id': inspection['restaurant_id'],
            'score': inspection['score'],
            'date': inspection['date'],
            'type': inspection['complaint_type']}

    try:
        db.query_db(query, data)

    except sqlalchemy.exc.IntegrityError:
        print "some error occurred with id: {}".format(data['restaurant_id'])

# Given a list of violation dicts, add only the rows that aren't already
# present within the violations table.
def add_new_violations():
    max_date = db.query_db("SELECT MAX(date) as max FROM violations")[0]['max']

    for violation in violations:
        if int(violation['date']) > int(max_date):
            add_violation(violation)

# Given a list of business dicts, add only the rows that aren't already
# present within the businesses table.
def add_new_businesses():
    max_id = db.query_db("SELECT MAX(id) as max FROM restaurants")[0]['max']

    for business in businesses:
        if int(business['restaurant_id']) > int(max_id):
            add_business(business)

# Given a list of inspection dicts, add only the rows that aren't already
# present within the inspections table.
def add_new_inspections():
    max_date = db.query_db("SELECT MAX(date) as max FROM inspections")[0]['max']

    for inspection in inspections:
        if int(inspection['date']) > int(max_date):
            add_inspection(inspection)

# Write all the data from SF URL to the database
def refresh_entire_dataset():
    for business in businesses:
        add_business(business)
    for inspection in inspections:
        add_inspection(inspection)
    for violation in violations:
        add_violation(violation)



add_new_violations()
add_new_businesses()
add_new_inspections()

#refresh_entire_dataset()












