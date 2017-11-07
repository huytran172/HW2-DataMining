from problem1 import elo_rating
import numpy as np
#-------------------------------------------------------------------------
'''
    Problem 2: 
    In this problem, you will use the Elo rating algorithm in problem 1 to rank the NCAA teams.
    You could test the correctness of your code by typing `nosetests test2.py` in the terminal.
'''

#--------------------------
def import_W(filename ='ncaa_results.csv'):
    '''
        import the matrix W of game results from a CSV file
        Input:
                filename: the name of csv file, a string 
        Output: 
                W: the game result matrix, a numpy integer matrix of shape (n by 2)
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    W = np.genfromtxt(filename, dtype='int', delimiter=',')
    #########################################
    return W

#--------------------------
def import_team_names(filename ='ncaa_teams.txt'):
    '''
        import a list of team names from a txt file. Each line of text in the file is a team name.
        Input:
                filename: the name of txt file, a string 
        Output: 
                team_names: the list of team names, a python list of string values, such as ['team a', 'team b','team c'].
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    with open(filename) as f:
        team_names = f.read().splitlines()
    #########################################
    return team_names

#--------------------------
def team_rating(resultfile = 'ncaa_results.csv', 
                teamfile='ncaa_teams.txt',
                K=16.):
    ''' 
        Rate the teams in the game results imported from a CSV file.
        (1) import the W matrix from `resultfile` file.
        (2) compute Elo ratings of all the teams
        (3) return a list of team names sorted by descending order of Elo ratings 

        Input: 
                resultfile: the csv filename for the game result matrix, a string.
                teamfile: the text filename for the team names, a string.
                K: a float scalar value, which is the k-factor of Elo rating system

        Output: 
                top_teams: the list of team names in descending order of their Elo ratings, a python list of string values, such as ['team a', 'team b','team c'].
                top_ratings: the list of elo ratings in descending order, a python list of float values, such as ['600.', '500.','300.'].
        
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    W = import_W(resultfile)
    team_names = import_team_names(teamfile)
    R = elo_rating(W, len(team_names), K)
    sorted_team_ids = [i[0] for i in sorted(enumerate(R), key=lambda x: x[1], reverse=True)]

    # {0: name, 1: name, 2: name ...}
    dict_team_names = {v: k for v, k in enumerate(team_names)}

    # {123: 0, 234: 1 ...}
    dict_sorted_team_ids = {k: v for v, k in enumerate(sorted_team_ids)}

    # Sort team names based on sorted team id
    sorted_pair_list = sorted(dict_team_names.items(), key=lambda x: dict_sorted_team_ids.get(x[0]))

    # Extract list of top_teams and top_ratings
    top_teams = list(zip(*sorted_pair_list)[1])
    top_ratings = sorted(R, reverse=True)

    #########################################
    return top_teams, top_ratings
