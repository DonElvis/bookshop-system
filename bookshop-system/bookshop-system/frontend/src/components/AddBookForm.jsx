import React, { useState } from 'react';
import { createBook } from '../api/bookService';

export function AddBookForm({ onBookAdded }) {
  const [formData, setFormData] = useState({ title: '', author: '', price: 0, stock: 0 });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await createBook({
        ...formData,
        price: Number(formData.price),
        stock: Number(formData.stock)
      });
      onBookAdded(); // Refresh the list in App.jsx
      alert("Book Added!");
    } catch (err) {
      alert("Error: " + (err.response?.data?.message || "Check console"));
    }
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 bg-white rounded shadow mb-6 flex gap-4 items-end">
      <div>
        <label className="block text-sm">Title</label>
        <input className="border p-1 rounded" onChange={e => setFormData({...formData, title: e.target.value})} />
      </div>
      <div>
        <label className="block text-sm">Author</label>
        <input className="border p-1 rounded" onChange={e => setFormData({...formData, author: e.target.value})} />
      </div>
      <div>
        <label className="block text-sm">Price</label>
        <input type="number" className="border p-1 rounded w-20" onChange={e => setFormData({...formData, price: e.target.value})} />
      </div>
      <button type="submit" className="bg-green-600 text-white px-4 py-1 rounded">Add</button>
    </form>
  );
}