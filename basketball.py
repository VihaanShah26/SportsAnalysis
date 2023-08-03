import csv 

class weightages:
    team = 75
    opp = 25

def past_encounters(year_extension, team1, team2):
    filename1 = f"/Users/vihaan/Desktop/Northwestern/KTP/Capstone Project/Program/basketball{year_extension}team.csv"
    filename2 = f"/Users/vihaan/Desktop/Northwestern/KTP/Capstone Project/Program/basketball{year_extension}opp.csv"
    
    # opening the team csv file
    with open(filename1) as file1:
        teams = file1.readlines() # this returns all the lines of the file as a list 

    # opening the opponent csv file 
    with open(filename2) as file2:
        opps = file2.readlines() # this returns all the lines of the file as a list 
    # now both the csv files for that year have been opened 

    #calculate how many points each team has scored against each other  
    team1pts = 0 # how many points has team 1 scored
    opp1pts = 0
    team2pts = 0 # how many points has team 2 scored
    opp2pts = 0

    for i in range(1,30): # starting from 1 because first line of the csv files has the titles 
        
        teams_line = teams[i].split(",") #splitting a line of the team file 
        opps_line = opps[i].split(",") #splitting a line of the opp file 

        if team1.lower() in teams_line[1].lower():
            team1pts = float(teams_line[-1])
        if team2.lower() in teams_line[1].lower():
            team2pts = float(teams_line[-1])
        if team1.lower() in opps_line[1].lower():
            opp1pts = float(opps_line[-1])
        if team2.lower() in opps_line[1].lower():
            opp2pts = float(opps_line[-1])
        
    
    return [team1pts, opp1pts, team2pts, opp2pts]



# the main program which calls the above method with all the year values 
def main_func(team1, team2):
    #defining the variables to count all points 
    team1_avg = 0
    opp1_avg = 0
    team2_avg = 0
    opp2_avg = 0

    team1_result, opp1_result, team2_result, opp2_result = past_encounters("_2022_23_", team1, team2)
    team1_avg += team1_result
    opp1_avg += opp1_result
    team2_avg += team2_result
    opp2_avg += opp2_result

    team1_result, opp1_result, team2_result, opp2_result = past_encounters("_2021_22_", team1, team2)
    team1_avg += team1_result
    opp1_avg += opp1_result
    team2_avg += team2_result
    opp2_avg += opp2_result

    team1_result, opp1_result, team2_result, opp2_result = past_encounters("_2020_21_", team1, team2)
    team1_avg += team1_result
    opp1_avg += opp1_result
    team2_avg += team2_result
    opp2_avg += opp2_result

    team1_result, opp1_result, team2_result, opp2_result = past_encounters("_2021_22_", team1, team2)
    team1_avg += team1_result
    opp1_avg += opp1_result
    team2_avg += team2_result
    opp2_avg += opp2_result

    team1_result, opp1_result, team2_result, opp2_result = past_encounters("_2020_21_", team1, team2)
    team1_avg += team1_result
    opp1_avg += opp1_result
    team2_avg += team2_result
    opp2_avg += opp2_result

    team1_result, opp1_result, team2_result, opp2_result = past_encounters("_2019_20_", team1, team2)
    team1_avg += team1_result
    opp1_avg += opp1_result
    team2_avg += team2_result
    opp2_avg += opp2_result

    team1_result, opp1_result, team2_result, opp2_result = past_encounters("_2018_19_", team1, team2)
    team1_avg += team1_result
    opp1_avg += opp1_result
    team2_avg += team2_result
    opp2_avg += opp2_result

    team1_result, opp1_result, team2_result, opp2_result = past_encounters("_2017_18_", team1, team2)
    team1_avg += team1_result
    opp1_avg += opp1_result
    team2_avg += team2_result
    opp2_avg += opp2_result

    team1_result, opp1_result, team2_result, opp2_result = past_encounters("_2016_17_", team1, team2)
    team1_avg += team1_result
    opp1_avg += opp1_result
    team2_avg += team2_result
    opp2_avg += opp2_result

    team1_result, opp1_result, team2_result, opp2_result = past_encounters("_2015_16_", team1, team2)
    team1_avg += team1_result
    opp1_avg += opp1_result
    team2_avg += team2_result
    opp2_avg += opp2_result

    team1_result, opp1_result, team2_result, opp2_result = past_encounters("_2014_15_", team1, team2)
    team1_avg += team1_result
    opp1_avg += opp1_result
    team2_avg += team2_result
    opp2_avg += opp2_result

    team1_result, opp1_result, team2_result, opp2_result = past_encounters("_2013_14_", team1, team2)
    team1_avg += team1_result
    opp1_avg += opp1_result
    team2_avg += team2_result
    opp2_avg += opp2_result
    # all the averages have been added up and data has been collected 


    #formula for making the prediction 
    team1prob = team1_avg/(team1_avg+team2_avg) * weightages.team
    team1prob += opp1_avg/(opp1_avg+opp2_avg) * weightages.opp

    team2prob = team2_avg/(team1_avg+team2_avg) * weightages.team
    team2prob += opp2_avg/(opp1_avg+opp2_avg) * weightages.opp
    
    print("--------------------Prediction--------------------")
    print(f"Probability of {team1} winning: {team1prob:.1f}%")
    print(f"Probability of {team2} winning: {team2prob:.1f}%")
