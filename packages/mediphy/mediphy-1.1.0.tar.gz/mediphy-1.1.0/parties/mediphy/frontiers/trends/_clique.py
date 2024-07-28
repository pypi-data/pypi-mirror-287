





#/
#
from mediphy.frontiers.trends.monetary.DB_mediphy_trends.collection_treasures.document.insert import insert_document
from mediphy.frontiers.trends.monetary.DB_mediphy_trends.collection_treasures.document.search import search_treasures
from mediphy.frontiers.trends.monetary.DB_mediphy_trends.collection_treasures.document.count import count_treasures
#
from mediphy.frontiers.trends.quests.saves._clique import saves_clique
#
#
import click
#
#
import ast
from pprint import pprint
#
#\

def trends_clique ():
	@click.group ("trends")
	def group ():
		pass
	
	
	
	''''
		mediphy trends insert-document --domain "wallet.1" --names "[ 'name_1', 'name_2' ]"
		mediphy_1 trends insert-document --domain "wallet.1" --names "[ 'name_1', 'name_2' ]" --topics "[ 'aptos' ]" 
		
		mediphy_1 trends insert-document --domain "solid_food.1" --topics "[ 'food' ]" --cautions "[ 'homo-sapiens ages months 6+' ]"
	"'''
	@group.command ("insert-document")
	@click.option ('--domain', required = True)
	@click.option ('--names', default = '[]')
	@click.option ('--topics', default = '[]')	
	@click.option ('--cautions', default = '[]')
	def command_insert_document (domain, names, topics, cautions):
		insert_document ({
			"document": {
				"domain": domain,
				"names": ast.literal_eval (names),
				"topics": ast.literal_eval (topics),
				"cautions": ast.literal_eval (cautions)
			}
		})
	
	

		
	
	
	
	''''
		mediphy_1 trends search --domain "wallet.1"
	"'''
	@group.command ("search")
	@click.option ('--domain', required = True)
	def command_search (domain):
		treasures = search_treasures ({
			"filter": {
				"domain": domain
			}
		})
		for treasure in treasures:
			pprint (treasure, indent = 4)
			
	@group.command ("count")
	def command_search ():
		count = count_treasures ()
		print ("count:", count)
		
	@group.command ("itemize")
	def on ():
		print ("on")
		

	group.add_command (saves_clique ())


	return group




#



