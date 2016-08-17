import { Injectable } from '@angular/core';
import { Headers, Jsonp, Http, URLSearchParams, Response  } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/from';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/publishReplay';
import 'rxjs/add/operator/toPromise';

/**
 * This class provides the Geocode service with methods to read names and add names.
 */
@Injectable()
export class AnalyzeService {

  /**
   * The array of initial names provided by the service.
   * @type {Array}
   */
  names = {};

  reqAdr: string = "판교";

  idxSource : number = 0;
  idxTarget : number = 0;

  routeResult: any[] = [];

  /**
   * Contains the currently pending request.
   * @type {Observable<string[]>}
   */
  //private request: Observable<string[]>;

  /**
   * Creates a new AnalyzeService with the injected Http.
   * @param {Http} http - The injected Http.
   * @constructor
   */
  constructor(private http: Http) {}

  CalcScore(sourecItems: any[], targetItems: any[] ){
    if(this.idxSource == 0 && this.idxTarget == 0){
      this.routeResult = [];
    }
    let startX = sourecItems[this.idxSource].mapx;
    let startY = sourecItems[this.idxSource].mapy;

    let endX = targetItems[this.idxTarget].mapx;
    let endY = targetItems[this.idxTarget].mapy;

    let headerV = new Headers();
    headerV.append('api-Type', 'SkpApi-Tmap-Routes')
    headerV.append('Content-Type', 'application/json');
    headerV.append('Target-URL', 'https://apis.skplanetx.com/tmap/routes');
    headerV.append('appkey', 'acd7926b-2fea-3457-915b-cdeb2b105fc5');
    let params = new URLSearchParams();
    params.set('version', '1'); // the user's search value
    params.set('endX', endX);
    params.set('endY', endY);
    params.set('startX', startX);
    params.set('startY', startY);
    params.set('reqCoordType', 'KATECH');
    return this.http.get('http://192.168.7.75:3000', { headers: headerV, search: params })
      .toPromise()
      .then((response: Response) => {
        var result = {
          fromTitle : sourecItems[this.idxSource].title[0],
          toTitle : targetItems[this.idxTarget].title,
          time :response.json().features[0].properties.totalTime
        }
        this.routeResult.push(result);
        this.idxTarget++;
        if( targetItems.length <= this.idxTarget ){
          this.idxSource++;
          this.idxTarget = 0;
        }

        if(sourecItems.length < this.idxSource + 1 ||
           targetItems.length < this.idxTarget + 1){
          this.idxSource = 0;
          this.idxTarget = 0;
          return;
        }
        else{
          this.CalcScore(sourecItems, targetItems);
        }
      }
        )
      .catch(this.handleError);
      //.map((response: Response) => response.json())
      //.map((data: string[]) => {
        //this.request = null;
        //console.log(data.result.items[0]);
        //return this.names = data.result.items;
      //}).publishReplay(1).refCount();
  //}
  }

  /**
   * Adds the given name to the array of names.
   * @param {string} value - The name to add.
   */

  private handleError(error: any) {
    console.error('An error occurred', error);
    return Promise.reject(error.message || error);
  }
}

