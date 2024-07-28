

''''
	from mediphy.frontiers.trends.monetary.DB_mediphy_trends.collection_treasures._indexes import prepare_collection_treasures_indexes
	prepare_collection_treasures_indexes ()
"'''

#/
#
from mediphy.frontiers.trends.monetary.DB_mediphy_trends.collection_treasures.document.insert import insert_document
from mediphy.frontiers.trends.monetary.DB_mediphy_trends.connect import connect_to_mediphy_inventory
#
#\

def prepare_collection_treasures_indexes ():
	print ("prepare_collection_treasures_indexes")

	[ driver, DB_mediphy_trends ] = connect_to_mediphy_inventory ()
	collection_treasures = DB_mediphy_trends ["collection_treasures"]
	
	collection_treasures.create_index([('domain', 1)], unique=True)
	
	driver.close ()