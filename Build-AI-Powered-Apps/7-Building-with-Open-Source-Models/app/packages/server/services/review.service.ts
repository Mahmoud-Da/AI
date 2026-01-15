import type { Review } from "@prisma/client";
import { llmClient } from "../llm/client";
import { reviewRepository } from "../repositories/review.repository";

export const reviewService = {
  getReviews(productId: number): Promise<Review[]> {
    return reviewRepository.getReviews(productId);
  },

  async summarizeReviews(productId: number): Promise<string> {
    const existingSummary = await reviewRepository.getReviewSummary(productId);

    if (existingSummary) {
      return existingSummary;
    }

    const reviews = await reviewRepository.getReviews(productId, 10);

    const joinedReviews = reviews.map((r) => r.content).join("\n\n");

    console.log(joinedReviews);

    const summary = await llmClient.summarizeReviews(joinedReviews);

    await reviewRepository.storeReviewSummary(productId, summary);

    return summary;
  },
};
