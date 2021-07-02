import {ModuleWithProviders} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {PlayerStatsComponent} from './player-stats.component';


const routes: Routes = [
  { path: '', component: PlayerStatsComponent, data: { title: 'Player Stats'} },
];

export const routing: ModuleWithProviders<RouterModule> = RouterModule.forChild(routes);