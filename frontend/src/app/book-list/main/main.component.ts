import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {
  tiles = [
    {text: 'One', cols: 1, rows: 1, color: 'lightblue'},
    {text: 'Two', cols: 1, rows: 1, color: 'lightgreen'},
    {text: 'Three', cols: 1, rows: 1, color: 'lightpink'},
    {text: 'Four', cols: 1, rows: 1, color: '#DDBDF1'},
    {text: 'Five', cols: 1, rows: 1, color: 'lightblue'},
    {text: 'Six', cols: 1, rows: 1, color: 'lightgreen'},
    {text: 'Seven', cols: 1, rows: 1, color: 'lightpink'},
    {text: 'Eight', cols: 1, rows: 1, color: '#DDBDF1'},
  ];
  constructor() { }

  ngOnInit() {
  }

}
