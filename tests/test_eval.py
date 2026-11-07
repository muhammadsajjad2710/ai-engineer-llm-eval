from src.eval import run_suite
def test_suite():
    out = run_suite([
        {"answer": "Paris is in France", "must_include": ["Paris"]},
        {"answer": "unknown", "must_include": ["Paris"]},
    ])
    assert out["passed"] == 1
