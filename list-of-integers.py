############## Interview Cake Problem 2 #######################


def get_products_of_all_ints_except_at_index(lst):

	if len(lst) < 2:
		raise IndexError('This list needs at least 2 numbers.')
	if len(lst) > 1:
		results_list = []
        for i in range(len(lst)):
			product = 1
			for x in range(len(lst)):
				if x != i:
					product *= lst[x]
			results_list.append(product)
	return results_list


# run your function through some test cases here
print get_products_of_all_ints_except_at_index([1, 3, 8])
print get_products_of_all_ints_except_at_index([0, 0, 0])
print get_products_of_all_ints_except_at_index([1])
