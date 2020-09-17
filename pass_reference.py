def numbers_less_than_twenty(list):
    counter = 0
    while counter < len(list):
        item = list[counter]
        if item > 20:
            list.remove(item)
        counter += 1
        return list
list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
num_list_sub_20 = numbers_less_than_twenty(list)
print(num_list_sub_20)
