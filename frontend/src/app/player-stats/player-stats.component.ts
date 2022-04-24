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

  playerData = null;  
  totalGames = null;
  totalFT = null;
  totalAst = null;
  totalBlocks = null;
  total3Taken = null;
  total3Made = null;
  totalShots = null;
  total2Made = null;


  constructor(
    protected activatedRoute: ActivatedRoute,
    protected cdr: ChangeDetectorRef,
    protected statsService: StatsService,
  ) {

  }

  ngOnInit(): void {
    this.statsService.getPlayerStats().pipe(untilDestroyed(this)).subscribe(data => {
      
     
      
      this.playerData = data;
      this.totalGames = 82;

      data.forEach(player => {
      
        
        this.totalFT += player.ftMade + player.ftMissed;
        this.totalAst += player.assists;
        this.totalBlocks += player.blocks;
        this.total3Taken += player.fg3Made + player.fg3Missed;
        this.total3Made += player.fg3Made;
        this.total2Made += player.fg2Made;
        this.totalShots += player.fgMade +  player.fgMissed;
      });

     

      
    });
  }

  ngOnDestroy() {
  }

}