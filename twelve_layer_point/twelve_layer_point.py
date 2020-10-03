#数组降维工具
from itertools import chain
#画图软件
import matplotlib.pyplot as plt


#产生新的点
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

#检查点是否在上一层出现过
def check_point(ex_layer,new_point):
    c_list = change_num_to_array(ex_layer)
    if new_point in c_list:
        return None
    return new_point

#把数字转化为数组
def change_num_to_array(layer):
    c_list = [[0]*2 for i in range(int(len(layer)/2))]
    counter = 0
    for i in range(int(len(layer)/2)):
        c_list[i][0] = layer[counter]
        c_list[i][1] = layer[counter+1]
        counter += 2
    return c_list

def fill_layer(base_point):
    layers = []
    layers.append(base_point)
    for i in range(0,11):
        new_layer = []
        for item in layers[i]:
            new_layer.append(item)
        #把上一层的数字两两组成坐标数组
        c_list = change_num_to_array(layers[i])
        #初始化检查数组，检查数组用于检查新产生的点是否已经在图中出现过
        check_arr = layers[i]
        for item in c_list:
            new_p = new_point(item,check_arr)
            for m in new_p:
                new_layer.append(m)
            check_arr = new_layer
        layers.append(new_layer)
    return layers

twelev_layer_point = fill_layer([25,26])
print(len(twelev_layer_point))
#可视化部分，取第12层进行展示
pic = change_num_to_array(twelev_layer_point[11])
#存储X坐标和y坐标
x_values =[]
y_values = []
for item in pic:
    x_values.append(item[0])
    y_values.append(item[1])
#根据y_color中的数进行颜色分层
y_color=[]
for x in range(0,12):
    y_lay = []
    if x==0:
        y_color.append(12)
        continue
    times = (len(twelev_layer_point[x])-len(twelev_layer_point[x-1]))/2
    for y in range(0,int(times)):
        y_lay.append(12-x)
    y_color.extend(y_lay)

plt.scatter(x_values,y_values,cmap=plt.cm.Greens,c=y_color)
plt.axis([10,40,10,40])
plt.show()