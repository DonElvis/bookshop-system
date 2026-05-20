import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  statistics = {
    totalSales: 15000,
    totalOrders: 150,
    totalCustomers: 45,
    lowStockItems: 8
  };

  constructor() { }

  ngOnInit(): void {
  }
}
