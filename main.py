import basketball
import audio
import any_sport

# get input from the user 
sport, team1, team2 = audio.main_func()

# call predictor function 
if sport.lower() == "basketball": basketball.main_func(team1, team2)
else: any_sport.predictor(team1, team2, sport)

