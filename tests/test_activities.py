def test_get_activities_returns_activity_dictionary(client):
    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()

    assert isinstance(payload, dict)
    assert "Chess Club" in payload

    chess_club = payload["Chess Club"]
    assert set(chess_club.keys()) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
    assert isinstance(chess_club["participants"], list)
