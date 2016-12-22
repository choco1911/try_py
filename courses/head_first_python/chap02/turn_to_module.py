# Automated approach
def recur_print(item_list) :
    for each_item in item_list :
        if isinstance(each_item,list) :
            recur_print(each_item)
        else :
            print each_item 

#recur_print(movie)
