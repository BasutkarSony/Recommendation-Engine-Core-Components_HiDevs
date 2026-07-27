class CandidateGenerator:
    """Generates recommendation candidates using different strategies."""

    def __init__(self):
        # User -> Items they interacted with
        self.user_history = {
            1: {"A", "B", "C"},
            2: {"B", "C", "D"},
            3: {"C", "D", "E"},
            4: set(),  # Cold-start user
        }

        # Item -> Similar Items
        self.similar_items = {
            "A": ["B", "C"],
            "B": ["A", "D"],
            "C": ["A", "E"],
            "D": ["B", "E"],
            "E": ["C", "D"],
        }

        # Item popularity
        self.popularity = [
            "C",
            "B",
            "D",
            "A",
            "E",
            "F",
            "G",
        ]

    def collaborative_candidates(self, user_id, limit=20):
        """Recommend items liked by similar users."""

        history = self.user_history.get(user_id, set())

        if not history:
            return self.popularity_candidates(limit)

        candidates = set()

        for other_user, items in self.user_history.items():
            if other_user == user_id:
                continue

            if history & items:
                candidates.update(items - history)

        return list(candidates)[:limit]

    def content_based_candidates(self, user_id, limit=20):
        """Recommend items similar to user's history."""

        history = self.user_history.get(user_id, set())

        if not history:
            return self.popularity_candidates(limit)

        candidates = set()

        for item in history:
            candidates.update(self.similar_items.get(item, []))

        candidates -= history

        return list(candidates)[:limit]

    def popularity_candidates(self, limit=20):
        """Return globally popular items."""

        return self.popularity[:limit]

    def hybrid_candidates(self, user_id, limit=20):
        """Combine collaborative, content-based and popularity."""

        combined = []

        combined.extend(self.collaborative_candidates(user_id, limit))
        combined.extend(self.content_based_candidates(user_id, limit))
        combined.extend(self.popularity_candidates(limit))

        # Remove duplicates while preserving order
        unique = list(dict.fromkeys(combined))

        return unique[:limit]


if __name__ == "__main__":
    generator = CandidateGenerator()

    print("Collaborative:", generator.collaborative_candidates(1))
    print("Content-Based:", generator.content_based_candidates(1))
    print("Popularity:", generator.popularity_candidates())
    print("Hybrid:", generator.hybrid_candidates(1))
    print("Cold Start:", generator.hybrid_candidates(4))