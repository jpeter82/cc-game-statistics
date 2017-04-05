
import operator


def bubble_sort(List):
    '''
    Sorts the given List. Repeatedly go through the unsorted part of the array,
    comparing consecutive elements, and interchange them when they are out of order.
        @param List list The list to be sorted
        @return list The sorted list
    '''
    for i in range(len(List) - 1):
        for j in range(len(List) - 1):
            if List[j] > List[j + 1]:
                temp = List[j]
                List[j] = List[j + 1]
                List[j + 1] = temp
    return List


def bubble_sort_ci(List, order=True, ci=True):
    '''
    Same as bubble_sort(), but handles case sensitivity.
    It also supports sorting in ascending/descending order.
        @param List list The list to be sorted
        @param order bool True if ascending, False if descending
        @param ci bool True if case insensitive, otherwise False
        @return list The sorted list
    '''
    op = operator.gt if order else operator.lt
    for i in range(len(List) - 1):
        for j in range(len(List) - 1):
            if op((List[j].lower() if ci else List[j]), (List[j + 1].lower() if ci else List[j + 1])):
                temp = List[j]
                List[j] = List[j + 1]
                List[j + 1] = temp
    return List


def bubble_sort_nested(List, order=True):
    '''
    Sorts nested lists by 1st element of list of lists.
    It also supports sorting in ascending/descending order.
        @param List list The list to be sorted
        @param order bool True if ascending, False if descending
        @return list The sorted list
    '''
    op = operator.gt if order else operator.lt
    for i in range(len(List) - 1):
        for j in range(len(List) - 1):
            if op(List[j][0], List[j + 1][0]):
                temp = List[j]
                List[j] = List[j + 1]
                List[j + 1] = temp
    return List


def bubble_sort_nested_multi(List, order=[True, True]):
    '''
    Sorts nested lists by 1st then 2nd element of list of lists.
    It also supports sorting in ascending/descending order.
        @param List list The list to be sorted
        @param order bool True if ascending, False if descending
        @return list The sorted list
    '''
    op1 = operator.gt if order[0] else operator.lt
    op2 = operator.gt if order[1] else operator.lt
    for i in range(len(List) - 1):
        for j in range(len(List) - 1):
            if op1(List[j][0], List[j + 1][0]):
                temp1 = List[j]
                List[j] = List[j + 1]
                List[j + 1] = temp1
            if List[j][0] == List[j + 1][0] and op2(List[j][1], List[j + 1][1]):
                temp2 = List[j]
                List[j] = List[j + 1]
                List[j + 1] = temp2
    return List


def selection_sort(List):
    '''
    Sorts the given List. Repeatedly find the smallest element in the unsorted part of the array
    and swap it with the first element in the unsorted part of the array.
        @param List list The list to be sorted
        @return list The sorted list
    '''
    for i in range(len(List)):
        small_sub = i
        for j in range(i + 1, len(List)):
            if List[j] < List[small_sub]:
                small_sub = j
        temp = List[i]
        List[i] = List[small_sub]
        List[small_sub] = temp
    return List


def selection_sort_improved(List, order=True):
    '''
    Same as selection sort(), but it avoids swapping an element with itself.
    It also supports sorting in ascending/descending order.
        @param List list The list to be sorted
        @param order bool True if ascending, False if descending
        @return list The sorted list
    '''
    op = operator.lt if order else operator.gt
    for i in range(len(List)):
        small_sub = i
        for j in range(i + 1, len(List)):
            if op(List[j], List[small_sub]):
                small_sub = j
        if List[i] != List[small_sub]:
            temp = List[i]
            List[i] = List[small_sub]
            List[small_sub] = temp
    return List


def selection_sort_improved_ci(List, order=True, ci=True):
    '''
    Same as selection_sort_improved(), but also handles case sensitivity.
        @param List list The list to be sorted
        @param order bool True if ascending, False if descending
        @param ci bool True if case insensitive, otherwise False
        @return list The sorted list
    '''
    op = operator.lt if order else operator.gt
    for i in range(len(List)):
        small_sub = i
        for j in range(i + 1, len(List)):
            if op((List[j].lower() if ci else List[j]), (List[small_sub].lower() if ci else List[small_sub])):
                small_sub = j
        if (List[i].lower() if ci else List[i]) != (List[small_sub].lower() if ci else List[small_sub]):
            temp = List[i]
            List[i] = List[small_sub]
            List[small_sub] = temp
    return List


def insertion_sort(List):
    '''
    Sorts the given List. Go through the list and insert each element
    into the sorted part of the list where it belongs.
        @param List list The list to be sorted
        @return list The sorted list
    '''
    for i in range(len(List)):
        j = i
        while j > 0 and List[j] < List[j - 1]:
            temp = List[j]
            List[j] = List[j-1]
            List[j-1] = temp
            j = j - 1
    return List


def insertion_sort_ci(List, order=True, ci=True):
    '''
    Same as insertion_sort(), but handles case sensitivity.
    It also supports sorting in ascending/descending order.
        @param List list The list to be sorted
        @param order bool True if ascending, False if descending
        @return list The sorted list
    '''
    op = operator.lt if order else operator.gt
    for i in range(len(List)):
        j = i
        while j > 0 and op((List[j].lower() if ci else List[j]), (List[j - 1].lower() if ci else List[j - 1])):
            temp = List[j]
            List[j] = List[j-1]
            List[j-1] = temp
            j = j - 1
    return List


# The next two functions are here only if I cannot use the oprator module
# If you want to use it:
# replace this: op = operator.lt if order else operator.gt
# with this: op = less_xy if order else greater_xy
def greater_xy(x, y):
    return x > y


def less_xy(x, y):
    return x < y


def main():
    pass

if __name__ == '__main__':
    main()
    '''
    Testing = ['Render', 'Real-time strategy', 'First-person shooter', 'RPG', 'Render']

    print(sorted(Testing))
    print(selection_sort(Testing))
    print(selection_sort_improved(Testing, True))
    print(selection_sort_improved_ci(Testing, True, True))
    print(insertion_sort(Testing))
    print(insertion_sort_ci(Testing, True, True))
    print(bubble_sort(Testing))
    print(bubble_sort_ci(Testing, True, True))
    print(bubble_sort_ci(Testing, True, False))
    print(bubble_sort_ci(Testing, False, True))
    print(bubble_sort_ci(Testing, False, False))
    '''
