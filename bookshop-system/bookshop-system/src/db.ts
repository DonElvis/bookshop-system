import { PrismaClient } from '@prisma/client';
import { Client } from 'pg';
import { PrismaPg } from '@prisma/adapter-pg';
import "dotenv/config";

// Ensure the URL exists
const connectionString = process.env.DATABASE_URL;
if (!connectionString) {
  throw new Error("DATABASE_URL is not defined in .env");
}

// 1. Setup Postgres Driver
const client = new Client({ connectionString });

// 2. Initialize Adapter
const adapter = new PrismaPg(client);

// 3. Instantiate Prisma (Singleton for scalability)
const globalForPrisma = global as unknown as { prisma: PrismaClient };

export const db = globalForPrisma.prisma || new PrismaClient({ adapter });

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = db;