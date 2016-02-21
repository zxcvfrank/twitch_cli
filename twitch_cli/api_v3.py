from twitch_cli.api_base import *


class StreamChannel(BaseApi):
    url = 'https://api.twitch.tv/kraken/streams/'
    allow_argument = [
        ApiArgument('channel', str, 'Channel Name')
    ]

    def __init__(self, args):
        self.url += args.get('channel')


class StreamFollowed(BaseApi):
    url = 'https://api.twitch.tv/kraken/streams/followed'

    def pretty_print(self):
        display_columns = [
            'display_name',
            'status',
        ]

        data_list = []

        for stream in self.data.get('streams'):
            channel = stream.get('channel')
            channel_data = []

            for col in display_columns:
                channel_data.append(channel.get(col))

            data_list.append(channel_data)

        self.display_header = ['user_name', 'description', 'update_time']
        self.display_data = data_list

        return super(StreamFollowed, self).pretty_print()


v3_router = ApiRouter({
    'StreamChannel': StreamChannel,
    'list': StreamFollowed
})
