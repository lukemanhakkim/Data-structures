"""
Author: Lukeman Hakkim Sheik Alavudeen
To balance the given paranthesis using stack
"""

open_brac_list = ["[", "{", "("]
close_brac_list = ["]", "}", ")"]


def bal_paranthesis_check(my_str):
    if len(my_str)==0:
       return "Balanced"
    stack = []
    for i in my_str:
        if i in open_brac_list:
            stack.append(i)
        elif i in close_brac_list:
             pos = close_brac_list.index(i)
             #import pdb;pdb.set_trace()
             if open_brac_list[pos]==stack[len(stack)-1]:
                 stack.pop()
             else:
                 return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

my_str="{[]{()}"
print(bal_paranthesis_check(my_str))



