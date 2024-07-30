


'''	
	from Oumuamua.adventures.monetary.DB.Oumuamua_inventory.connect import connect_to_Oumuamua_inventory
	[ driver, Oumuamua_inventory_DB ] = connect_to_Oumuamua_inventory ()
	driver.close ()
'''

'''
	from Oumuamua.adventures.monetary.DB.Oumuamua_inventory.connect import connect_to_Oumuamua_inventory
	[ driver, Oumuamua_inventory_DB ] = connect_to_Oumuamua_inventory ()
	foods_collection = Oumuamua_inventory_DB ["foods"]	
	foods_collection.close ()
'''




from Oumuamua.adventures.monetary.moves.URL.retrieve import retreive_monetary_URL
from Oumuamua._essence import retrieve_essence
	
import pymongo

def connect_to_Oumuamua_inventory ():
	essence = retrieve_essence ()
	
	ingredients_DB_name = essence ["monetary"] ["databases"] ["template"] ["alias"]
	monetary_URL = retreive_monetary_URL ()

	driver = pymongo.MongoClient (monetary_URL)

	return [
		driver,
		driver [ ingredients_DB_name ]
	]