import re

def load_any_json(my_str, keys, struct="listofdict"):
    if struct=="listofdict":
        my_str = my_str.replace("\'","\"")
        res_dict = {}
        for k in keys:
            match_res  = re.findall(f'"{k}": "(.*?)"', my_str)
            if len(match_res)==0:
                match_res  = re.findall(f'"{k}": (\d+)', my_str)
                match_res = [int(s) for s in match_res]
            res_dict[k] = match_res

        final_res = []
        for i in range(len(res_dict[keys[0]])):
            final_res.append({k:res_dict[k][i] for k in keys})
    else:
        raise NotImplementedError
    return final_res




import re
import json

mystr = "[{'PageIndex': 0, 'Index': 0, 'LineIndexInPage': 1, 'Sentence': '17 Best LinkedIn Summary & Bio Examples [+ How to Write Your Own]'}, {'PageIndex': 0, 'Index': 1, 'LineIndexInPage': 2, 'Sentence': '17 Best LinkedIn Summary & Bio Examples [+ How to Write Your Own]'}]"

# Preprocess the string to replace single quotes with double quotes
# preprocessed_string = re.sub(r"(\w+):", r'"\1":', string.replace("'", '"'))
#
# # Load the list of dictionaries using json.loads()
# result = json.loads(preprocessed_string)
#
# print(result)

print(load_any_json(mystr,["PageIndex","Index","LineIndexInPage","Sentence"]))
