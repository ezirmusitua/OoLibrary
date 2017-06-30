import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { SideNavComponent } from './side-nav/side-nav.component';
import { MdButtonModule, MdIconModule, MdSidenavModule } from '@angular/material';
import { HttpModule } from '@angular/http';
import { FlexLayoutModule } from '@angular/flex-layout';
import { RouterModule, Routes } from '@angular/router';
import { TestComponent } from './test.component';

const appRoutes: Routes = [
  { path: 'test', component: TestComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    SideNavComponent,
    TestComponent,
  ],
  imports: [
    BrowserModule,
    MdSidenavModule,
    MdIconModule,
    MdButtonModule,
    HttpModule,
    FlexLayoutModule,
    RouterModule.forRoot(
      appRoutes,
      { enableTracing: true } // <-- debugging purposes only
    )
    // other imports here
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
