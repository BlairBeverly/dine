import mysqlconnection
import datahelper
import twilio_helper

SF_DATA_URL = 'https://extxfer.sfdph.org/food/SFFoodProgram_Complete_Data.zip'
DATABASE = 'teamdb'


db = mysqlconnection.MySQLConnector(DATABASE)
datahelper = datahelper.Helper(db)
businesses, inspections = datahelper.get_data(SF_DATA_URL)

datahelper.add_new_businesses(businesses)
new_inspections = datahelper.add_new_inspections(inspections)

if new_inspections:

    query = "SELECT user_id, name AS restaurant_name, restaurant_id, phone "\
            "AS user_phone, email AS user_email FROM favorites f JOIN "\
            "restaurants r ON f.restaurant_id = r.id JOIN users u ON "\
            "f.user_id = u.id"

    favorites = db.query_db(query)

    for inspection in new_inspections:
        if inspection['score'] != '':
            if int(inspection['score']) < 71:
                for favorite in favorites:
                    if int(inspection['restaurant_id']) == int(favorite['restaurant_id']):
                        twilio_helper.send_alert(
                            favorite['restaurant_name'],
                            favorite['user_phone'])



#datahelper.refresh_entire_dataset()












