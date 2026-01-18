import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import { useState } from "react";
import { HiSparkles } from "react-icons/hi";
import Skeleton from "react-loading-skeleton";
import "react-loading-skeleton/dist/skeleton.css";
import { Button } from "../ui/button";
import StarRating from "./StarRating";
import ReviewSkeleton from "./ReviewSkeleton";

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

type SummarizeResponse = {
  summary: string;
};

const ReviewList = ({ productId }: ReviewListProps) => {
  const [summary, setSummary] = useState("");
  const [isSummaryLoading, setIsSummaryLoading] = useState(false);
  const [summaryError, setSummaryError] = useState("");

  const {
    data: reviewData,
    isLoading,
    error,
  } = useQuery<GetReviewsResponse>({
    queryKey: ["reviews", productId],
    queryFn: () => fetchReviews(),
  });

  const handleSummaries = async () => {
    try {
      setIsSummaryLoading(true);
      setSummaryError("");

      const { data } = await axios.post<SummarizeResponse>(
        `/api/products/${productId}/reviews/summarize`
      );
      setSummary(data.summary);
    } catch (error) {
      console.log(error);
      setSummaryError("Could not summarize the reviews. Try again.");
    } finally {
      setIsSummaryLoading(false);
    }
  };

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
          <ReviewSkeleton key={i} />
        ))}
      </div>
    );
  }

  if (error) {
    return <p className="text-red-500">Could not fetch reviews. Try again.</p>;
  }

  if (!reviewData?.reviews.length) return null;

  const currentSummary = reviewData.summary || summary;

  return (
    <div>
      <div className="mb-5">
        {currentSummary ? (
          <p>{currentSummary}</p>
        ) : (
          <div>
            <Button
              onClick={handleSummaries}
              className="cursor-pointer"
              disabled={isSummaryLoading}
            >
              <HiSparkles />
              Summarize
            </Button>
            {isSummaryLoading && (
              <div className="py-3">
                <ReviewSkeleton />
              </div>
            )}
            {summaryError && <p className="text-red-500">{summaryError}</p>}
          </div>
        )}
      </div>
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
    </div>
  );
};

export default ReviewList;
