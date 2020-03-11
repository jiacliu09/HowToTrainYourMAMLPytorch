import json
import os

jsn_inp = '../datasets/map_to_label_name_mini_imagenet_full_size.json'
jsn_out = jsn_inp.replace('.json', '_reformat.json')

with open(jsn_inp, 'r') as inp:
    dataset = json.load(inp)

    '''
    for k,v in sorted(dataset.items()):
        print(k, v)
        exit()
    key_list = sorted([int(key) for key in dataset.keys()])
    '''

with open(jsn_out, 'w') as out:
    json.dump(dataset, out, indent=2)
    print('*** {} ***'.format(jsn_out))
