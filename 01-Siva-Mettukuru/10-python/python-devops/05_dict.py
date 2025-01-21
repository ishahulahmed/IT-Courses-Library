sample_dict = {1: 1, 2: 4, 3: 9} # dict()
# Keys in dictionary should be of immutable datatype
# list as key gives error because it is mutable datatype

print(sample_dict[3])

sample_dict = {1: 1, 2: 4, 3: 9, 3: 15}
print(sample_dict[3]) # 15 --> first key is overriden now 15 will be it's value

sample_dict = {(1, 2, 3, 4): 1, 2: 4, 3: 9}
print(sample_dict[(1, 2, 3, 4)]) # 1

sample_dict = {"1": 1, 2: 4, 3: 9}
print(sample_dict["1"])

# sample_dict = {[1, 2, 3, 4]: 1, 2: 4, 3: 9}
# print(sample_dict[[1, 2, 3, 4]]) # error

"""
Traceback (most recent call last):    
  File "d:\devops\repos\python-devops\05_dict.py", line 11, in <module>     
    sample_dict = {[1, 2, 3, 4]: 1, 2: 4, 3: 9}
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list
"""

dict_keys = sample_dict.keys()
dict_values =sample_dict.values()
dict_items = sample_dict.items()
print(dict_keys, dict_values, dict_items)
# dict_keys(['1', 2, 3]) dict_values([1, 4, 9]) dict_items([('1', 1), (2, 4), (3, 9)])

# What happens if you access a key that is not present inside a dict
sample_dict = {"1": 1, 2: 4, 3: 9}
print(sample_dict.get(1)) # None (if key is not present)
# print(sample_dict[1]) # Error because the key is not present

sample_dict = {1: 1, 2: 4, 3: 9}
sample_dict[4] = 16
print(sample_dict)
# {1: 1, 2: 4, 3: 9, 4: 16}




