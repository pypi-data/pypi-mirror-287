




'''
	from mediphy.frontiers.trends.monetary.DB_mediphy_trends.collection_treasures.document.search import search_treasures
	search_treasures ({
		"filter": {
			"nature.identity.FDC ID": ""
		}
	})
'''



#/
#
from mediphy._essence import retrieve_essence
from mediphy.frontiers.trends.monetary.DB_mediphy_trends.connect import connect_to_mediphy_inventory
#
#
import ships.modules.exceptions.parse as parse_exception
#
#
import pymongo
#
#
import time
#
#\



def search_treasures (packet):
	filter = packet ["filter"]

	try:
		[ driver, DB_mediphy_trends ] = connect_to_mediphy_inventory ()
		collection_treasures = DB_mediphy_trends ["collection_treasures"]
	except Exception as E:
		print ("food collection connect:", E)
		
	treasures_roster = []
	try:	
		essence = retrieve_essence ()
		
		print ("filter:", filter)
		
		treasures_roster = []
		treasures = collection_treasures.find (filter)
		for treasure in treasures:
			treasure ["_id"] = str (treasure ["_id"]) 
			
			treasures_roster.append (treasure)
		
	except Exception as E:
		print (parse_exception.now (E))
	
		raise Exception (E)
		pass;
		
	try:
		driver.close ()
	except Exception as E:
		print (parse_exception.now (E))
		print ("food collection disconnect exception:", E)	
		
		
	return treasures_roster;








