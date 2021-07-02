import {HttpClient, HttpParams} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable, BehaviorSubject} from 'rxjs';
import {map} from 'rxjs/operators';
// import {plainToClass} from 'class-transformer';

import {BaseService} from './base.service';

@Injectable({
  providedIn: 'root'
})
export class StatsService extends BaseService {
  constructor(protected http: HttpClient) {
    super(http);
  }

  getPlayerStats(): Observable<any> {
    const endpoint = `${this.baseUrl}/playerStats`;

    return this.get(endpoint).pipe(map(
      (data: Object) => {
          return data;
      },
      error => {
          return error;
      }
    ));
  }

  getPlayerShotStats(playerID?: number, teamID?: number, gameID?: number, gameDate?: string): Observable<any> {
    const endpoint = `${this.baseUrl}/playerShotStats`;
    let params: HttpParams = new HttpParams();

    if (playerID) {
      params = params.set('playerID', playerID);
    }
    
    if (teamID) {
      params = params.set('teamID', teamID);
    }

    if (gameID) {
      params = params.set('gameID', gameID);
    }

    if (gameDate) {
      params = params.set('gameDate', gameDate);
    }

    return this.get(endpoint, params).pipe(map(
      (data: Object) => {
          return {endpoint: endpoint + '?' + params.toString(), apiResponse: data};
      },
      error => {
          return error;
      }
    ));
  }
}