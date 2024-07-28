


''''
	from mediphy.frontiers.trends.monetary.DB_mediphy_trends.connect import connect_to_mediphy_inventory
	[ driver, mediphy_inventory_DB ] = connect_to_mediphy_inventory ()
	collection_treasures = DB_mediphy_trends ["collection_treasures"]
	driver.close ()
"'''



#/
#
from mediphy.frontiers.trends.monetary.moves.URL.retrieve import retreive_monetary_URL
from mediphy._essence import retrieve_essence
#
#
import pymongo
#
#\

def connect_to_mediphy_inventory ():
	essence = retrieve_essence ()
	
	ingredients_DB_name = essence ["trends"] ["monetary"] ["databases"] ["DB_mediphy_trends"] ["alias"]
	monetary_URL = retreive_monetary_URL ()

	driver = pymongo.MongoClient (monetary_URL)

	return [
		driver,
		driver [ ingredients_DB_name ]
	]