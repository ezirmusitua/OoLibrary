import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SearchCtrlComponent } from './search-ctrl/search-ctrl.component';
import { ListComponent } from './list/list.component';
import { MainComponent } from './main/main.component';
import { BookListRoutingModule } from './book-list-routing.module';
import { MdGridListModule } from '@angular/material';

@NgModule({
  imports: [
    CommonModule,
    BookListRoutingModule,
    MdGridListModule,
  ],
  declarations: [SearchCtrlComponent, ListComponent, MainComponent]
})
export class BookListModule { }
