import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def is_number(c):
    try:
        int(c)
        return True
    except ValueError:
        return False

def get_amount_chars_together(st):
    total = 0
    previous_was_char = False
    for c in st:
        if not is_number(c):
            if not previous_was_char:
                total = total + 1
            previous_was_char = True
        else:
            previous_was_char = False
    return total

def get_index_biggest_list(total_list):
    biggest_len = 0 
    biggest_index = -1
    for index, item in enumerate(total_list):
        if len(item) > biggest_len:
            biggest_index = index
            biggest_len = len(item)
    return biggest_index

def main():
    total_lists = []
    with open('all.csv', 'rb') as f:
        rea = csv.reader(f, delimiter=',')
        for row in rea:
            all_posts = row[2].split()
            total_lists.append(map(get_amount_chars_together, all_posts))

    biggest_list_index = get_index_biggest_list(total_lists)
    elements = [[] for x in range(0, len(total_lists[biggest_list_index]))]
    for l in total_lists:
        for x in range(0, len(total_lists[biggest_list_index])):
            if len(l) > x:
                elements[x].append(l[x])

    for index, element in enumerate(elements):
        plt.hist(element, bins = 50,range = (0,20), alpha = 0.75)
        plt.savefig('out/' + str(index))
        plt.clf()

if __name__ == '__main__':
    main()
