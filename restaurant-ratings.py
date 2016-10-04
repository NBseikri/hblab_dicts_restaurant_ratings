def clean_file(path):
    """Removes white space and splits file lines at : symbol"""
    new_file = open(path)
    split_line = []
    for line in new_file:
        line = line.rstrip()
        split_line.append(line.split(':'))
    return split_line


def mk_dict(path):
    """Creates dictionary of restaurant ratings"""
    split_line = clean_file(path)
    new_dict = {}
    for item in split_line:
        new_dict[item[0]] = item[1]
    return new_dict


def print_sorted_ratings(path):
    """Uses dictionary keys and values for alphabetized reviews"""
    rest_rating = mk_dict(path)
    sorted_ratings = sorted(rest_rating.keys())
    for key in sorted_ratings:
        print '%s is rated at %s.' % (key, rest_rating[key])

# sort_rating('scores.txt')

def add_rating(path):
    rest_rating = mk_dict(path)
    restaurant = raw_input("Please add a restaurant.")
    rest_rating[restaurant] = int(raw_input("How would you rate this restaurant?")) 
    return rest_rating

print add_rating('scores.txt')


