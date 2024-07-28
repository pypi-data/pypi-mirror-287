
#/
#
from mediphy._clique import clique
from mediphy.frontiers.trends.monetary.DB_mediphy_trends.collection_vernacular._indexes import prepare_collection_vernacular_indexes
#
#
import rich
#
#
import pathlib
import inspect
import os
from os.path import dirname, join, normpath
#
#\

# prepare_collection_vernacular_indexes ()

configured = False


def is_configured ():
	return configured

def start ():

	return;

	mediphy_config = config_scan.start ()
	if (mediphy_config == False): 
		#print ("mediphy_config == False")
		
		print ("The config was not found; exiting.")
		print ()
		
		exit ();
		
		return;

	print ()
	print ("configuring")
	print ()
	
	print ('merging config', mediphy_config)
	mediphy_essence.merge_config (mediphy_config ["configuration"])
	
	
	rich.print_json (data = mediphy_essence.essence)
	rich.print_json (data = mediphy_essence.essence)
	
	
	return;


	'''
	rich.print_json (data = {
		"mediphy_config": mediphy_config
	})
	'''
	
	'''
	mediphy_essence.change ("mongo", {
		"directory": ""
	})
	'''
	
	'''
		get the absolute paths
	'''
	'''
	mediphy_config ["configuration"] ["treasuries"] ["path"] = (
		normpath (join (
			mediphy_config ["directory_path"], 
			mediphy_config ["configuration"] ["treasuries"] ["path"]
		))
	)
	'''
	
	
	'''
		paths:
			trends
				mongo_data_1
	
	
		mongo:
			safety
				passes
				zips
				zips.files
	'''
	trends_path = normpath (join (
		mediphy_config ["directory_path"], 
		mediphy_config ["configuration"] ["trends"] ["path"]
	))
	edited_config = {
		"mints": {
			"path": normpath (join (
				mediphy_config ["directory_path"], 
				mediphy_config ["configuration"] ["mints"] ["path"]
			))
		},
		"trends": {
			"path": trends_path,
			
			"nodes": [{
				"host": "localhost",
				"port": "27017",
				"data path": normpath (join (
					trends_path, 
					"mongo_data_1"
				))
			}]
		},
		"CWD": mediphy_config ["directory_path"]
	}
	
	'''
	config_template = {
		
	}
	'''
	
	rich.print_json (data = {
		"edited_config": edited_config
	})

	
	mediphy_essence.change ("edited_config", edited_config)
	

	#print ('mediphy configuration', mediphy_config.configuration)

	'''
		Add the changed version of the basal config
		to the essence.
	'''
	'''
	config = mediphy_config ["configuration"];
	for field in config: 
		mediphy_essence.change (field, config [field])
	'''
	
	configured = True
	
	print ()
