# def remove_none_values(dict):
#     for k,v in dict.items():
#         if(dict[k] is None):
#             del dict[k]

def remove_none_values(dict):
    keys_to_delete = []
    for key, value in dict.items():
        if value is None:
            keys_to_delete.append(key)
    for key_to_delete in keys_to_delete:
        del dict[key_to_delete]
    return dict


def page_tup(lol):
    return lol[1]

def sort_pages(pages):
    pages_list = []
    for url, count in pages.items():
        pages_list.append((url, count))
    pages_list.sort(key=page_tup, reverse=True)
    return pages_list