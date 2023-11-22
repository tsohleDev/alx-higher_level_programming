#!/usr/bin/python3

def fucn(my_list, search, replace):
    for idx, i in enumerate(my_list):
        my_list[idx] = replace if search == i else i

    return my_list

if __name__ == "__main__":
    square = fucn([1,2,3,4,5], 3, 20)
    print(square)


    a = {1,2,3,4,5}
    b = {9,2,3,0}

    c = a ^ b
    print(c)
