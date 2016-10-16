import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';

import { ClientDataService } from './client-data.service';

@Component({
    moduleId: module.id,
    selector: 'app-info-table',
    templateUrl: 'info-table.component.html',
    styleUrls: ['info-table.component.css']
})
export class InfoTableComponent implements OnInit {
    clientInfo: Object;
    selectedTool: string;
    errorMessage: any;

    toolCommands: Object = {
        'wget': 'wget -qO -',
        'curl': 'curl',
        'fetch': 'fetch -qo -',
        'powershell': 'Invoke-RestMethod'
    };

    constructor (private clientDataService: ClientDataService,
                 private route: ActivatedRoute ) {}

    ngOnInit(): void {
        this.clientDataService.getClientInfo().subscribe(value => this.clientInfo = value);

        this.route.params.forEach((params: Params) => {
            this.selectedTool = params['tool'];
        });
    }

    getFirstColumn(): string {
        return this.selectedTool == 'browser' ? 'Item:' : 'Command:';
    }

    getCommand(key): string {
        if (this.selectedTool in this.toolCommands) {
            return this.toolCommands[this.selectedTool] + ' ' + this.clientInfo['host'] + '/api/' + key.toLowerCase();
        }
        else {
            throw('An unrecognized tool is selected')
        }
    }

    clientInfoJson(): Object {
        return JSON.stringify(this.clientInfo, null, '  ');
    }

    clientInfoKeys(): Array<string> {
        return Object.keys(this.clientInfo);
    }
}