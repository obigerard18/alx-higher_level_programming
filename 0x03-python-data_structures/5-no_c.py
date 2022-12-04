#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for elm in my_string:
        if elm != 'C' and elm != 'c':
            new_str += elm
    return new_str
