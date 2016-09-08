import json

jsonPath = "../../config.json"
gConf = []

with open(jsonPath, 'r') as f:
    gConf = json.load(f);
