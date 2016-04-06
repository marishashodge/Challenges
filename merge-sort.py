
# Question: With two pre-sorted lists as input, return a list that is merged and sorted

# Input = [1,3,10,14], [9,10,11,20]
# Output = [1,2,3,4,5,9,10,11]

def merge_two_sorted_lists(a, b):

    results_list = []

    #compare item at the first index in both a and b, add whichever item that is lower to the results list, and then pop the  first item off that list

    while len(a) > 0 and len(b) > 0:
      if a[0] < b[0]:
          results_list.append(a[0])
          a.pop(0)
      elif a[0] > b[0]:
          results_list.append(b[0])
          b.pop(0)
      else:
          results_list.append(a[0])
          a.pop(0)
          results_list.append(b[0])
          b.pop(0)

    if len(a) == 0:
      results_list.extend(b)

    if len(b) == 0:
      results_list.extend(a)

    return results_list


# Runtime: O(n)

print merge_two_sorted_lists([1,3,10,14], [9,10,11,20])


#Question 2: Make sure a list is sorted

# input= [5,4,7,9,2,1]
# output= [1,2,4,5,7,9]

def merge_sort_list_with_recursion(lst):

    if len(lst) < 2:
        return lst

    mid = len(lst)/2
    lst1 = merge_sort_list_with_recursion(lst[:mid])
    lst2 = merge_sort_list_with_recursion(lst[mid:])

    results_list = []

    while len(lst1) > 0 or len(lst2) > 0:

        if len(lst1) == 0:
            results_list.append(lst2.pop(0))

        elif len(lst2) == 0:
            results_list.append(lst1.pop(0))

        elif lst1[0] < lst2[0]:
            results_list.append(lst1.pop(0))

        else:
            results_list.append(lst2.pop(0))

    return results_list

print merge_sort_list_with_recursion([5,4,7,9,2,1])
