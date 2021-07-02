import {ModuleWithProviders} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'player-stats', },
  { path: 'player-stats', loadChildren: () => import('./player-stats/player-stats.module').then(m => m.PlayerStatsModule), data: {preload: true}},
  { path: 'player-shot-stats', loadChildren: () => import('./player-shot-stats/player-shot-stats.module').then(m => m.PlayerShotStatsModule), data: {preload: true}},
  { path: '**', redirectTo: 'player-stats'}
];

export const routing: ModuleWithProviders<RouterModule> = RouterModule.forRoot(routes, { relativeLinkResolution: 'legacy' });
