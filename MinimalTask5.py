number_list = [1, 3, 6, 4, 1, 2]
def get_smallest_positive_integer(number_list):
    if all(number < 0 for number in number_list) or 1 not in number_list:
        return 1
    else:
        try:
            
            number_list = sorted(number_list) 
            return min(x for x in range(number_list[0], number_list[-1] + 1) if x not in number_list and x != 0)
        except:
            return max(number_list) + 1


print(get_smallest_positive_integer(number_list))