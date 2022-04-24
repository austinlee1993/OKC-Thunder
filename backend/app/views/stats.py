# -*- coding: utf-8 -*-
import logging
from functools import partial

from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler
from app.dbmodels import stats
from django.db.models import Q

LOGGER = logging.getLogger('django')


class PlayerStats(APIView):
    logger = LOGGER

    def get(self, request):
        """Return all player stats"""
        player_stats = stats.PlayerStats.objects.all()

        return Response([player_stat.to_dict() for player_stat in player_stats.all()])



class PlayerShotStats(APIView):
    logger = LOGGER

    def get(self, request):

     
        """Return player shooting data"""
        player_id = request.query_params.get('playerID')
        team_id = request.query_params.get('teamID')
        game_id = request.query_params.get('gameID')
        game_date = request.query_params.get('gameDate')
        
        # TODO: Complete API response

        #query
        player_shot_stats = stats.PlayerShotStats.objects.filter(Q(nbapersonid = player_id) | Q(nbateamid = team_id) | Q(gameid = game_id) | Q(gametimestamp = game_date))
        
    
        overall_shot_list = [player_shot_stat.get_shots() for player_shot_stat in player_shot_stats.all()]
        two_shot_list = [player_shot_stat.get_twos() for player_shot_stat in player_shot_stats.all()]
        three_shot_list = [player_shot_stat.get_threes() for player_shot_stat in player_shot_stats.all()]
        made_two_shot_list = [player_shot_stat.get_twos_made() for player_shot_stat in player_shot_stats.all()]
        made_three_shot_list = [player_shot_stat.get_threes_made() for player_shot_stat in player_shot_stats.all()]      
              
        
        my_allshot_list = list(filter(None, overall_shot_list))
        my_2_list = list(filter(None, two_shot_list))
        my_3_list = list(filter(None, three_shot_list))
        my_2_made_list = list(filter(None, made_two_shot_list))
        my_3_made_list = list(filter(None, made_three_shot_list))


        ids = []

        for names in my_allshot_list:
            ids.append(names['nbaPersonID'])
        
        ids = list(set(ids))
        

        all_shots = len(my_allshot_list)
        two_shots = len(my_2_list)
        three_shots = len(my_3_list)
        made_two_shots = len(my_2_made_list)
        made_three_shots = len(my_3_made_list)
        
        
        response = [{
            'IDs of players who took shots': ids,
            'Percentage of shots taken from 3PT Range': three_shots/all_shots,
            '3PT FG%': made_three_shots/three_shots,
            '2PT FG%': made_two_shots/two_shots,
            'eFG%': (made_two_shots + (1.5 * made_three_shots))/all_shots
        }]
       
        return Response(response)
      
           
        
            
