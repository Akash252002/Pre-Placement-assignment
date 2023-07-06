# Write a Python program to merge two sorted lists into a single sorted list.

def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append remaining elements from list1 or list2
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

# Example usage
sorted_list1 = [1, 3, 5, 7]
sorted_list2 = [2, 4, 6, 8]
merged_list = merge_sorted_lists(sorted_list1, sorted_list2)
print(merged_list)
