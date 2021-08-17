# 별 찍기 - 10
# 76ms

import sys

def draw_star(len) :
    if len == 1 :
        return ["*"]
    unit_block = draw_star(len//3)
    next_unit_block = []
    for row in unit_block :
        next_unit_block.append(row*3)
    for row in unit_block :
        next_unit_block.append(row+ " "*(len//3) + row)
    for row in unit_block :
        next_unit_block.append(row*3)
    
    return next_unit_block

print("\n".join(draw_star(int(sys.stdin.readline()))))
    
    






                
    




