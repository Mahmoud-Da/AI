import { PrismaClient, type Review } from "@prisma/client";
import dayjs from "dayjs";

const prisma = new PrismaClient();

export const reviewRepository = {
  getReviews(productId: number, limit?: number): Promise<Review[]> {
    return prisma.review.findMany({
      where: { productId },
      orderBy: { createdAt: "desc" },
      take: limit,
    });
  },

  async storeReviewSummary(productId: number, summary: string) {
    const now = new Date();

    const expiresAt = dayjs().add(7, "day").toDate();

    const data = {
      content: summary,
      generatedAt: now,
      expiresAt,
      productId,
    };

    return prisma.summary.upsert({
      where: {
        productId,
      },
      create: data,
      update: data,
    });
  },

  async getReviewSummary(productId: number): Promise<string | null> {
    const summary = await prisma.summary.findFirst({
      where: {
        AND: [
          { productId },
          {
            expiresAt: {
              gt: new Date(),
            },
          },
        ],
      },
    });

    return summary ? summary.content : null;
  },
};
