import os
import json
import urllib2
from ConfigParser import ConfigParser
from tabulate import tabulate


config = ConfigParser()
config.read(os.path.expanduser('~/.twitch-cli/config.ini'))
ACCESS_TOKEN = config._sections['Twitch']['access_token']


class BaseApi(object):
    version = 'v3'
    type = 'json'
    access_token = ACCESS_TOKEN
    url = None
    allow_argument = []
    raw_data = None
    data = None
    display_data = []
    display_header = []

    def __init__(self, args):
        pass

    def get_header(self):
        return {
            'Authorization': 'OAuth %s' % self.access_token,
            'Accept': 'application/vnd.twitchtv.%s+%s' % (self.version, self.type)
        }

    def execute(self):
        request = urllib2.Request(self.url, headers=self.get_header())
        response = urllib2.urlopen(request)
        self.raw_data = response.read()
        self.data = json.loads(self.raw_data)

    def pretty_print(self):
        print tabulate(self.display_data, headers=self.display_header)


class ApiArgument(object):
    name = ''
    type = None
    help = ''

    def __init__(self, name, type, help):
        self.name = name
        self.type = type
        self.help = help

    def get_kwargs(self):
        return {
            'name': self.name,
            'type': self.type,
            'help': self.help
        }


class ApiRouter(object):
    apis = {}

    def __init__(self, apis):
        self.apis = apis

    def add_api(self, api_name, api_class):
        self.apis[api_name] = api_class

    def remove_api(self, api_name):
        del self.apis[api_name]

    def get_argument(self, api_name):
        return self.apis[api_name].allow_argument

    def get_arguments(self):
        args = {}

        for k, v in self.apis.iteritems():
            args[k] = v.allow_argument

        return args
