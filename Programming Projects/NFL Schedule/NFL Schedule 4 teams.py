import random
import math

class Scheduler:

    def __init__(self, num_weeks):
	    self.num_teams = 4
	    self.num_weeks = num_weeks
	    self.teams = ['Lions','Bears','Packers','Vikings']
	    self.teams_played = []
	    self.schedule = []
	    
    def set_teams(self):
	    '''Prompt user for number of teams and their names.'''

##	    self.num_teams = int(input("Enter number of teams: "))
	    
	    # ask user num_teams times for a team name
##	    for i in range(self.num_teams):
##	        # get team name and save to teams
##	        self.teams.append(input("Enter team name {}: ".format(i)))
	        
	    self.teams_played = [[False] * self.num_teams for i in range(self.num_teams)]

	    # set all teams True for own list to not play themselves
	    for idx in range(self.num_teams):
	        self.teams_played[idx][idx] = True
    
    def pick_random_team(self, scheduled):
	    '''Pick random team that has not been scheduled.'''
	    team = random.randint(0, self.num_teams - 1)

	    # check if team is scheduled
	    while scheduled[team]:
	        team = random.randint(0, self.num_teams - 1)
	    
	    return team
  
    def create_schedule(self):
	    '''Create schedule.'''
	    self.schedule = [[] for i in range(self.num_weeks)]
	    
	    for week in range(self.num_weeks):
	        # track which teams have been scheduled for the week
	        scheduled = [False] * self.num_teams
	        
	        while(not all(scheduled)):
	            # pick a random home and opp team
	            home = self.pick_random_team(scheduled)
	            opp  = self.pick_random_team(scheduled)
	            
	            # pick new opponent if team is already played
	            while(self.teams_played[home][opp] or self.teams_played[opp][home]):
	                opp = self.pick_random_team(scheduled)
	                
	            # set teams to have played each other
	            self.teams_played[home][opp] = True
	            self.teams_played[opp][home] = True
	            
	            # set teams to be scheduled
	            scheduled[home] = True
	            scheduled[opp]  = True
	            
	            # add game to schedule
	            self.schedule[week].append([home, opp])

    def __str__(self):
        '''Print schedule in terms of team names.'''
	
	# check if a schedule has been created
        if not self.schedule:
            return "Schedule hasn't been made yet!"
	    	
        output = ""
        
        # loop through each week
        for week_num, week in enumerate(self.schedule): 
            output += "Week: " + str(week_num + 1) + '\n'
            # loop through each game
            for game_num, game in enumerate(week):
                # print game number of that week
                home = self.teams[game[0]]
                opp  = self.teams[game[1]]

                output += '\tGame: ' + str(game_num + 1)
                output += ' ' + home + ' v. ' + opp + '\n'       
        return output
if __name__ == '__main__':
    num_weeks = 3
    schedule1 = Scheduler(num_weeks)
    schedule1.set_teams()
    schedule1.create_schedule()
    print(schedule1)

