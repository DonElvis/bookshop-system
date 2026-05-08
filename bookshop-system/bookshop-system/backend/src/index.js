const express = require("express");
const { PrismaClient } = require("@prisma/client");
const cors = require("cors");
const { z } = require("zod");

const app = express();
const prisma = new PrismaClient(); // This is all you need!

app.use(cors());
app.use(express.json());

// Validation Schema
const bookSchema = z.object({
  title: z.string().min(1),
  author: z.string().min(2),
  price: z.number().positive(),
  stock: z.number().int().nonnegative(),
});

// Create book with Validation
app.post("/books", async (req, res) => {
  try {
    // 1. Validate the request body against the schema
    const validatedData = bookSchema.parse(req.body);

    // 2. If validation passes, create the book
    const book = await prisma.book.create({
      data: validatedData,
    });

    res.status(201).json(book);
  } catch (error) {
    // 3. Handle Zod validation errors specifically
    if (error instanceof z.ZodError) {
      return res.status(400).json({
        message: "Validation failed",
        errors: error.errors, // Provides details on which field failed
      });
    }
    
    // Handle other database/server errors
    res.status(500).json({ error: "Internal Server Error" });
  }
});

// Get all books
app.get("/books", async (req, res) => {
  try {
    const books = await prisma.book.findMany({
        orderBy: { createdAt: 'desc' } // Good practice for scalable lists
    });
    res.json(books);
  } catch (error) {
    res.status(500).json({ error: "Could not fetch books" });
  }
});

app.listen(3000, () => console.log("🚀 Server ready at http://localhost:3000"));