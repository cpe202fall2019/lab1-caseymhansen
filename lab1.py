import sys
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if int_list == []:
      return None
   max_val = int_list[0]
   for i in range(len(int_list)):
      if int_list[i] > max_val:
         max_val = int_list[i]
   return max_val

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if int_list == []:
      return None
   if len(int_list) == 1:
      return int_list
   return reverse_rec(int_list[1:]) + [int_list[0]]

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list is None:
      raise ValueError
   if not int_list:
      return None
   if len(int_list) == 1:
      return 0
   if len(int_list[low:high]) > 1:
      mid = 1 + int(high - 1 / 2)  # Gets the middle index of the list
      if int_list[mid] == target:  # Checks the middle value of the list
         return mid
         # Checks if middle value in list greater than the target and returns left part of the list
      elif int_list[mid] > target:
         return bin_search(target, low, mid - 1, int_list)
         # Returns right part of the list because the target is greater than the middle value
      else:
         return bin_search(target, mid + 1, high, int_list)
   else:  # Returns None because the specified value was not found
      return None
