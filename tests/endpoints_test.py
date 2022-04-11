def test_random_quote_endpoint(app):
    result = app.simulate_get("/api")
    expected_keys = {"quote", "timestamp", "season", "episode"}
    assert expected_keys <= result.json.keys()
