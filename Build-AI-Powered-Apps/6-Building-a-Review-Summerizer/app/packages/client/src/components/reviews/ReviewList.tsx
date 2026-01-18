import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import { useEffect } from "react";
import Skeleton from "react-loading-skeleton";
import "react-loading-skeleton/dist/skeleton.css";
import StarRating from "./StarRating";

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

type ReviewListProps = {
  productId: number;
};

const ReviewList = ({ productId }: ReviewListProps) => {
  const {
    data: reviewData,
    isLoading,
    error,
  } = useQuery<GetReviewsResponse>({
    queryKey: ["reviews", productId],
    queryFn: () => fetchReviews(),
  });

  const fetchReviews = async () => {
    const { data } = await axios.get<GetReviewsResponse>(
      `/api/products/${productId}/reviews`
    );

    return data;
  };

  if (isLoading) {
    return (
      <div className="flex flex-col gap-5">
        {[1, 2, 3].map((i) => (
          <div key={i} className="flex flex-col gap-2">
            <Skeleton width={150} />
            <Skeleton width={100} />
            <Skeleton count={2} />
          </div>
        ))}
      </div>
    );
  }

  if (error) {
    return <p className="text-red-500">Could not fetch reviews. Try again.</p>;
  }

  if (!reviewData) return null;

  return (
    <div className="flex flex-col gap-6">
      {reviewData.summary && (
        <div className="bg-gray-100 p-4 rounded-md">
          <h2 className="font-semibold mb-2">Review Summary</h2>
          <p>{reviewData.summary}</p>
        </div>
      )}

      {reviewData.reviews.map((review) => (
        <div key={review.id} className="border p-4 rounded-md">
          <div className="font-semibold">{review.author}</div>
          <StarRating value={review.rating} />
          <p className="py-2">{review.content}</p>
        </div>
      ))}
    </div>
  );
};

export default ReviewList;
