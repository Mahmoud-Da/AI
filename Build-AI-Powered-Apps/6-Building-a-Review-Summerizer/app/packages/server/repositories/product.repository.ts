import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export const productRepository = {
  async getProduct(productId: number) {
    return prisma.product.findUnique({
      where: {
        id: productId,
      },
    });
  },
};
