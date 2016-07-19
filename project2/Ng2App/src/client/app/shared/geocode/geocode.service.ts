import { Injectable } from '@angular/core';
import { Headers, Jsonp, Http, URLSearchParams, Response  } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/from';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/publishReplay';

/**
 * This class provides the Geocode service with methods to read names and add names.
 */
@Injectable()
export class GeocodeService {

  /**
   * The array of initial names provided by the service.
   * @type {Array}
   */
  names: string[] = [];

  /**
   * Contains the currently pending request.
   * @type {Observable<string[]>}
   */
  private request: Observable<string[]>;

  /**
   * Creates a new GeocodeService with the injected Http.
   * @param {Http} http - The injected Http.
   * @constructor
   */
  constructor(private jsonp: Http) {}

  /**
   * Returns an Observable for the HTTP GET request for the JSON resource. If there was a previous successful request
   * (the local names array is defined and has elements), the cached version is returned
   * @return {string[]} The Observable for the HTTP request.
   */
  get(): Observable<string[]> {
    //if (!this.request) {
    let headerV = new Headers();
      //'encoding': 'utf-8',
      //'coord': 'latlng',
      //'output': 'json',
      //'query' : 'Midas',
      //'Content-Type': 'application/json',
      //'Access-Control-Allow-Origin' : '*',
      //'Host' : 'openapi.naver.com',
      //'Accept': '*/*',
      //'X-Naver-Client-Id': '---',
      //'X-Naver-Client-Secret': '---'
    //});
    headerV.append('Content-Type', 'application/javascript');
    //headerV.append('Access-Control-Allow-Origin', '*');
    headerV.append('X-Naver-Client-Id', '---');
    headerV.append('X-Naver-Client-Secret', '---');
    let params = new URLSearchParams();
    //params.set('Content-Type', 'application/javascript');
    params.set('X-Naver-Client-Id', '---');
    params.set('X-Naver-Client-Secret', '---');
    params.set('encoding', 'utf-8'); // the user's search value
    params.set('coord', 'latlng');
    params.set('query', 'MIDAS');
    params.set('output', 'json');
    params.set('callback', 'JSONP_CALLBACK');
    //this.request = this.http.get('https://openapi.naver.com/v1/map/geocode', { headers: headers})
          //.map(request => <string[]> request.json()[1]);
         // this.jsonp.get('https://openapi.naver.com/v1/map/geocode', { headers: headerV, search: params })
        //  .map(res => console.log(res.json()));
    this.request = this.jsonp.get('https://openapi.naver.com/v1/map/geocode', { headers: headerV, search: params })
      .map(request => <string[]> request.json()[1]);
     // .map((response: Response) => response.json())
     // .map((data: string[]) => {
     //     this.request = null;
     //     return this.names = data;
     // }).publishReplay(1).refCount();
    //}
    return this.request;
  }

  /**
   * Adds the given name to the array of names.
   * @param {string} value - The name to add.
   */
  add(value: string): void {
    this.names.push(value);
  }
}

