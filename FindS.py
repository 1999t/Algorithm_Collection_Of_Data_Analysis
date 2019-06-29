'''
    Find_S算法实现: 寻找极大特殊假设
'''

# 数据集合
x1 = ['sunny', 'warm', 'normal', 'strong', 'warm', 'same' ,1]
x2 = ['sunny', 'warm', 'high', 'strong', 'warm', 'same' , 1]
x3 = ['rainy', 'cold', 'high', 'strong', 'warm', 'change', 0]
x4 = ['sunny', 'warm', 'high', 'strong', 'cool', 'change', 1]

xa = [x1, x2, x3, x4]
h = [ None, None, None, None, None, None ]

sum = 0
for each_data in xa:
    sum += 1
    if each_data[-1] == 0:
        print('第', sum, '个样本, 规则是：', h)
        continue
    else:
        for each in range(len(each_data[:-1])):
            if h[each] == None:
                h[each] = each_data[each]
            elif h[each] != each_data[each]:
                h[each] = '?'
        print('第', sum, '个样本, 规则是：', h)


