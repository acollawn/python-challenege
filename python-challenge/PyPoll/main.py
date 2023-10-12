# Dependencies
import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')
election_text_analysis = os.path.join("analysis", "election_analysis.txt")

# First - find total votes
total_votes = 0

# Second - find unique candidates and their performance
unique_candidates =[]
candidate_votes = {}

# Third - determine the winner
winner_vote_total = 0
winner = ""

total_votes =+ 1

# Read in the CSV file
# Info needed from csv are the unique values and the count
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)

    # Extract the first title row and start reading data from second row
    title_row = next(csvreader)

    # The total number of votes cast
    for vote_count in csvreader:
        total_votes += 1

        # Assign the index with the names to a variable
        candidates = vote_count[2]

        # Determine how to keep track of votes for each unique candidate
        if candidates not in unique_candidates:
            unique_candidates.append(candidates)

            # Establish the candidate vote count as an integer value
            candidate_votes[candidates] = 0

        # Count the number of times each candidate is listed to tally the votes
        candidate_votes[candidates] += 1
    print(total_votes)
    print(candidate_votes)

# Write a file (election_text_analysis)to print the results
# Make sure to write items into election_text_analysis in order - each part is its own piece
with open(election_text_analysis, "w") as file:

    # Format the header
    analysis_header = (
        f"\nElection Results\n\n"
        f"-----------------------\n\n"
    )
    # Write the header into the file
    file.write(analysis_header)

    # Format the total votes
    official_vote_total = (
        f"Total Votes: {total_votes}\n\n"
        f"-----------------------\n\n"
        )
    # Write in the total votes into the file
    file.write(official_vote_total)

    # Each candidate name, their personal count, and the percentage of votes they received
    for name in candidate_votes:
        individuals_vote_count = candidate_votes.get(name)
        percentage_of_votes = round(individuals_vote_count/total_votes * 100, 3) 
       
        #Format the standings
        official_standings = (
            f"{name}: {percentage_of_votes}% ({individuals_vote_count})\n\n"
            )
        print(official_standings)

        #Write in the official standings into the file
        file.write(official_standings)
    
        #Determine the winner
        if individuals_vote_count > winner_vote_total:
            winner = name
            winner_vote_total = individuals_vote_count
    print(winner)

    #format the officiall winner
    official_winner = (
        f"-----------------------\n\n"
        f"Winner: {winner}\n\n"
        f"-----------------------\n\n"
        )

    #write in the offical winner into the file
    file.write(official_winner)
