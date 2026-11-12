from typing import Any

from common import RoleConstants

Config = dict[str, int | str | bool | dict[str, Any]]


class C(RoleConstants):
    NAME_IN_URL = 'experiment'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1

    GROUP_NAME = "live-%s-%s-%s"

    LLM_ERROR = 'No Connection to LLM server'
