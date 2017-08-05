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


# bubble_sort(record_list)


def bubble_sort_update(order_list):
    """ 添加了 flag ，有数据交换，则在进行下一轮循环判断"""
    cycle_count = 0
    swap_count = 0

    length = len(order_list)
    flag = True
    for i in range(length - 1):
        if flag:
            flag = False
            for j in range(length - i - 1):
                cycle_count += 1

                if order_list[j] > order_list[j + 1]:
                    order_list[j], order_list[j + 1] = order_list[j + 1], order_list[j]
                    flag = True
                    swap_count += 1
    print('order_list', order_list, cycle_count, swap_count)


# bubble_sort_update(list_2)

# 简单选择排序
#  在为排序序列中选出最小的元素和序列的第 1 个元素进行交换
#  第 2 个...... 一次类推
#  相比于冒泡，两层全遍历不可缺少，但是数据交换次数比较少

# 长度9，0-8
simple = [54, 38, 96, 23, 15, 72, 60, 45, 83]


def simple_sort(record_list):
    """ Simple Selection Sort """
    cycle_count = 0
    swap_count = 0

    length = len(record_list)
    for i in range(length - 1):
        k = i
        for j in range(i + 1, length):
            cycle_count += 1
            if record_list[k] > record_list[j]:
                k = j

        if k != i:
            record_list[i], record_list[k] = record_list[k], record_list[i]
            swap_count += 1

    print('simple_sort', record_list, cycle_count, swap_count)


# simple_sort(simple)

# 直接插入排序
# 将待排序序列分为 排号序，为排序两部分
# 已排序只有1个元素，未排序有 n-1 个
# 进行插入排序
insert_list = [35, 3, 61, 135, 78, 29, 50]


def insert_sort(insert_list):
    length = len(insert_list)

    for i in range(1, length):
        tem = insert_list[i]
        j = i - 1
        print('======', i)
        # insert_list[j] 是已经排序列表到最后最大一个元素
        # insert_list[j] > tem， 和已排序最后一个元素进行比较
        # 排序最后一个比当前值大，需要将当前值插入到已排序队列中
        while j >= 0 and insert_list[j] > tem:
            insert_list[j + 1] = insert_list[j]
            j -= 1  # j 若不改变，while 条件一直成立

        print('后移插入前', insert_list, tem, j + 1)
        insert_list[j + 1] = tem
        print('后移插入后', insert_list)

    print('insert_list', insert_list)


insert_sort(insert_list)
