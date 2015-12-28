import csv

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

with open('all.csv', 'rb') as f:
    rea = csv.reader(f, delimiter=',')
    for row in rea:
        all_posts = row[2].split()
        print str(map(get_amount_chars_together, all_posts))
