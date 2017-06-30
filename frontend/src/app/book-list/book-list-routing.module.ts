
import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { SearchComponent } from './search/search.component';
import { ListComponent } from './list/list.component';
@NgModule({
  imports: [RouterModule.forChild([
    { path: '', component: SearchComponent },
    { path: 'list', component: ListComponent}
  ])],
  exports: [RouterModule]
})
export class BookListRoutingModule {}
