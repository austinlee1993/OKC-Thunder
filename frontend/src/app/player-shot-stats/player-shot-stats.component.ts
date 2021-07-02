import {
  ChangeDetectorRef,
  Component,
  OnDestroy,
  OnInit,
  ViewEncapsulation
} from '@angular/core';
import * as moment from 'moment';
import {ActivatedRoute} from '@angular/router';
import {untilDestroyed, UntilDestroy} from '@ngneat/until-destroy';
import {StatsService} from '../_services/stats.service';

@UntilDestroy()
@Component({
  selector: 'player-shot-stats-component',
  templateUrl: './player-shot-stats.component.html',
  styleUrls: ['./player-shot-stats.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
export class PlayerShotStatsComponent implements OnInit, OnDestroy {

  endpoint: any;
  apiResponse: any;
  playerID: number;
  teamID: number;
  gameID: number;
  gameDate: string;

  constructor(
    protected activatedRoute: ActivatedRoute,
    protected cdr: ChangeDetectorRef,
    protected statsService: StatsService,
  ) {

  }

  ngOnInit(): void {
    this.fetchApiResponse();
  }

  changeParams(): void {
    this.fetchApiResponse();
  }

  fetchApiResponse(): void {
    let momentDate = null;
    if (this.gameDate) {
      momentDate = new Date(this.gameDate);
    }
    let formattedDate = momentDate ? moment(momentDate).format("MM-DD-YYYY") : null;
    this.statsService.getPlayerShotStats(this.playerID, this.teamID, this.gameID, formattedDate).pipe(untilDestroyed(this)).subscribe(data => {
      this.endpoint = data.endpoint;
      this.apiResponse = JSON.stringify(data.apiResponse, null, 2);
    });
  }

  ngOnDestroy() {
  }

}