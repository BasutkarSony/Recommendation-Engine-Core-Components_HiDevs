import math


class RecommendationEvaluator:
    """Evaluates recommendation quality."""

    @staticmethod
    def precision_at_k(recommendations, relevant_items, k):
        if not recommendations or not relevant_items:
            return 0.0

        recommended = recommendations[:k]
        relevant = set(relevant_items)

        hits = len(set(recommended) & relevant)

        return hits / len(recommended)

    @staticmethod
    def recall_at_k(recommendations, relevant_items, k):
        if not relevant_items:
            return 0.0

        recommended = recommendations[:k]
        relevant = set(relevant_items)

        hits = len(set(recommended) & relevant)

        return hits / len(relevant)

    @staticmethod
    def ndcg_at_k(recommendations, relevant_items, k):
        if not recommendations or not relevant_items:
            return 0.0

        dcg = 0.0

        for i, item in enumerate(recommendations[:k]):
            if item in relevant_items:
                dcg += 1 / math.log2(i + 2)

        ideal_hits = min(len(relevant_items), k)

        idcg = sum(
            1 / math.log2(i + 2)
            for i in range(ideal_hits)
        )

        if idcg == 0:
            return 0.0

        return dcg / idcg

    def evaluate_all(self, recommendations_dict, ground_truth_dict, k=5):

        precisions = []
        recalls = []
        ndcgs = []

        for user_id, recs in recommendations_dict.items():

            truth = ground_truth_dict.get(user_id)

            if truth is None:
                continue

            precisions.append(
                self.precision_at_k(recs, truth, k)
            )

            recalls.append(
                self.recall_at_k(recs, truth, k)
            )

            ndcgs.append(
                self.ndcg_at_k(recs, truth, k)
            )

        if not precisions:
            return {
                "precision": 0.0,
                "recall": 0.0,
                "ndcg": 0.0
            }

        return {
            "precision": round(sum(precisions) / len(precisions), 3),
            "recall": round(sum(recalls) / len(recalls), 3),
            "ndcg": round(sum(ndcgs) / len(ndcgs), 3)
        }


if __name__ == "__main__":

    evaluator = RecommendationEvaluator()

    recommendations = {
        1: ["A", "B", "C"],
        2: ["D", "E", "F"]
    }

    ground_truth = {
        1: ["A", "C"],
        2: ["D", "G"]
    }

    results = evaluator.evaluate_all(
        recommendations,
        ground_truth,
        k=3
    )

    print(results)