import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatTableModule } from '@angular/material/table';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { CustomersRoutingModule } from './customers-routing.module';
import { CustomersComponent } from './customers.component';

@NgModule({
  declarations: [CustomersComponent],
  imports: [CommonModule, CustomersRoutingModule, MatTableModule, MatButtonModule, MatIconModule]
})
export class CustomersModule { }
