import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { InfoTableComponent } from './info-table.component';
import { ClientDataService } from './client-data.service';
import { routing } from './app.routing';

@NgModule({
    imports: [ BrowserModule, HttpModule, routing ],
    providers: [ ClientDataService ],
    declarations: [ AppComponent , InfoTableComponent ],
    bootstrap: [ AppComponent ]
})
export class AppModule {}