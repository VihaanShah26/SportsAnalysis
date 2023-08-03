import openai
import time 

class weightages:
    win_percent = 90
    current_form = 10 

def predictor(team1, team2, sport):
    time.sleep(20)
    team1prob = 0 # probability that team 1 will win 
    team2prob = 0 # probability that team 2 will win 

    openai.api_key = "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"
    messages = [ {"role": "system", "content": 
              sport} ]

    # checking how many times team 1 has beaten team 2
    prompt1 = f"How many times has {team1} beaten {team2} in {sport}"
    messages.append(
            {"role": "user", "content": prompt1},
        )
    chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    team1win = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": team1win})

    #extracting the number of times team 1 has beaten team 2 
    num_team1win_list = num_from_string(team1win)
    for num in num_team1win_list: 
        if not num == 2021: num_team1win = num

    #checking how many times team 2 has beaten team 1
    prompt2 = f"How many times has {team2} beaten {team1} in {sport}"
    messages.append(
            {"role": "user", "content": prompt2},
        )
    chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    team2win = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": team2win})

    #extracting the number of times team 2 has beaten team 1
    num_team2win_list = num_from_string(team2win)
    for num in num_team2win_list: 
        if not num == 2021: num_team2win = num


    # calculating the win percentages of each team and adding that to the probability of each team winning 
    team1prob += num_team1win/(num_team1win + num_team2win) * weightages.win_percent
    team2prob += num_team2win/(num_team1win + num_team2win) * weightages.win_percent

    # adding a time delay to reduce number of calls per minute 
    time.sleep(20)

    # finding the current form of each team as Positive/Negative
    prompt3 = f"How has {team1} been performing recenty?"
    messages.append(
            {"role": "user", "content": prompt3},
        )
    chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    ans3 = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": ans3})
    
    prompt4 = f"How has {team2} been performing recently?"
    messages.append(
            {"role": "user", "content": prompt4},
        )
    chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    ans4 = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": ans4})

    team1form = positive_or_negative(ans3) # current form of team 1
    team2form = positive_or_negative(ans4) # current form of team 2

    # changing the winning probabilitiy for each team based on current form if they both do not have the same form 
    if not team1form == team2form:
        team1prob += team1form * weightages.current_form
        team2prob += team2form * weightages.current_form
    else: 
        team1prob = num_team1win/(num_team1win + num_team2win) * 100
        team2prob = num_team2win/(num_team1win + num_team2win) * 100

    print("--------------------Prediction--------------------")
    print(f"Probability of {team1} winning : {team1prob:.1f}")
    print(f"Probability of {team2} winning : {team2prob:.1f}")



# function used to extract numbers from a string which is returned by OpenAI
def num_from_string(string : str):
    result = [int(i) for i in string.split() if i.isdigit()]
    return result 

# function to determine if a statement if positive or negative -- sentiment analysis 
def positive_or_negative(string : str):
    model_engine = "text-davinci-002"
    prompt = f"Classify the sentiment of the following statement as positive or negative:\n\n{string}\n\nPositive\nNegative"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.0,
    )
    sentiment = response.choices[0].text.strip().lower()

    if sentiment == "positive": return 1
    elif sentiment == "negative": return -1
    
