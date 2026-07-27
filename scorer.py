class RecommendationScorer:
    """Scores and ranks recommendation candidates."""

    def __init__(self):
        self.scorers = []

    def add_scorer(self, name, function, weight):
        """Register a scoring function with a weight."""
        self.scorers.append({
            "name": name,
            "function": function,
            "weight": weight
        })

    def calculate_score(self, user_id, item_id, context=None):
        """Calculate weighted score for an item."""

        if context is None:
            context = {}

        total_weight = sum(s["weight"] for s in self.scorers)

        if total_weight == 0:
            return {
                "score": 0.0,
                "explanation": "No scoring functions registered."
            }

        final_score = 0.0
        explanation = []

        for scorer in self.scorers:
            score = scorer["function"](user_id, item_id, context)

            # Keep score in range [0,1]
            score = max(0.0, min(score, 1.0))

            final_score += score * scorer["weight"]
            explanation.append(f"{scorer['name']}={score:.2f}")

        final_score /= total_weight

        return {
            "score": round(final_score, 3),
            "explanation": ", ".join(explanation)
        }

    def rank_candidates(self, user_id, candidates, limit=10, context=None):
        """Rank candidates based on score."""

        ranked = []

        for item in candidates:
            result = self.calculate_score(user_id, item, context)

            ranked.append({
                "item": item,
                "score": result["score"],
                "explanation": result["explanation"]
            })

        ranked.sort(key=lambda x: x["score"], reverse=True)

        return ranked[:limit]


# -----------------------------
# Example scoring functions
# -----------------------------

def relevance(user_id, item_id, context):
    return context.get("relevance", {}).get(item_id, 0.5)


def popularity(user_id, item_id, context):
    return context.get("popularity", {}).get(item_id, 0.5)


def recency(user_id, item_id, context):
    return context.get("recency", {}).get(item_id, 0.5)


if __name__ == "__main__":

    scorer = RecommendationScorer()

    scorer.add_scorer("Relevance", relevance, 0.5)
    scorer.add_scorer("Popularity", popularity, 0.3)
    scorer.add_scorer("Recency", recency, 0.2)

    context = {
        "relevance": {
            "A": 0.9,
            "B": 0.7,
            "C": 0.4
        },
        "popularity": {
            "A": 0.6,
            "B": 0.9,
            "C": 0.8
        },
        "recency": {
            "A": 0.8,
            "B": 0.4,
            "C": 0.9
        }
    }

    recommendations = scorer.rank_candidates(
        user_id=1,
        candidates=["A", "B", "C"]
    , context=context)

    for item in recommendations:
        print(item)