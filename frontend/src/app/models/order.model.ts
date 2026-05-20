export interface Order {
  id: string;
  customer_id?: string;
  total_amount: number;
  discount_amount: number;
  payment_method: string;
  status: string;
  notes?: string;
  items: OrderItem[];
  created_at: string;
  updated_at: string;
}

export interface OrderItem {
  id: string;
  order_id: string;
  product_id: string;
  quantity: number;
  unit_price: number;
}

export interface OrderCreateRequest {
  customer_id?: string;
  items: OrderCreateItem[];
  discount_amount: number;
  payment_method: string;
  notes?: string;
}

export interface OrderCreateItem {
  product_id: string;
  quantity: number;
}
