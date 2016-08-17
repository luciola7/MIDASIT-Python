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
export class GeocodeService {

  /**
   * The array of initial names provided by the service.
   * @type {Array}
   */
  names = {};

  reqAdr: string = "판교";

  /**
   * Contains the currently pending request.
   * @type {Observable<string[]>}
   */
  //private request: Observable<string[]>;

  /**
   * Creates a new GeocodeService with the injected Http.
   * @param {Http} http - The injected Http.
   * @constructor
   */
  constructor(private http: Http) {}

  /**
   * Returns an Observable for the HTTP GET request for the JSON resource. If there was a previous successful request
   * (the local names array is defined and has elements), the cached version is returned
   * @return {string[]} The Observable for the HTTP request.
   */
  get(){
    //if (!this.request) {
      console.log('get');
      let headerV = new Headers();
      headerV.append('api-Type', 'NaverApi-Map-Geocode')
      headerV.append('Content-Type', 'application/json');
      headerV.append('Target-URL', 'https://openapi.naver.com/v1/map/geocode');
      headerV.append('X-Naver-Client-Id', 'YXS0h7yKOMXv0hjO59E2');
      headerV.append('X-Naver-Client-Secret', 'DHqT_iixro');
      let params = new URLSearchParams();
      params.set('encoding', 'utf-8'); // the user's search value
      params.set('coord', 'tm128');
      params.set('query', this.reqAdr);
      params.set('output', 'json');
      console.log(this.reqAdr);
      //this.http.get('http://127.0.0.1:3000', { headers: headerV, search: params })
      return this.http.get('http://192.168.7.75:3000', { headers: headerV, search: params })
        .toPromise()
        .then((response: Response) => {
          this.names = response.json()
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
  add(value: string): void {
    this.reqAdr = value;
    this.get();
    //this.names.push(value);
  }

  private handleError(error: any) {
    console.error('An error occurred', error);
    return Promise.reject(error.message || error);
  }
}

