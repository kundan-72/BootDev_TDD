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


def print_report(pages):
    links = []
    for k in list(pages):
        if pages[k] is None:
            del pages[k]
    for k in pages:    
        links.append((k,pages[k]))
    links.sort(key=page_tup)
    
    for link in links:
        print("Found {} internal links to {}".format(link[1],link[0]))
        
# def print_report(pages):
#     pages = remove_none_values(pages)
#     pages_list = sort_pages(pages)
#     for page in pages_list:
#         url = page[0]
#         count = page[1]
#         print("Found {} internal links to {}".format(count, url))


# # remove_none_values removes all keys from a dictionary
# # where the value was None
# def remove_none_values(dict):
#     keys_to_delete = []
#     for key, value in dict.items():
#         if value is None:
#             keys_to_delete.append(key)
#     for key_to_delete in keys_to_delete:
#         del dict[key_to_delete]
#     return dict
        
        