# your code goes here
def clean_file(path):
    new_file = open(path)
    split_line = []
    for line in new_file:
        line = line.rstrip()
        split_line.append(line.split(':'))
    return split_line

# print clean_file('scores.txt')

def mk_dict(path):
    split_line = clean_file(path)
    new_dict = {}
    for item in split_line:
        new_dict[item[0]] = item[1]
    print new_dict


#print mk_dict('scores.txt')

    

