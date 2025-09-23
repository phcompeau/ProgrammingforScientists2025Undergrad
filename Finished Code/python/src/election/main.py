import random  # for generating random numbers

def main():
	print("Let's simulate an election!")
def simulate_multiple_elections(electoral_votes: dict[str, int], polls: dict[str, float], 
                                num_trials: int, margin_of_error: float) -> tuple[float, float, float]:
    if num_trials <= 0:
         return ValueError
    if margin_of_error < 0:
         return ValueError
    
    win_count_1 = 0
    win_count_2 = 0
    tie_count = 0

    for i in range(num_trials):
        votes_1, votes_2 = simulate_one_election(polls, electoral_votes, margin_of_error)
        if votes_1 > votes_2:
            win_count_1 += 1
        elif votes_2 > votes_1:
            win_count_2 += 1
        else:
            tie_count += 1

    
def simulate_one_election(electoral_votes: dict[str, int], polls: dict[str, float], 
                                margin_of_error: float) -> tuple[int, int]:
    if margin_of_error < 0:
         raise ValueError("MOE cant be negative")
    college_votes_1 = 0
    college_votes_2 = 0
    
    def add_noise(polling_value: float, margin_of_error: float) -> float:
         x = random.gauss1(0, 1)
         polling_value += x
         x /= 2.0
         x *= margin_of_error
         polling_value += x
         return polling_value

    for state_name, polling_value in polls.items():
        num_votes = electoral_votes[state_name]
        adjusted_polling_value = add_noise(polling_value)

        if adjusted_polling_value > 0.5:
              college_votes_1 += num_votes
        else:
             college_votes_2 += num_votes
         
    
    return college_votes_1, college_votes_2

   



    
             
         
    probability_1 = win_count_1/num_trials
    probability_2 = win_count_2/num_trials
    probability_tie = tie_count/num_trials


if __name__ == "__main__":
    main()