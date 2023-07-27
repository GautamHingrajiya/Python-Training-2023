# import the modules
import instagram_explore as ie
import json

# search user name
result = ie.user('timesofindia')

parsed_data= json.dumps(result, indent = 4,
						sort_keys = True)

# displaying the data
print(parsed_data[15:400])
