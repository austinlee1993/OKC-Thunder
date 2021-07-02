import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {PlayerStatsComponent} from './player-stats.component';
import {routing} from 'app/player-stats/player-stats.routing';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatCardModule} from '@angular/material/card';
import {FlexModule} from '@angular/flex-layout';
import {MatListModule} from '@angular/material/list';
import {MatRadioModule} from '@angular/material/radio';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {StatsService} from 'app/_services/stats.service';


@NgModule({
  declarations: [PlayerStatsComponent],
  imports: [
    CommonModule,
    routing,
    MatToolbarModule,
    MatCardModule,
    FlexModule,
    MatListModule,
    MatRadioModule,
    MatIconModule,
    MatButtonModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [StatsService],
  bootstrap: [PlayerStatsComponent],
})
export class PlayerStatsModule { }