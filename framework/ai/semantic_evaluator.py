class SemanticEvaluator:

    @staticmethod
    def keyword_coverage(response_text, expected_keywords):

        response_lower = response_text.lower()

        matched = [
            keyword
            for keyword in expected_keywords
            if keyword.lower() in response_lower
        ]

        score = len(matched) / len(expected_keywords)

        return score