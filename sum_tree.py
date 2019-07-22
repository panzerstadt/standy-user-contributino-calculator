
import json
import numpy as np
import pandas as pd 

json_file = "./tree.json"
json_data = open(json_file)
data = json.load(json_data)
data



keys = sorted(list(data.keys()))
num = len(data)
rel = np.zeros((num, num))

for i in range(len(keys)):
    one_end = keys[i]
#     print (one_end)
    children = data[one_end]['children']
    
#     print (children)
    if children == 'none':
        continue
    else:
        for j in range(len(children)):
#             print ('---' + children[j])

            theother_end = keys.index(children[j])
#             print(keys.index(one_end), theother_end)
            rel[keys.index(one_end), theother_end] = 1
          
      

rel_df = pd.DataFrame(rel, columns = keys, index = keys)


mid_user = 'user_e' # user along the tree where the summation ends 
starting_user = 'user_a' # 'user_c' parent user or not 
starting_matrix = np.array(data[starting_user]['matrix'])

while mid_user != starting_user:
    
    print (mid_user)
    mid_user_1 = rel_df[rel_df[mid_user] == 1].index.values[0]
    mid_user_1_matrix = data[mid_user_1]['matrix']
    mid_user = mid_user_1
    starting_matrix += np.asarray(mid_user_1_matrix)

