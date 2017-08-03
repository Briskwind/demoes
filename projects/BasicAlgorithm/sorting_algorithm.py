""" 基本的排序算法 """
order_list = [35, 28, 61, 78, 89, 50, 135]

list_2 = [2, 1, 3, 4, 5, 8, 6, 7]


# 冒泡排序
# 第0个，从1起，和之后的每个进行对比，大了则互换位置
# 第1个，从2起， 和之后的每个对比 ……
# 第i个， 从i+1起，……
# i+1 <= length, 故 i 需 0 < i < length -1

# (可进行优化)
def bubble_sort(order_list):
    count = 0
    length = len(order_list)

    for i in range(length - 1):
        for j in range(i + 1, length):
            count += 1

            if order_list[i] > order_list[j]:
                order_list[j], order_list[i] = order_list[i], order_list[j]
    print('count', count)
    return order_list


res = bubble_sort(list_2)
print('res', res)

