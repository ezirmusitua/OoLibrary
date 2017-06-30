import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MainComponent } from './main/main.component';
import { SettingRoutingModule } from './setting-routing.module';

@NgModule({
  imports: [
    CommonModule,
    SettingRoutingModule
  ],
  declarations: [MainComponent]
})
export class SettingModule { }
