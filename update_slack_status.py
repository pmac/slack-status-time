#!/usr/bin/env python

import os
import time
from datetime import datetime

from slackclient import SlackClient


CLIENT = None
os.environ.setdefault('TZ', 'America/New_York')
time.tzset()


def get_client():
    global CLIENT
    if CLIENT is None:
        SLACK_TOKEN = os.environ['SLACK_TOKEN']
        CLIENT = SlackClient(SLACK_TOKEN)

    return CLIENT


def get_status():
    hour = datetime.now().hour
    if hour > 12:
        hour = hour - 12
        hour_scope = 'pm'
    else:
        hour_scope = 'am'

    return {
        'status_text': '%s%s in %s' % (hour, hour_scope, os.environ['TZ']),
        'status_emoji': ':clock%s:' % hour,
    }


def update_status():
    slack = get_client()
    status = get_status()
    print('Setting status:', status)
    resp = slack.api_call('users.profile.set', profile=status)


if __name__ == '__main__':
    update_status()
