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
        assert task.entries[0].get('title') == 'The Walking Dead'
        assert task.entries[1].get('title') == 'Homeland'

        assert task.entries[0].get('url') == 'https://api.trakt.tv/shows/1393'
        assert task.entries[1].get('url') == 'https://api.trakt.tv/shows/1398'

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
        assert task.entries[0].get('title') == 'Moana'
        assert task.entries[1].get('title') == 'Rogue One: A Star Wars Story'

        assert task.entries[0].get('url') == 'https://api.trakt.tv/movies/175475'
        assert task.entries[1].get('url') == 'https://api.trakt.tv/movies/211396'
