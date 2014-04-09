from enum import Enum

class Status(Enum):
	online = 1
	offline = 2
	none = 3

COMMAND_LIST = [
	'say',
	'seed'
]