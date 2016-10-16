import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class ClientDataService {
    private apiUrl: string = '/api/all';
    private apiSourceIpUrl: string = '/api/source-ip';

    constructor(private http: Http) {

    }

    public getClientInfo(): Observable<Object> {
        return this.http.get(this.apiUrl)
            .map((res: Response) => res.json());
    }

    public getClientIp(): Observable<string> {
        return this.http.get(this.apiSourceIpUrl)
            .map((res: Response) => res['_body']);
    }
}
