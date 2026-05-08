import { db } from '../db.js';

export class BookService {
  static async getAllBooks() {
    return await db.book.findMany({
      include: { author: true }
    });
  }

  static async getBooksByAuthor(authorName: string) {
    return await db.book.findMany({
      where: {
        author: { // You must target the relation object first
          name: {
            contains: authorName,
            mode: 'insensitive'
          }
        }
      },
      include: { author: true }
    });
  }
}