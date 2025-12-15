import express from "express";
import type { Request, Response } from "express";
import OpenAI from "openai";
import dotenv from "dotenv";
import { z } from "zod";

dotenv.config();

const app = express();
// Enable JSON parsing
app.use(express.json());

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const port = process.env.PORT || 3000;

app.get("/", (req: Request, res: Response) => {
  res.send("Hello World");
});

app.get("/api/hello", (req: Request, res: Response) => {
  res.json({ message: "Hello World!" });
});

// method 1
// only last massage
// let lastResponseId: string | null = null;

// method 2
// all conversation
const conversations = new Map<string, string>();
const chatSchema = z.object({
  prompt: z
    .string()
    .trim()
    .min(1, "prompt is required")
    .max(1000, "prompt is too long, maximum 1000 characters"),
  conversationId: z.uuid("invalid UUID"),
});

app.post("/api/chat", async (req: Request, res: Response) => {
  const { prompt, conversationId } = req.body;

  const parsedResult = chatSchema.safeParse(req.body);

  if (!parsedResult.success) {
    return res.status(400).json(parsedResult.error.format());
  }

  const response = await client.responses.create({
    model: "gpt-5-mini",
    input: prompt,
    // NOTE: this is not support with GPT 5
    // temperature: 0.2,
    max_output_tokens: 100,
    previous_response_id: conversations.get(conversationId),
  });

  // update in Memory
  // method 1
  // PS: gpt5
  // lastResponseId = response.id;

  conversations.set(conversationId, response.id);
  res.json({
    message: response.output_text,
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
