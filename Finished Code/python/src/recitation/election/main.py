import random  # for generating random numbers
from election_io import *  # for reading from files

def main() :
	print("Let's simulate an election!") # reading csv files!

	electoral_votes_file_path = "data/electoralVotes.csv"
	electoral_votes = process_electoral_votes(electoral_votes_file_path)

	# print("electoral_votes", electoral_votes)

	print("electoral_votes", electoral_votes)







if __name__ == "__main__":
    main()

