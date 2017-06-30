import { Component, OnInit } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';
import { MdIconRegistry } from '@angular/material';

@Component({
  selector: 'app-side-nav',
  templateUrl: './entry.component.html',
  styleUrls: ['./entry.component.scss']
})
export class SideNavComponent implements OnInit {

  constructor(iconRegistry: MdIconRegistry, sanitizer: DomSanitizer) {
    iconRegistry.addSvgIcon(
      'dehaze',
      sanitizer.bypassSecurityTrustResourceUrl('assets/img/svg/ic_dehaze_white_24px.svg'));
  }

  ngOnInit() {
  }

}
