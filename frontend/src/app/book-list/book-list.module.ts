import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ListComponent } from './list/list.component';
import { SearchComponent } from './search/search.component';
import { BookListRoutingModule } from './book-list-routing.module';
import { MdButtonModule, MdCardModule, MdGridListModule, MdListModule } from '@angular/material';

@NgModule({
  imports: [
    CommonModule,
    BookListRoutingModule,
    MdGridListModule,
    MdListModule,
    MdCardModule,
    MdButtonModule,
  ],
  declarations: [ListComponent, SearchComponent]
})
export class BookListModule { }
