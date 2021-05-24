import os
import json
import yaml

# ----------------------------------------------------------------------------------------------------------

# 1
'''                                        Yaml to text parser                                     '''
with open("file_yaml.yml", "r") as yaml_file_,\
	 open('file_yaml.txt', 'w') as file:
    data = yaml.safe_load(yaml_file_)
    yaml.dump(data, file)
# ----------------------------------------------------------------------------------------------------------

# 2
'''                                        json to txt parser                                     '''
with open("file_json.json", "r") as json_ ,\
	 open('file_json.txt', 'w') as file:
    data = json.load(json_)
    json.dump(data, file)
# ----------------------------------------------------------------------------------------------------------

# 3
'''                                        json to yaml parser                                     '''
with open("file_json.json", 'r') as json__,\
	 open("file_json.yml", "w") as yaml_file:
    object_json = json.load(json__)
    yaml.dump(object_json, yaml_file)
# ----------------------------------------------------------------------------------------------------------

# 4
'''                                        Yaml to json parser                                    '''
with open("file_yaml.yml", 'r') as yaml_,\
	 open("file_yaml.json", "w") as json_1:
    object_yaml = yaml.safe_load(yaml_)
    json.dump(object_yaml, json_1)
# ----------------------------------------------------------------------------------------------------------

