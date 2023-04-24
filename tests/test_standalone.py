from rottentomatoes import standalone


def test_tomatometer(top_gun_mav_content):
    assert standalone.tomatometer("top gun maverick", content=top_gun_mav_content) == 96


def test_movie_url():
    """The old version, before using search."""
    assert standalone._movie_url("top gun") == "https://www.rottentomatoes.com/m/top_gun"


def test_movie_title(top_gun_mav_content):
    assert standalone.movie_title("top gun", top_gun_mav_content) == "Top Gun: Maverick"


def test_audience_score(happy_gilmore_content):
    assert standalone.audience_score("happy gilmore", happy_gilmore_content) == 85


def test_genres(happy_gilmore_content):
    assert standalone.genres("happy gilmore", happy_gilmore_content) == ["Comedy"]


def test_weighted_score(top_gun_mav_content):
    assert standalone.weighted_score("top gun maverick", top_gun_mav_content) == 97


def test_rating(top_gun_mav_content):
    assert standalone.rating("top gun maverick", top_gun_mav_content) == "PG-13"


def test_duration(top_gun_mav_content):
    assert standalone.duration("top gun", top_gun_mav_content) == "2h 11m"


def test_year_released(forrest_gump_content):
    assert standalone.year_released("forrest gump", forrest_gump_content) == "1994"


def test_actors(forrest_gump_content):
    res = standalone.actors("forrest gump", forrest_gump_content)
    
    for actor in [
        'Tom Hanks', 'Robin Wright', 'Gary Sinise', 'Mykelti Williamson', 'Sally Field'
    ]:
        assert actor in res


def test_directors(happy_gilmore_content):
    res = standalone.directors("happy gilmore", content=happy_gilmore_content)
    assert "Dennis Dugan" in res
