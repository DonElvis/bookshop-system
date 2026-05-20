export interface Product {
  id: string;
  name: string;
  description?: string;
  category_id: string;
  price: number;
  cost: number;
  image_url?: string;
  is_active: number;
  created_at: string;
  updated_at: string;
}

export interface Category {
  id: string;
  name: string;
  description?: string;
}
