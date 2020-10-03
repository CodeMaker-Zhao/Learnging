from itertools import chain
def new_point(bp,ex_layer):
    bp_up = [bp[0],bp[1]-1]
    bp_down = [bp[0],bp[1]+1]
    bp_left = [bp[0]-1,bp[1]]
    bp_right = [bp[0]+1,bp[1]]
    point_array = [bp_up,bp_down,bp_left,bp_right]
    new_point_array = []
    for item in point_array:
        item = check_point(ex_layer,item)
        if item != None:
            new_point_array.append(item)
    new_point_chain = list(chain(*new_point_array))
    return new_point_chain

def check_point(ex_layer,new_point):
    c_list = change_num_to_array(ex_layer)
    if new_point in c_list:
        return None
    return new_point

def change_num_to_array(layer):
    c_list = [[0]*2 for i in range(int(len(layer)/2))]
    counter = 0
    for i in range(int(len(layer)/2)):
        c_list[i][0] = layer[counter]
        c_list[i][1] = layer[counter+1]
        counter += 2
    return c_list

print(new_point([1,2],[1,2,3,4,1,2,1,3]))

