import math


class SimilarityCalculator:
    """Provides different similarity metrics."""

    @staticmethod
    def cosine_similarity(vec1, vec2):
        """Calculate cosine similarity between two vectors."""

        if len(vec1) != len(vec2) or len(vec1) == 0:
            return 0.0

        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        magnitude1 = math.sqrt(sum(a * a for a in vec1))
        magnitude2 = math.sqrt(sum(b * b for b in vec2))

        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0

        return dot_product / (magnitude1 * magnitude2)

    @staticmethod
    def jaccard_similarity(set1, set2):
        """Calculate Jaccard similarity between two sets."""

        if not set1 and not set2:
            return 1.0

        union = set1 | set2

        if len(union) == 0:
            return 0.0

        intersection = set1 & set2

        return len(intersection) / len(union)

    @staticmethod
    def pearson_correlation(ratings1, ratings2):
        """Calculate Pearson correlation coefficient."""

        if len(ratings1) != len(ratings2) or len(ratings1) == 0:
            return 0.0

        mean1 = sum(ratings1) / len(ratings1)
        mean2 = sum(ratings2) / len(ratings2)

        numerator = sum(
            (a - mean1) * (b - mean2)
            for a, b in zip(ratings1, ratings2)
        )

        denominator1 = math.sqrt(
            sum((a - mean1) ** 2 for a in ratings1)
        )

        denominator2 = math.sqrt(
            sum((b - mean2) ** 2 for b in ratings2)
        )

        denominator = denominator1 * denominator2

        if denominator == 0:
            return 0.0

        return numerator / denominator


if __name__ == "__main__":
    calc = SimilarityCalculator()

    print("Cosine Similarity:")
    print(calc.cosine_similarity([1, 2, 3], [1, 2, 3]))

    print("\nJaccard Similarity:")
    print(calc.jaccard_similarity({"python", "ml"}, {"python", "ai"}))

    print("\nPearson Correlation:")
    print(calc.pearson_correlation([5, 4, 3], [5, 4, 3]))