




''''
	mediphy treasures send --name "treasure.1" --version 1.0.0
"'''

''''
	objective:
		stow_treasure ({
			"domain": "treasure.1",
			"version": "1.0.0",
			"path": ""
		})
	
		the procedure:
			[ ] search the treasures
"'''

''''
	DB: mediphy_trends_DB
		collection: treasures_collection
"'''


#/
#
from mediphy.frontiers.treasures._quests.itemize import itemize_treasures
from mediphy.frontiers.treasures.check.domain_fiber import check_domain_fiber
#
#
from mediphy._essence import retrieve_essence
#
#\

def pass_treasure (packet):
	essence = retrieve_essence ()

	domain = packet ["domain"]
	version = packet ["version"] 
	path = packet ["path"] 
	
	treasures = itemize_treasures ()
	
	check_domain_fiber ({
		"domain_fiber": domain
	})
	
	
	
	
	
	
	
	
	
	return;