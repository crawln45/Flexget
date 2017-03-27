import pytest

class TestTrendingSerieList(object):
    config = """
        tasks:
          test_trending_list:
            trending_list:
              kind: series
            exec: echo "Found {{title}}"
             """

    @pytest.mark.online
    def test_trending_series(self, execute_task):
        task = execute_task('test_trending_list')
        assert len(task.entries) == 10
        assert task.entries[0].get('title') == 'The Walking Dead (2010)'
        assert task.entries[1].get('title') == 'Homeland (2011)'

        assert task.entries[0].get('url') == 'https://trakt.tv/shows/the-walking-dead'
        assert task.entries[1].get('url') == 'https://trakt.tv/shows/homeland'

class TestTrendingMovieList(object):
    """
    This task generates entries based on the Trakt trending API endpoints.
    """

    config = """
        tasks:
          test_trending_list:
            trending_list:
              kind: movies
            exec: echo "Found {{title}}"
             """

    @pytest.mark.online
    def test_trending_movies(self, execute_task):
        task = execute_task('test_trending_list')
        assert len(task.entries) == 10
        assert task.entries[0].get('title') == 'Moana (2016)'
        assert task.entries[1].get('title') == 'Rogue One: A Star Wars Story (2016)'

        assert task.entries[0].get('url') == 'https://trakt.tv/movies/moana-2016'
        assert task.entries[1].get('url') == 'https://trakt.tv/movies/rogue-one-a-star-wars-story-2016'
