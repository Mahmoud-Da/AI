import { useMutation, useQuery } from "@tanstack/react-query";
import axios from "axios";
import { HiSparkles } from "react-icons/hi";
import "react-loading-skeleton/dist/skeleton.css";
import { Button } from "../ui/button";
import ReviewSkeleton from "./ReviewSkeleton";
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

type SummarizeResponse = {
  summary: string;
};

const ReviewList = ({ productId }: ReviewListProps) => {
  const summaryMutation = useMutation<SummarizeResponse>({
    mutationFn: () => summarizeReviews(),
  });

  const reviewsQuery = useQuery<GetReviewsResponse>({
    queryKey: ["reviews", productId],
    queryFn: () => fetchReviews(),
  });

  const summarizeReviews = async () => {
    const { data } = await axios.post<SummarizeResponse>(
      `/api/products/${productId}/reviews/summarize`
    );
    return data;
  };

  const fetchReviews = async () => {
    const { data } = await axios.get<GetReviewsResponse>(
      `/api/products/${productId}/reviews`
    );

    return data;
  };

  if (reviewsQuery.isLoading) {
    return (
      <div className="flex flex-col gap-5">
        {[1, 2, 3].map((i) => (
          <ReviewSkeleton key={i} />
        ))}
      </div>
    );
  }

  if (reviewsQuery.isError) {
    return <p className="text-red-500">Could not fetch reviews. Try again.</p>;
  }

  if (!reviewsQuery.data?.reviews.length) return null;

  const currentSummary =
    reviewsQuery.data?.summary || summaryMutation.data?.summary;

  return (
    <div>
      <div className="mb-5">
        {currentSummary ? (
          <p>{currentSummary}</p>
        ) : (
          <div>
            <Button
              onClick={() => summaryMutation.mutate()}
              className="cursor-pointer"
              disabled={summaryMutation.isPending}
            >
              <HiSparkles />
              Summarize
            </Button>
            {summaryMutation.isPending && (
              <div className="py-3">
                <ReviewSkeleton />
              </div>
            )}
            {summaryMutation.isError && (
              <p className="text-red-500">
                Could not summarize the reviews. Try again!
              </p>
            )}
          </div>
        )}
      </div>
      <div className="flex flex-col gap-6">
        {reviewsQuery.data?.summary && (
          <div className="bg-gray-100 p-4 rounded-md">
            <h2 className="font-semibold mb-2">Review Summary</h2>
            <p>{reviewsQuery.data?.summary}</p>
          </div>
        )}
        {reviewsQuery.data?.reviews.map((review) => (
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
