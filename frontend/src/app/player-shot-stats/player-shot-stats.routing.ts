import {ModuleWithProviders} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {PlayerShotStatsComponent} from './player-shot-stats.component';


const routes: Routes = [
  { path: '', component: PlayerShotStatsComponent, data: { title: 'Player Shot Stats'} },
];

export const routing: ModuleWithProviders<RouterModule> = RouterModule.forChild(routes);