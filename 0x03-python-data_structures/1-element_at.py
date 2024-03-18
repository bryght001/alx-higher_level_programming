#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > my_list[-1]:
        return
    elif idx < 0:
        return
    else:
        return my_list[idx]
