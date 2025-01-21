sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"]

# ele is loop variable here. you can use any name
# for ele in sample_list:
#     print(ele, len(ele))

# Print the element and its corresponding index
# for idx, ele in enumerate(sample_list):
#     print(idx, ele)

# Range based for loop
# 1:10 -> 1,2..,9
# sample_range = range(0, len(sample_list))
# print(sample_range, type(sample_range))
# range(0, 5) <class 'range'> --> it is a range object

# for idx in sample_range:
#     print(idx)
# 0
# 1
# 2
# 3
# 4    

# for idx in range(0, len(sample_list)):
#     print(idx, sample_list[idx])

# for idx in range(0, len(sample_list)):
#      if sample_list[idx] == "Docker":
#           continue # it will skip iteration
#      print(idx, sample_list[idx])

# for idx in range(0, len(sample_list)):
#      if sample_list[idx] == "Docker":
#           break # it will break loop
#      print(idx, sample_list[idx])

# for idx in range(0, len(sample_list)):
#      if sample_list[idx] == "Docker":
#           pass # execute whatever is next this is dummy
#      print(idx, sample_list[idx])

# for idx in range(0, len(sample_list)):
#      if sample_list[idx] == "Docker":
#           exit(1) # exit entire program
#      print(idx, sample_list[idx])

# print(sample_list)

# sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"]

# idx = 0

# while idx < len(sample_list):
#     print(idx, sample_list[idx])
#     idx += 1

sample_dict = {1: 1, 2: 4, 3: 9}

for k, v in sample_dict.items():
    print(k, v)


