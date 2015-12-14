#!/usr/bin/python
def dict_list_to_dict(dict_list, main_key):
    csv_dict = {}
    for dic in dict_list:
        key = dic[main_key]
        csv_dict[key] = {}
        for k in dic:
            if not k == main_key:
                csv_dict[key][k] = dic[k]
    return csv_dict