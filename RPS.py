# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. 
# It is not a very good player so you will need to change the code to pass the challenge.
import random

def player(prev_play, opponent_history=[]):

    # Lookup for the opposite response to opponents predicted next move
    OPP = {
        'R':'P',
        'P':'S',
        'S':'R'
    }
    
    # If empty string supplied as previ play, clear the array, otherwise append value.
    if(prev_play == ""):
        opponent_history.clear()
    else: 
        opponent_history.append(prev_play)

    # Assign guess as a random value
    guess = ['R','P','S'][random.randint(0,2)]

    # If more than 11 plays have been played, try looking for patterns
    if (len(opponent_history) >= 11):

        # Check the last 10 plays and see if that sequence has been used before, 
        # and if found, play opposite the next value the opponent previously played
        recent = opponent_history[-10:]
        
        for x in range( len(opponent_history) - 11 ):
            history = opponent_history[x:x+10]
            
            if all(recent[i] == history[i] for i in range(10)): 
                guess = opponent_history[x+10]
                return OPP[guess]

        # If no 10 length patterns were found, try a 4 length pattern
        recent = opponent_history[-4:]
        
        for x in range( len(opponent_history) - 5 ):
            history = opponent_history[x:x+4]
            
            if all(recent[i] == history[i] for i in range(4)): 
                guess = opponent_history[x+4]
                return OPP[guess]

    
        # If no pattern found, build a probability of most common play after most recent 3 plays
        prob_chart = {}
        recent = opponent_history[-2:]
        for x in range(len(opponent_history) - 3):
            if opponent_history[x] == recent[0] and opponent_history[x+1] == recent[1]:
                prob_chart[opponent_history[x+2]] = prob_chart.get(opponent_history[x+2], 0) + 1
         
        if (prob_chart):
            return OPP[max(prob_chart, key=prob_chart.get)]

        # If no pattern found, build a probability of most common play after most recent play
        #prob_chart = {}
        #for x in range(len(opponent_history) - 1):
        #    if opponent_history[x] == prev_play:
        #        prob_chart[opponent_history[x+1]] = prob_chart.get(opponent_history[x+1], 0) + 1
         
        #if (prob_chart):
        #    return OPP[max(prob_chart, key=prob_chart.get)]
        
        # If no pattern found, reply opposite of what this players most common response is
        #most_common = { 'S': opponent_history.count('S'),'P':opponent_history.count('P'),'R':opponent_history.count('R')}
        #return OPP[max(most_common, key=most_common.get)]

    # If no pattern found, return random guess
    return guess



