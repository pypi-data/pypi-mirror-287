

import rich

from mediphy._essence import retrieve_essence

def show ():
	mongo = mediphy_essence.connect ()


	documents = mongo ['safety'] ['passes'].find ()

	# Iterate over the documents and print them
	data = []
	for document in documents:	
		data.append ({
			"_id": str (document ["_id"]),
			"legal": document ["legal"]
		})

	rich.print_json (data = data)