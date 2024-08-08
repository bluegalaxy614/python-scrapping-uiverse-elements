def store_data_to_db(db_collection, document):
    db_collection.insert_one(document)