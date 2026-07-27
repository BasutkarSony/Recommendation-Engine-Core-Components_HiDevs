from similarity import SimilarityCalculator
from candidate_gen import CandidateGenerator
from scorer import (
    RecommendationScorer,
    relevance,
    popularity,
    recency,
)
from evaluator import RecommendationEvaluator


def run_tests():
    print("Running Recommendation Engine Tests...\n")

    # Similarity
    sim = SimilarityCalculator()
    assert round(sim.cosine_similarity([1, 2], [1, 2]), 2) == 1.00
    assert round(sim.jaccard_similarity({"A"}, {"A", "B"}), 2) == 0.50
    print("Similarity tests passed.")

    # Candidate Generator
    gen = CandidateGenerator()
    assert len(gen.popularity_candidates()) > 0
    assert isinstance(gen.hybrid_candidates(1), list)
    print("Candidate Generator tests passed.")

    # Scorer
    scorer = RecommendationScorer()
    scorer.add_scorer("Relevance", relevance, 0.5)
    scorer.add_scorer("Popularity", popularity, 0.3)
    scorer.add_scorer("Recency", recency, 0.2)

    context = {
        "relevance": {"A": 0.9},
        "popularity": {"A": 0.8},
        "recency": {"A": 0.7},
    }

    result = scorer.calculate_score(1, "A", context)
    assert result["score"] > 0
    print("Scorer tests passed.")

    # Evaluator
    evaluator = RecommendationEvaluator()
    metrics = evaluator.evaluate_all(
        {1: ["A", "B"]},
        {1: ["A"]},
        k=2,
    )

    assert "precision" in metrics
    assert "recall" in metrics
    assert "ndcg" in metrics
    print("Evaluator tests passed.")

    print("\nAll tests passed successfully!")


if __name__ == "__main__":
    run_tests()