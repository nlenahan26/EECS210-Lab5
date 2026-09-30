# Name: Nathan Lenahan
# KUID: 3178995
# LAB Session (Day/Time): Wednesday 11am
# LAB Assignment: Lab 5
# Description:
#
#
#
# Collaborators/Sources:
import re

def get_input_list(prompt="Enter numbers (use spaces and/or commas): ") -> list[int]:
    user_input = input(prompt)
    # Split on commas or spaces (one or more of them)
    tokens = re.split(r"[,\s]+", user_input.strip())
    # Convert to integers, ignoring empty strings
    return [int(t) for t in tokens if t]

# Your Code Here

def merge(list1, list2):
    merged_list = []

    while len(list1) > 0 and len(list2) > 0:

        if list1[0] < list2[0]:
            merged_list.append(list1.pop(0))
        elif list2[0] < list1[0]:
            merged_list.append(list2.pop(0))

    
        if list1 == []:
            while len(list2) > 0:
                merged_list.append(list2.pop(0))

        if list2 == []:
            while len(list1) > 0:
                merged_list.append(list1.pop(0))

    return merged_list

def mergesort(entry_list):
    if len(entry_list) <= 1:
        return entry_list
    
    mlist1 = []
    mlist2 = []

    n = len(entry_list)
    if n > 1:
        m = n//2
        for x in range(m):
            mlist1.append(entry_list[x])

        for x in range(m, n):
            mlist2.append(entry_list[x])

    flist = merge(mergesort(mlist1), mergesort(mlist2))
    return flist



# Example usage
def main():
    L1 = get_input_list()
    print(f"Got: {L1}")

    print(mergesort(L1))
main()