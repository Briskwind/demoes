""" 基本的排序算法 """
record_list = [35, 28, 61, 78, 89, 50, 135]

list_2 = [2, 1, 3, 4, 5, 6, 7]


# 冒泡排序
# 窗口为2移动，两两比较

def bubble_sort(record_list):
    count = 0
    length = len(record_list)

    for i in range(length - 1):
        print('=======')

        for j in range(length - i - 1):
            count += 1

            if record_list[j] > record_list[j + 1]:
                print(j, j + 1)

                record_list[j], record_list[j + 1] = record_list[j + 1], record_list[j]
    print('order_list', record_list, count)


bubble_sort(record_list)


def bubble_sort_update(order_list):
    """ 添加了 flag ，有数据交换，则在进行下一轮循环判断"""
    count = 0
    length = len(order_list)
    flag = True
    for i in range(length - 1):
        if flag:
            flag = False
            for j in range(length - i - 1):
                count += 1

                if order_list[j] > order_list[j + 1]:
                    order_list[j], order_list[j + 1] = order_list[j + 1], order_list[j]
                    flag = True
    print('order_list', order_list, count)


bubble_sort_update(list_2)
