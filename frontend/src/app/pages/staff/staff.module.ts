import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatTableModule } from '@angular/material/table';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { StaffRoutingModule } from './staff-routing.module';
import { StaffComponent } from './staff.component';

@NgModule({
  declarations: [StaffComponent],
  imports: [CommonModule, StaffRoutingModule, MatTableModule, MatButtonModule, MatIconModule]
})
export class StaffModule { }
