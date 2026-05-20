import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatTableModule } from '@angular/material/table';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { PosRoutingModule } from './pos-routing.module';
import { PosComponent } from './pos.component';

@NgModule({
  declarations: [PosComponent],
  imports: [CommonModule, PosRoutingModule, MatTableModule, MatButtonModule, MatIconModule]
})
export class PosModule { }
