
################## Interview Cake Q#2 ###############################

# Product of All other Numbers
# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

def get_products_of_all_ints_except_at_index(lst):

	if len(lst) < 1:
		return []
	elif len(lst) == 1:
		return [1]
	else:

		results_list = [None] * len(lst)

		product_before = 1
		i = 0
		while i < len(lst):
			results_list[i] = product_before
			product_before *= lst[i]
			i += 1

		product_after = 1
		i = len(lst) - 1
		while i >= 0:
			results_list[i] = results_list[i] * product_after
			product_after *= lst[i]
			i -= 1


	return results_list

print get_products_of_all_ints_except_at_index([1,2])
print get_products_of_all_ints_except_at_index([9,5,7,20,10])

Runtime = O(n)
