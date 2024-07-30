


'''
	from Oumuamua.adventures.monetary.DB.Oumuamua_inventory.foods.document.insert import insert_food
	insert_food ({
		"FDC_ID": "",
		"affiliates": [],
		"goodness_certifications": []
	})
'''



from Oumuamua._essence import retrieve_essence
from Oumuamua.adventures.monetary.DB.Oumuamua_inventory.connect import connect_to_Oumuamua_inventory
from Oumuamua.besties.food_USDA.nature_v2._ops.retrieve import retrieve_parsed_USDA_food
	
import ships.modules.exceptions.parse as parse_exception


def find_next_emblem (food_collection):
	count = food_collection.count_documents ({})

	if (count == 0):
		return 1

	next_emblem = food_collection.find ().sort ({ 
		"emblem": -1
	}).limit (1).next () ["emblem"] + 1
	
	return next_emblem;
	

	
'''
	FDC_ID = "",
	affiliates = [],
	goodness_certifications = []
'''
def insert_food (packet):
	FDC_ID = packet ["FDC_ID"]
	affiliates = packet ["affiliates"]


	try:
		[ driver, Oumuamua_inventory_DB ] = connect_to_Oumuamua_inventory ()
		food_collection = Oumuamua_inventory_DB ["food"]
	except Exception as E:
		print ("food collection connect:", E)
		
	
	try:	
		essence = retrieve_essence ()
		
		print ("essence:", essence)
		
		USDA_food_pass = essence ['USDA'] ['food']
		
		
		

		out_packet = retrieve_parsed_USDA_food ({
			"FDC_ID": FDC_ID,
			"USDA API Pass": USDA_food_pass
		})


		'''
			This is actually two operations.
				1. find the previous emblem
			
			Multi step insert?
		'''
		next_emblem = find_next_emblem (food_collection)
		
		print ("next_emblem:", next_emblem)
		
		inserted = food_collection.insert_one ({
			'emblem': next_emblem,
			'nature': out_packet,
			"affiliates": affiliates,
			"goodness certifications": goodness_certifications
		})
		
		inserted_document = food_collection.find_one ({"_id": inserted.inserted_id })
		
		print ()
		print ("inserted:", inserted_document ["emblem"])

	except Exception as E:
		print (parse_exception.now (E))
	
		raise Exception (E)
		pass;
		
	try:
		driver.close ()
	except Exception as E:
		print (parse_exception.now (E))
		print ("food collection disconnect exception:", E)	
		
	return None;








