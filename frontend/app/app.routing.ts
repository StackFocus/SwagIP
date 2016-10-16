import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { InfoTableComponent } from './info-table.component'

const appRoutes: Routes = [
    {
        path: ':tool',
        component: InfoTableComponent
    },
    {
        path: '',
        redirectTo: '/browser',
        pathMatch: 'full'
    }
];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);
