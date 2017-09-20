 # -*- coding: utf-8 -*-

def queryset_to_dict(queryset):
    """
    初步将 queryset 转换成 json 化的字典
    :param queryset:
    :return:
    """
    return_list = []
    for item in queryset.iterator():
        tem = {}
        fields = item._meta.fields
        for field in fields:
            c = getattr(item, field.name)
            tem[field.name] = str(c)
            return_list.append(tem)
    return return_list