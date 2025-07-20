#!/usr/bin/python3
def no_c(my_string):
    s_list = list(my_string)
    for i in range(len(s_list)):
        if s_list[i] == 'c' or s_list[i] == 'C':
            s_list[i] = ''
    new_s = ''.join(s_list)
    return (new_s)
