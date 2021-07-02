import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {PlayerShotStatsComponent} from './player-shot-stats.component';
import {routing} from 'app/player-shot-stats/player-shot-stats.routing';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatCardModule} from '@angular/material/card';
import {FlexModule} from '@angular/flex-layout';
import {MatListModule} from '@angular/material/list';
import {MatRadioModule} from '@angular/material/radio';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import {MatNativeDateModule} from '@angular/material/core';
import {MatDatepickerModule} from '@angular/material/datepicker';
import {StatsService} from 'app/_services/stats.service';


@NgModule({
  declarations: [PlayerShotStatsComponent],
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
    MatFormFieldModule,
    MatInputModule,
    ReactiveFormsModule,
    MatNativeDateModule,
    MatDatepickerModule
  ],
  providers: [StatsService],
  bootstrap: [PlayerShotStatsComponent],
})
export class PlayerShotStatsModule { }