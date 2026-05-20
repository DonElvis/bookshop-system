import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatTableModule } from '@angular/material/table';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { InventoryRoutingModule } from './inventory-routing.module';
import { InventoryComponent } from './inventory.component';

@NgModule({
  declarations: [InventoryComponent],
  imports: [CommonModule, InventoryRoutingModule, MatTableModule, MatButtonModule, MatIconModule]
})
export class InventoryModule { }
