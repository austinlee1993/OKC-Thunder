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