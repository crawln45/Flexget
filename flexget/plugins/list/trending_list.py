from __future__ import unicode_literals, division, absolute_import

from flexget import plugin
from flexget.event import event
from flexget.entry import Entry
from flexget.plugins.internal.api_trakt import get_session, get_api_url


class TrendingList(object):

    schema = {
            'type': 'object',
            'properties': {
                'kind': { 'type': 'string', 'enum': ['series', 'movies'] }
            },
            'required': ['kind']
    }

    def on_task_input(self, task, config):
        kind = 'shows' if config['kind'] == 'series' else 'movies'
        url = get_api_url(kind, "trending")
        results = get_session().get(url).json()

        return [self._api_result_to_entry(result, kind) for result in results]

    def _api_result_to_entry(self, result, kind):
        key = kind[0:-1] # this is either 'serie' or 'movie'
        url = get_api_url(kind, result[key]['ids']['trakt'])

        return Entry(result[key]['title'], url)


@event('plugin.register')
def register_plugin():
    plugin.register(TrendingList, 'trending_list', api_ver=2)
