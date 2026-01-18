import { useEffect, useState } from "react";
import axios from "axios";
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
  const [reviewData, setReviewData] = useState<GetReviewsResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchReviews = async () => {
      try {
        setIsLoading(true);
        setError("");

        const { data } = await axios.get<GetReviewsResponse>(
          `/api/products/${productId}/reviews`
        );

        setReviewData(data);
      } catch (err) {
        console.error(err);
        setError("Could not fetch the reviews. Try again.");
      } finally {
        setIsLoading(false);
      }
    };

    fetchReviews();
  }, [productId]);

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
    return <p className="text-red-500">{error}</p>;
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
