import csv   # csv is a library within python that lets you read csv files


def process_electoral_votes(file_path):
    """
    takes in a file path woth the csv file with the first col as the state and the second col with how many votes tayt state gets.
    This will return a dictionary mapping states to how many votes they get.
    """

    result = dict()
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            state = row[0]
            votes = row[1]
            result[state] = votes
            print(row)

    return result



def process_poll_results(file_path):
    """
    Takes in a file path with the csv file woth first col = state, second col = canodate 1 results, third col = canidate 2 results, returns a dictionary mapping states to canidate results.
    dictionary key = state, value = c1 results.
    """

    result = dict()
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            state = row[0]
            c1_results = row[1]
            result[state] = c1_results

    return result
