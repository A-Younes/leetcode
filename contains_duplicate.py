def contains_dup(num_list):
    # Create and empty hashset to add to when iterating over the list
    hashset = set()

    for i in num_list:
        if i in hashset:
            print("True")
            return True
        hashset.add(i)
    print("False")
    return False

nums = [1, 2, 3, 4, 5, 6, 7, 1]
contains_dup(nums)