import axios from 'axios';

const API_URL = 'http://localhost:3000';

export const getBooks = () => axios.get(`${API_URL}/books`);
export const createBook = (bookData) => axios.post(`${API_URL}/books`, bookData);