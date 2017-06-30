import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

export const routes: Routes = [
  { path: '', redirectTo: 'search', pathMatch: 'full'},
  { path: 'search', loadChildren: 'app/book-list/book-list.module#BookListModule'},
  { path: 'book', loadChildren: 'app/book-detail/book-detail.module#BookDetailModule' },
  { path: 'setting', loadChildren: 'app/setting/setting.module#SettingModule' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { enableTracing: true })],
  exports: [RouterModule],
})
export class AppRoutingModule {
}
