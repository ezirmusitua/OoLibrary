import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { MainComponent } from './main/main.component';

@NgModule({
  imports: [RouterModule.forChild([
    { path: ':id', component: MainComponent }
  ])],
  exports: [RouterModule]
})
export class BookListRoutingModule {}
