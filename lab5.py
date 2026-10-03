# Name: Nathan Lenahan
# KUID: 3178995
# LAB Session (Day/Time): Wednesday 11am
# LAB Assignment: Lab 5
# Description: The program implements the recursive implementation
# of Merge sort using Algorithms 9 and 10 of Section 5.4
# Collaborators/Sources: None

import re

def get_input_list(prompt="Enter numbers (use spaces and/or commas): ") -> list[int]:
    user_input = input(prompt)
    # Split on commas or spaces (one or more of them)
    tokens = re.split(r"[,\s]+", user_input.strip())
    # Convert to integers, ignoring empty strings
    return [int(t) for t in tokens if t]

#Merges two sorted lists into one sorted list 
def merge(list1, list2):
    merged_list = []

    #Continuously compares the first elements of the list while both still have values
    while len(list1) > 0 and len(list2) > 0:

        #Removes the smaller value from the two and adds it to merged list
        if list1[0] < list2[0]:
            merged_list.append(list1.pop(0))
        elif list2[0] < list1[0]:
            merged_list.append(list2.pop(0))

        #If list1 is empty, adds the rest of list2
        if list1 == []:
            while len(list2) > 0:
                merged_list.append(list2.pop(0))

        #If list2 is empty, add the rest of list1
        if list2 == []:
            while len(list1) > 0:
                merged_list.append(list1.pop(0))

    return merged_list

#Sorts a list by recursively dividing the list into smaller lists and merging them
def mergesort(entry_list):

    #Base case for a list with one or less element
    if len(entry_list) <= 1:
        return entry_list
    
    mlist1 = []
    mlist2 = []

    n = len(entry_list)

    #Divides list into two halves
    if n > 1:
        m = n//2

        #Add the first half of list to mlist1
        for x in range(m):
            mlist1.append(entry_list[x])

        #Add the second half of list to mlist2
        for x in range(m, n):
            mlist2.append(entry_list[x])

    #Recursively sorts both halves and merges them
    flist = merge(mergesort(mlist1), mergesort(mlist2))
    return flist

#Gets input list and sorts it
def main():
    L1 = get_input_list()

    list_sorted = mergesort(L1)
    print(", ".join(str(x) for x in list_sorted))
main()