import {
  ChangeDetectorRef,
  Component,
  OnDestroy,
  OnInit,
  ViewEncapsulation
} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {untilDestroyed, UntilDestroy} from '@ngneat/until-destroy';
import {StatsService} from './../_services/stats.service';

@UntilDestroy()
@Component({
  selector: 'player-stats-component',
  templateUrl: './player-stats.component.html',
  styleUrls: ['./player-stats.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
export class PlayerStatsComponent implements OnInit, OnDestroy {

  constructor(
    protected activatedRoute: ActivatedRoute,
    protected cdr: ChangeDetectorRef,
    protected statsService: StatsService,
  ) {

  }

  ngOnInit(): void {
    this.statsService.getPlayerStats().pipe(untilDestroyed(this)).subscribe(data => {
      console.log(data);
    });
  }

  ngOnDestroy() {
  }

}