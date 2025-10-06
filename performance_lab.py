# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    numbers.sort()
    max_count = count = 1
    most = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
            most = numbers[i]
    return most
    pass
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))
"""
Time and Space Analysis for problem 1:
- Best-case: o(n)
- Worst-case: o(n)
- Average-case: o(n)
- Space complexity: Not sure here I tried searching online for help outside of resoures and got o(k) or o(u)
- Why this approach? Because of how quick this approch is while being able to use dictornary to count the numbers and show what number is most frequent here
- Could it be optimized? No because this is already optimal and saves time
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]


def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result  
print(remove_duplicates([4, 5, 4, 6, 5, 7]))
pass

"""
Time and Space Analysis for problem 2:
- Best-case: O(n) - we go through each number once(single loop)
- Worst-case: O(n) - all numbers are added to a set and checked in single loop
- Average-case: O(1) - set operations are O(1)
- Space complexity: O(n)
- Why this approach? This approach was easiest because the information already gave us numbers in set form. Now we just needed to use set to check all numbers and remove the number that was on consistant throughout list created.
- Could it be optimized? No because it is already in a simple fast form
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs
print(find_pairs([1, 2, 3, 4], target=5)) 

pass

"""
Time and Space Analysis for problem 3:
- Best-case: O(n) - single loop through list
- Worst-case: O(n) - checks numbers in list
- Average-case: O(1) - accessing the index
- Space complexity: O(n)
- Why this approach? this approach allows us to use a single loop to avoid nested loops
- Could it be optimized? No because it's already linear, fast, and effeicent
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 2 
    lst = [None] * capacity
    size = 0

    for i in range(1, n + 1):
        if size == capacity:
            print(f"Resizing: current capacity {capacity} → new capacity {capacity*2}")
            new_lst = [None] * (capacity * 2)
            for j in range(size):
                new_lst[j] = lst[j]
            lst = new_lst
            capacity *= 2
        lst[size] = i
        size += 1
add_n_items(6)

pass

"""
Time and Space Analysis for problem 4:
- When do resizes happen? when list is full
- What is the worst-case for a single append? O(n)
- What is the amortized time per append overall? O(1) average
- Space complexity: O(n)
- Why does doubling reduce the cost overall? Doubling reduces the cost overall by ensuring the number grows slowy to not reach capacity quickly
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    totals = []
    current_sum = 0
    for num in nums:
        current_sum += num
        totals.append(current_sum)
    return totals
print(running_total([1, 2, 3, 4])) 
pass

"""
Time and Space Analysis for problem 5:
- Best-case: O(n) Single loop though whole problem
- Worst-case: O(n) Same as best case because of single loop
- Average-case: O(n)
- Space complexity:O(n)
- Why this approach? a single loop allows us to run sums and be able to append(add) to the current sum
- Could it be optimized? We could optimize space for less time but overall this is a great effective method for this problem
"""
https://github.com/braswell1106/Assignment5/commits/main/performance_lab.py