import type { Review } from "@prisma/client";
import { reviewRepository } from "../repositories/review.repository";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

export const reviewService = {
  getReviews(productId: number): Promise<Review[]> {
    return reviewRepository.getReviews(productId);
  },

  async summarizeReviews(productId: number): Promise<string> {
    const reviews = await reviewRepository.getReviews(productId, 10);

    const joinedReviews = reviews.map((r) => r.content).join("\n\n");
    const prompt = `
      Summarize the following customer reviews into a short paragraph,
      highlighting key themes, both positive and negative:

      ${joinedReviews}
          `;
    console.log(joinedReviews);
    const response = await client.responses.create({
      model: "gpt-5-mini",
      input: prompt,
      max_output_tokens: 1000,
    });

    console.log(response);
    return response.output_text;
  },
};
