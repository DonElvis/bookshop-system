import React, { useEffect, useState } from 'react';
import { getBooks } from './api/bookService';
import { AddBookForm } from './components/AddBookForm';

function App() {
  const [books, setBooks] = useState([]);

  const loadBooks = async () => {
    const res = await getBooks();
    setBooks(res.data);
  };

  useEffect(() => { loadBooks(); }, []);

  return (
    <div className="p-10 bg-gray-100 min-h-screen">
      <h1 className="text-2xl font-bold mb-6">Bookshop Inventory</h1>
      
      <AddBookForm onBookAdded={loadBooks} />

      <div className="grid gap-4">
        {books.map(book => (
          <div key={book.id} className="p-4 bg-white rounded shadow flex justify-between">
            <div>
              <p className="font-bold">{book.title}</p>
              <p className="text-sm text-gray-600">{book.author}</p>
            </div>
            <div className="text-right">
              <p className="font-mono">${book.price}</p>
              <p className="text-xs text-blue-500">{book.stock} in stock</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;