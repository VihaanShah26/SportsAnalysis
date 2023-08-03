# SportsAnalysis
This is a sports analysis software which uses past data to predict the winner of any two teams in any sporting event. 

For basketball, I have collected detailed information about all matches for the last 10 years. The algorithm takes into account how the team has performed, how many baskets they have scored, how the team's opponents have performed in the rest of the season and then determines the probability of each team winning. 

For any other sport, I have used the OpenAI API to collect information about the two teams' past encounters (prior to September 2021). I have also generated a summary of the team's performance over the years and I then perform sentiment analysis on this summary to determine whether it is positive or negative. These factors are taken into account by the algorithm that predicts the probability of each team winning. 

The user interacts with the software through voice which makes it easier to use and more user-friendly. 

## Future Developments 
Since the data provided by OpenAI is only prior to Sept 2021, the most recent data cannot be taken into account for sports other than basketball. I plan to build a Large Language Model on top of ChatGPT to provide more recent data and make the predictions for any random sport more accurate. 

## Conclusion
The sports analysis system has successfully prediced the outcome of 5 out of 5 NBA games in the 2023 season and 3 out of 4 IPL cricket games in 2023. 
