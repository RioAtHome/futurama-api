def test_random_quote_endpoint(app):
    result = app.simulate_get("/api")
    print(result.json.keys())
    expected_keys = {"line", "timestamp", "season", "episode"}
    
    assert expected_keys <= result.json.keys()
