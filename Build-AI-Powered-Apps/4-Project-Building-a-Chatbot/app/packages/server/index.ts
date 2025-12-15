import express from "express";
import type { Request, Response } from "express";
import OpenAI from "openai";
import dotenv from "dotenv";

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

app.post("/api/chat", async (req: Request, res: Response) => {
  const { prompt } = req.body;

  const response = await client.responses.create({
    model: "gpt-40-mini",
    input: prompt,
    temperature: 0.2,
    max_output_tokens: 100,
  });

  res.json({
    message: response.output_text,
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
