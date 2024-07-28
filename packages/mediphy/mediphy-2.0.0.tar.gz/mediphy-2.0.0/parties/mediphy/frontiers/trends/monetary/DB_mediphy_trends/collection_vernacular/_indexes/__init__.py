

''''
	from mediphy.frontiers.trends.monetary.DB_mediphy_trends.collection_vernacular._indexes import prepare_collection_vernacular_indexes
	prepare_collection_vernacular_indexes ()
"'''

#/
#
from mediphy.frontiers.trends.monetary.DB_mediphy_trends.collection_vernacular.document.insert import insert_document
from mediphy.frontiers.trends.monetary.DB_mediphy_trends.connect import connect_to_mediphy_inventory
#
#\

def prepare_collection_vernacular_indexes ():
	print ("prepare_collection_vernacular_indexes")

	[ driver, DB_mediphy_trends ] = connect_to_mediphy_inventory ()
	collection_vernacular = DB_mediphy_trends ["collection_vernacular"]
	
	collection_vernacular.create_index([('domain', 1)], unique=True)
	
	driver.close ()