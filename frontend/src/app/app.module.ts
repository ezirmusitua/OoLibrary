import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { SideNavComponent } from './entry/entry.component';
import { MdButtonModule, MdIconModule, MdSidenavModule } from '@angular/material';
import { HttpModule } from '@angular/http';
import { FlexLayoutModule } from '@angular/flex-layout';
import { TestComponent } from './test.component';
import { AppRoutingModule } from './app-routing.module';
import { SettingModule } from './setting/setting.module';
import { BookListModule } from './book-list/book-list.module';
import { BookDetailModule } from './book-detail/book-detail.module';


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
    AppRoutingModule,
    SettingModule,
    BookListModule,
    BookDetailModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
