import type { Review } from "@prisma/client";
import { llmClient } from "../llm/client";
import { reviewRepository } from "../repositories/review.repository";
import template from "../prompts/summarize-reviews.txt";

export const reviewService = {
  getReviews(productId: number): Promise<Review[]> {
    return reviewRepository.getReviews(productId);
  },

  async summarizeReviews(productId: number): Promise<string> {
    const reviews = await reviewRepository.getReviews(productId, 10);

    const joinedReviews = reviews.map((r) => r.content).join("\n\n");
    const prompt = template.replace("{{reviews}}", joinedReviews);

    console.log(joinedReviews);
    const response = await llmClient.generateText({
      model: "gpt-5-mini",
      prompt,
      maxTokens: 1000,
    });

    console.log(response);
    return response.text;
  },
};
