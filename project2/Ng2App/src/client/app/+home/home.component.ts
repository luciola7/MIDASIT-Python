import { Component } from '@angular/core';
import { REACTIVE_FORM_DIRECTIVES } from '@angular/forms';

import { NameListService } from '../shared/index';
import { SearchService } from '../shared/index';
import { GeocodeService } from '../shared/index';

/**
 * for GeoCode
 */
export class GeoCode {
  x: string;
  y: string;
}

/**
 * This class represents the lazy loaded HomeComponent.
 */
@Component({
  moduleId: module.id,
  selector: 'sd-home',
  templateUrl: 'home.component.html',
  styleUrls: ['home.component.css'],
  directives: [REACTIVE_FORM_DIRECTIVES]
})
export class HomeComponent {

  newName: string = '판교';

  inputQuery: string = '마이다스아이티';

  /**
   * Creates an instance of the HomeComponent with the injected
   * NameListService.
   *
   * @param {NameListService} nameListService - The injected NameListService.
   */
  constructor(public nameListService: NameListService,
              public searchService: SearchService,
               public geocodeService: GeocodeService) {}

  /**
   * Calls the add method of the NameListService with the current newName value of the form.
   * @return {boolean} false to prevent default form submit behavior to refresh the page.
   */
  addName(): boolean {
    //this.nameListService.add(this.newName);
    console.log("addName");
    this.geocodeService.add(this.newName);
    this.newName = '';
    return false;
  }

  searchQuery() {
    console.log('searchQuery');
    this.searchService.searchQuery(this.inputQuery);
    this.inputQuery = '';
    console.log('searchQuery End');
  }

}
