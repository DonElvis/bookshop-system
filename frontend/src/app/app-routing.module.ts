import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { LoginComponent } from './pages/login/login.component';

const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'pos', loadChildren: () => import('./pages/pos/pos.module').then(m => m.PosModule) },
  { path: 'inventory', loadChildren: () => import('./pages/inventory/inventory.module').then(m => m.InventoryModule) },
  { path: 'products', loadChildren: () => import('./pages/products/products.module').then(m => m.ProductsModule) },
  { path: 'customers', loadChildren: () => import('./pages/customers/customers.module').then(m => m.CustomersModule) },
  { path: 'staff', loadChildren: () => import('./pages/staff/staff.module').then(m => m.StaffModule) },
  { path: 'reports', loadChildren: () => import('./pages/reports/reports.module').then(m => m.ReportsModule) },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
