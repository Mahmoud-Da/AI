import OpenAI from "openai";

import dotenv from "dotenv";
dotenv.config();

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const stream = await client.responses.create({
  model: "gpt-4.1",
  input: "Write a story about a robot",
  temperature: 0.7,
  max_output_tokens: 250,
  stream: true,
});

for await (const event of stream) {
  if (event.delta) {
    process.stdout.write(event.delta);
  }
}
