import { Component, OnInit } from '@angular/core';

// Add the RxJS Observable operators we need in this app.
import './rxjs-operators';
import { ClientDataService } from './client-data.service';

@Component({
    moduleId: module.id,
    selector: 'my-app',
    templateUrl: 'app.component.html',
    styleUrls: ['app.component.css']
})
export class AppComponent implements OnInit {
    title = 'AppComponent';
    ipAddress: any;
    tool: string;
    tabs: Array<Object> = [
        {displayName: 'Browser', name: 'browser'},
        {displayName: 'Wget', name: 'wget'},
        {displayName: 'Curl', name: 'curl'},
        {displayName: 'Fetch', name: 'fetch'},
        {displayName: 'PowerShell 3+', name: 'powershell'}
    ];

    constructor (private clientDataService: ClientDataService) {

    }

    ngOnInit() {
        this.clientDataService.getClientIp()
            .subscribe(value => this.ipAddress = value);
    }
}