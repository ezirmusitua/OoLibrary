import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SearchComponentComponent } from './search-component/search-component.component';
import { SearchCtrlComponent } from './search-ctrl/search-ctrl.component';
import { ListComponent } from './list/list.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [SearchComponentComponent, SearchCtrlComponent, ListComponent]
})
export class BookListModule { }
