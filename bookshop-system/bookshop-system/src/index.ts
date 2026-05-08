import express, { Request, Response } from 'express';
import cors from 'cors';
import { db } from './db.js';
import "dotenv/config";

const app = express();
app.use(cors());
app.use(express.json());

// Type-safe interface for the Request Body
interface CreateBookBody {
  title: string;
  isbn: string;
  price: number;
  stock?: number;
  authorName: string;
}

app.post('/books', async (req: Request<{}, {}, CreateBookBody>, res: Response) => {
  try {
    const { title, isbn, price, stock, authorName } = req.body;

    const newBook = await db.book.create({
      data: {
        title,
        isbn,
        price,
        stock: stock || 0,
        author: {
          connectOrCreate: {
            where: { name: authorName },
            create: { name: authorName }
          }
        }
      },
      include: { author: true }
    });

    res.status(201).json(newBook);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Check console for error details' });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`📚 Server running on http://localhost:${PORT}`);
});