# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os



# Add a variable to load a file from a path.
                            #no need for the "..", and outer folder, because i am already in the resources foler
file_to_load = os.path.join("election_data.csv")
# Add a variable to save the file to a path.
                            #my files are at the same level
file_to_save = os.path.join("analysis", "election_analysis.txt")

####initalize count to 0 total votes
total_votes = 0

###county options and county votes
county_options = []
county_votes={}

#county_options.append({"county":"Arapahoe"})
#county_options.append({"county":"Denver"})
#county_options.append({"county":"Jefferson"})

county_votes={}

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)


    headers = next(file_reader)


    for row in file_reader:
        print(row)

    for row in file_reader:
        total_votes += 1

    county_name = row[1]

    if county_name not in county_options:
            # Add it to the list of countys.
        county_options.append("Arapahoe")
        county_options.append("Denver")
        county_options.append("Jefferson")

for vote_tally in range(len(county_votes)):

        #county_votes[0] = 0
    print(county_votes)

#Track the winning county, vote count and percentage
winning_county = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the county name from each row.
        county_name = row[1]

        # 3: Extract the county name from each row.


        # If the county does not match any existing county add it to
        # the county list
       

    # 6a: Write a for loop to get the county from the county dictionary.

        # 6b: Retrieve the county vote count.

        # 6c: Calculate the percentage of votes for the county.


with open(file_to_save, "w") as txt_file:

 if county_name not in county_options:

            # Add the county name to the county list.
            county_options.append(county_name)

            # And begin tracking that county's voter count.
            county_votes[county_name] = 0

        # Add a vote to that county's count
            county_votes[county_name] += 1

    print(county_name)
    txt_file.write(election_results)




    for county_name in county_votes:

 # Retrieve vote count and percentage
        votes =votes = county_votes.get(county_name)
        vote_percentage = int(votes) / int(total_votes) * 100
        county_results = (
        f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(county_results)
        txt_file.write(county_results)
    

         # 6e: Save the county votes to a text file.
    
    

        #winning county summary conditional statement 
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_county = county_name
            winning_percentage = vote_percentage

    # 7: Print the county with the largest turnout to the terminal.
# Print the winning county (to terminal)

        print(winning_county)
        txt_file.write(winning_county)


#winning county summary
winning_county_summary = (
  f"-------------------------\n"
        f"Winner: {winning_county}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
print(winning_county_summary)
txt_file.write(winning_county_summary)


    # 8: Save the county with the largest turnout to a text file.

    # Save the results to our text file.


    # Print the final vote count (to terminal)
election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
print(election_results, end="")
txt_file.write(election_results)


    # Save the final county vote count to the text file.
    #for county_name in county_name:
#
       







        # Print each county's voter count and percentage to the
        # terminal.
   
        #  Save the county results to our text file.
        #txt_file.write(county_results)



    # Print the winning county (to terminal)
   # winning_county_summary = (
  #f"-------------------------\n"
   #     f"Winner: {winning_county}\n"
   #     f"Winning Vote Count: {winning_count:,}\n"
   #     f"Winning Percentage: {winning_percentage:.1f}%\n"
   #     f"-------------------------\n")
   # print(winning_county_summary)
    # 
    # Save the winning county's name to the text file
    #txt_file.write(winning_county_summary)
