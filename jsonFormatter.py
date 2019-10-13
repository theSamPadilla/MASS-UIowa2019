import json


#dictionary to be saved in JSON at the end
mydict = {}

#change the jason file name
data_path = "dummy.json"
output_file = "output1.json"

with open(data_path, "r") as data_file:
	data = json.load(data_file)

#iterate over attributes
for element in data:
	print(element)
	if 'id' in element:
		print(type(element))
		#save the id value to dictionary
		mydict["id"] = data['id']

	if "text" in element:
		mydict["text"] = data["text"]

	if "user" in element:
		for ind, a in enumerate(data[element]):
			print(a)
			print(ind)
			if "location" in a:
				
				mydict["loc"] = data[element][a]

	if "quoted_status" in element:
		for b in data[element]:
			if "lang" in b:
				mydict["lang"] = data[element][b]

	#open the output file in append mode and write json
with open(output_file, 'a') as f:
	json.dump(mydict, f)

	

