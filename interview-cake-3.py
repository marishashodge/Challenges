
################## Interview Cake Q#3 ###############################

# Highest Product of Three

# Given a list_of_ints, find the highest_product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.

def get_highest_product_of_three(lst):

    highest = max(lst[0], lst[1])

    lowest = min(lst[0], lst[1])

    highest_product_of_2 = lst[0] * lst[1]

    lowest_product_of_2 = lst[0] * lst[1]

    highest_product_of_three = lst[0] * lst[1] * lst[2]

    for num in lst[2:]:

        if (highest_product_of_2 * num) > highest_product_of_three:
            highest_product_of_three = highest_product_of_2 * num

        if (lowest_product_of_2 * num) > highest_product_of_three:
            highest_product_of_three = lowest_product_of_2 * num

        if (highest * num) > highest_product_of_2:
            highest_product_of_2 = highest * num

        elif (lowest * num) > highest_product_of_2:
            highest_product_of_2 = lowest * num

        if num > highest:
            highest = num

        if num < lowest:
            lowest = num

    return highest_product_of_three



print get_highest_product_of_three([4,5,6])
print get_highest_product_of_three([1,2,2,4])
print get_highest_product_of_three([-1,9,9,-5])
