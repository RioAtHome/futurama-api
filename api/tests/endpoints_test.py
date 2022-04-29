def test_random_quote_endpoint(app):
    result = app.simulate_get("/api")
    expected_keys = {"line", "timestamp", "season", "episode"}
    assert expected_keys <= result.json.keys()
    assert result.status_code == 200


def test_get_character(app, random_character):
    result = app.simulate_get(f"/api/{random_character}")

    assert result.json["character"] == random_character

    expected_keys = {"line", "timestamp", "season", "episode"}

    assert expected_keys <= result.json.keys()
    assert result.status_code == 200


def test_get_character_gives_error(app):
    someone = "someonenotinthedatabase"
    result = app.simulate_get(f"/api/{someone}")
    assert result.json["title"] == f"Hmm, looks like {someone} isnt in the show.."
    assert result.status_code == 404


# def test_get_quote_from_season(app):
#     result = app.simulate_get(f"/api/12")

#     assert result.json["season"] == "12"
#     assert result.status_code == 200
