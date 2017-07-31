record_list = [1, 5, 8, 2, 9, 23]


# 顺序查找
def order_to_find(record_list, vaule):
    for index, values in enumerate(record_list):
        if values == vaule:
            return index
    return None


index = order_to_find(record_list, 50)


def order_to_find_py(record_list, vaule):
    try:
        return record_list.index(vaule)
    except ValueError:
        return None


index_py = order_to_find_py(record_list, 50)

# 二分查找法 1、顺序存储结构，2、待查表是有序表
order_record_list = sorted(record_list)


def dichotomy(order_record_list, vaule):
    low = 0
    length = len(order_record_list)

    while length > low:
        mid = int((length + low) / 2)

        if order_record_list[mid] == vaule:
            return mid
        elif order_record_list[mid] > vaule:
            length = mid
        else:
            low = mid

    return None


# for i in order_record_list:
#     res = dichotomy(order_record_list, i)
#     print('值', i, '位置', res)


from bisect import *

# 将值按顺序插入
# insort_left, insort_right 插入相同值时的位置不同，结果相同
insort(order_record_list, 3)
print('res', order_record_list)

# 查找值在列表中的位置，不会插入, 若相同值，插入在已有数后面
#  bisect_left ， bisect_right  处理将会插入重复数值的情况，返回将会插入的位置
index = bisect(order_record_list, 2)
print('res', index)


def dichotomy_py(order_record_list, vaule):
    i = bisect_left(order_record_list, vaule)

    # 若是新增最大值 则会进行插入在最后，则 i == len(order_record_list)
    # 只有插入原来列表中的值，才会 order_record_list[i] == vaule
    if i != len(order_record_list) and order_record_list[i] == vaule:
        return i
    return None


for i in order_record_list:
    res = dichotomy_py(order_record_list, i)
    print('值', i, '位置', res)
