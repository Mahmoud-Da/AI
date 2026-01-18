import { useEffect, useState } from "react";
import axios from "axios";

type ReviewListProps = {
  productId: number;
};

type Review = {
  id: number;
  author: string;
  content: string;
  rating: number;
  createdAt: string;
};

type GetReviewsResponse = {
  summary: string | null;
  reviews: Review[];
};

const ReviewList = ({ productId }: ReviewListProps) => {
  const [reviewData, setReviewData] = useState<GetReviewsResponse | null>(null);

  const fetchReviews = async () => {
    const { data } = await axios.get<GetReviewsResponse>(
      `/api/products/${productId}/reviews`
    );
    setReviewData(data);
  };

  useEffect(() => {
    fetchReviews();
  }, [productId]);

  if (!reviewData) {
    return <div>Loading reviews...</div>;
  }

  return (
    <div className="flex flex-col gap-5">
      {reviewData.reviews.map((review) => (
        <div key={review.id} className="border rounded p-4">
          <div className="font-semibold">{review.author}</div>
          <div className="text-sm text-gray-600">
            Rating: {review.rating} / 5
          </div>
          <p className="py-2">{review.content}</p>
        </div>
      ))}
    </div>
  );
};

export default ReviewList;
