import pytest

from framework.ai.semantic_evaluator import SemanticEvaluator


@pytest.mark.ai
def test_semantic_keyword_coverage():

    response = (
        "Software testing validates application behavior "
        "and helps identify defects before release."
    )

    expected_keywords = [
        "testing",
        "validates",
        "defects"
    ]

    score = SemanticEvaluator.keyword_coverage(
        response,
        expected_keywords
    )

    assert score >= 0.66
@pytest.mark.ai
def test_low_semantic_keyword_coverage():

    response = "Programming involves writing code."

    expected_keywords = [
        "testing",
        "validation",
        "defects"
    ]

    score = SemanticEvaluator.keyword_coverage(
        response,
        expected_keywords
    )

    assert score < 0.5    