# -*- coding: utf-8 -*-
import logging
from functools import partial

from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler
from app.dbmodels import stats

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

        response = [{
            'playerID': player_id, 
            'teamID': team_id, 
            'gameID': game_id,
            'gameDate': game_date
        }]
        return Response(response)
