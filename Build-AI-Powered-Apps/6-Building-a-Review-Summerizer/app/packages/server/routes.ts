import type { Request, Response } from "express";
import express from "express";
import { chatController } from "./controllers/chat.controller";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

const router = express.Router();

router.get("/", (req: Request, res: Response) => {
  res.send("Hello World");
});

router.get("/api/hello", (req: Request, res: Response) => {
  res.json({ message: "Hello World!" });
});

router.post("/api/chat", chatController.sendMessage);

router.get("/api/products/:id/reviews", async (req: Request, res: Response) => {
  try {
    const productId = Number(req.params.id);

    if (Number.isNaN(productId)) {
      return res.status(400).json({
        error: "Invalid product id",
      });
    }

    const reviews = await prisma.review.findMany({
      where: {
        productId: productId,
      },
      orderBy: {
        createdAt: "desc",
      },
    });

    return res.json(reviews);
  } catch (error) {
    console.log(error);
  }
});

export default router;
