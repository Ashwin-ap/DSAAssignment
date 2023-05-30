Q1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
-
def twoSum(nums, target):
    num_dict = {} 
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_dict:
            return [num_dict[complement], i]
        
        num_dict[num] = i
    
    return []

Q2. Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
-
def removeElement(nums, val):
    k = 0 
    
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
        
    return k

Q3. Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
-
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1  
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid 
        
        elif nums[mid] < target:
            left = mid + 1
            
        else:
            right = mid - 1
    
    return left

Q4. You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
-
def plusOne(digits):
    carry = 1
    n = len(digits)
    
    for i in range(n-1, -1, -1):
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10
        
        if carry == 0:
            break
    
    if carry != 0:
        digits.insert(0, carry)
    
    return digits

Q5. You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
-
def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1  
    k = m + n - 1 
    
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

Q6. Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
-
def containsDuplicate(nums):
    num_set = set()
    
    for num in nums:
        if num in num_set:
            return True
        else:
            num_set.add(num)
    
    return False

Q7. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.
-
def moveZeroes(nums):
    n = len(nums)
    left = 0  # Pointer for the next non-zero element
    
    for i in range(n):
        if nums[i] != 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1


Q8. You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
-
def findErrorNums(nums):
    n = len(nums)
    num_set = set()
    duplicate = -1
    missing = -1
    
    # Find the duplicate and missing numbers
    for num in nums:
        if num in num_set:
            duplicate = num
        num_set.add(num)
    
    # Find the missing number
    for i in range(1, n+1):
        if i not in num_set:
            missing = i
            break
    
    return [duplicate, missing]

