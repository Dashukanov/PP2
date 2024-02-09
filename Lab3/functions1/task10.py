def unique_el(input_list):
    unique_list = []
    for i in input_list:
        if i not in unique_list:
            unique_list.append(i)
    
    return unique_list

first_list = [4, 8, True, True, 77, 3.14, 3.14]
second_list = unique_el(first_list)
print(second_list)