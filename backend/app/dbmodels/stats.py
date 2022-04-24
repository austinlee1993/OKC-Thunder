# -*- coding: utf-8 -*-
"""Contains models related to stats"""
from django.db import models

class PlayerStats(models.Model):
    """
    Season level box score statistics for players
    """
    class Meta:
        db_table = 'player_stats'
        
    
    id = models.BigAutoField(primary_key=True, db_index=True)
    player_id = models.IntegerField(null=False, db_index=True)
    games_played = models.IntegerField(null=False, db_index=True)
    games_on_roster = models.IntegerField(null=False, db_index=True)
    seconds_played = models.FloatField(null=False, db_index=True)
    points = models.IntegerField(null=False, db_index=True)
    reb_offensive = models.IntegerField(null=False, db_index=True)
    reb_defensive = models.IntegerField(null=False, db_index=True)
    assists = models.IntegerField(null=False, db_index=True)
    steals = models.IntegerField(null=False, db_index=True)
    turnovers = models.IntegerField(null=False, db_index=True)
    blocks = models.IntegerField(null=False, db_index=True)
    ft_made = models.IntegerField(null=False, db_index=True)
    ft_missed = models.IntegerField(null=False, db_index=True)
    fg_made = models.IntegerField(null=False, db_index=True)
    fg_missed = models.IntegerField(null=False, db_index=True)
    fg2_made = models.IntegerField(null=False, db_index=True)
    fg2_missed = models.IntegerField(null=False, db_index=True)
    fg3_made = models.IntegerField(null=False, db_index=True)
    fg3_missed = models.IntegerField(null=False, db_index=True)

    

    def to_dict(self):
        
        return dict(
            id=self.id,
            playerID=self.player_id,
            gamesPlayed=self.games_played,
            gamesOnRoster=self.games_on_roster,
            secondsPlayed=self.seconds_played,
            points=self.points,
            rebOffensive=self.reb_offensive,
            rebDefensive=self.reb_defensive,
            assists=self.assists,
            steals=self.steals,
            turnovers=self.turnovers,
            blocks=self.blocks,
            ftMade=self.ft_made,
            ftMissed=self.ft_missed,
            fgMade=self.fg_made,
            fgMissed=self.fg_missed,
            fg2Made=self.fg2_made,
            fg2Missed=self.fg2_missed,
            fg3Made=self.fg3_made,
            fg3Missed=self.fg3_missed,
        )

class PlayerShotStats(models.Model):
    """
    PlayerShot Stats
    """
    class Meta:
        db_table = 'play_by_play'
        
    
    leagueid = models.BigIntegerField(null=False, db_index=True)
    leaguename = models.TextField(null=False, db_index=True)
    seasontype = models.TextField(null=False, db_index=True)
    gametimestamp = models.DateTimeField(null=False, db_index=True)
    homenbateamid = models.IntegerField(null=False, db_index=True)
    hometeamname = models.TextField(null=False, db_index=True)
    awaynbateamid = models.IntegerField(null=False, db_index=True)
    awayteamname = models.TextField(null=False, db_index=True)
    nbateamid = models.IntegerField(null=False, db_index=True)
    nbapersonid = models.IntegerField(null=False, db_index=True)
    nbapersonname = models.TextField(null=False, db_index=True)
    eventid = models.IntegerField(null=False, db_index=True)     
    period = models.IntegerField(null=False, db_index=True)  
    minutesecond = models.TimeField(null=False, db_index=True)       
    points = models.IntegerField(null=False, db_index=True)
    blockedshot = models.IntegerField(null=False, db_index=True)   
    rebdefensive = models.IntegerField(null=False, db_index=True)
    fg3attempted = models.IntegerField(null=False, db_index=True)
    assist = models.IntegerField(null=False, db_index=True)
    ftmade = models.IntegerField(null=False, db_index=True)    
    fgmade = models.IntegerField(null=False, db_index=True)
    fgattempted = models.IntegerField(null=False, db_index=True)
    fg2attempted = models.IntegerField(null=False, db_index=True)
    ftattempted = models.IntegerField(null=False, db_index=True)
    turnover = models.IntegerField(null=False, db_index=True)
    fg2made = models.IntegerField(null=False, db_index=True)
    reboffensive = models.IntegerField(null=False, db_index=True)
    fg3made = models.IntegerField(null=False, db_index=True)
    gameid = models.BigAutoField(primary_key=True, db_index=True) 



    def get_shots(self):

        if self.fgattempted > 0:

            return dict(
                
                fgAttempted=self.fgattempted,      
                nbaPersonID = self.nbapersonid,                     
                
            )
        else:
            return None
    
    def get_twos(self):

        if self.fg2attempted > 0:

            return dict(                  
                    
                    fg2Attempted = self.fg2attempted,                              
                    
                )
        else:
            return None

        
    def get_threes(self):

        if self.fg3attempted > 0:

            return dict(                  
                    
                    fg3Attempted = self.fg3attempted,                              
                    
                )
        else:
            return None
    
    def get_twos_made(self):

        if self.fg2made > 0:

            return dict(                  
                    
                    fg2Made = self.fg2made,                              
                    
                )
        else:
            return None
    
    def get_threes_made(self):

        if self.fg3made > 0:

            return dict(                  
                    
                    fg3Made = self.fg3made,                              
                    
                )
        else:
            return None



        
