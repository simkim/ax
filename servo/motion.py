import json

class Position:
	def __init__(self, filename):
		self.json = json.load(file(filename))
	def __call__(self, network):
		# todo use SyncWrite
		for ident, config in self.json.items():
			network.get_servo(int(ident)).goal_position = int(config["current_position"])

