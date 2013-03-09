import ConfigParser

class ServoConfig(ConfigParser.SafeConfigParser):
	def __init__(self, filename="ax.ini"):
		ConfigParser.SafeConfigParser.__init__(self)
		self.readfp(open(filename))
		ids = self.get("net", "id")
		self.ids = []
		for _id in ids.split(","):
			_id = int(_id)
			self.ids.append(_id)
		self.load_config_for_servos()

	def get_config_for_servo_label(self, label):
		config = self.servo_by_label.get(label)
		return config

	def get_config_for_servo_id(self, ident):
		config = self.servo_by_id.get(int(ident))
		if not config:
			config = self.get_config_for_section("ax.unknown")
			config["id"] = ident
		return config

	def load_config_for_servos(self):
		self.servo_by_id = {}
		self.servo_by_label = {}
		for section in self.sections():
			if not section.startswith("ax."):
				continue
			config = self.get_config_for_section(section)
			self.servo_by_id[config["id"]] = config
			self.servo_by_label[config["label"]] = config
		return self.servo_by_id.values()
			
	def get_config_for_section(self, section):
		if section not in self.sections():
			config = { "label" : "unknown"}
			return config 
		return {
			"label" : self.get(section, "label") or "",
			"id" : int(section[3:])
		}
