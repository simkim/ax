import dynamixel
import serial

class ServoNetwork:
	def __init__(self, config, exit_on_error=True):
		baudrate = config.get("net", "baudrate")
		port = config.get("net", "port")
		try:
			s = dynamixel.SerialStream(port=port, baudrate=baudrate, timeout=1)
		except serial.SerialException, e:
			print e
			if exit_on_error:
				import sys
				sys.exit(1)
			else:
				raise
		self.net = dynamixel.DynamixelNetwork(s)
		self.config = config
	def get_servo(self, ident):
		d = dynamixel.Dynamixel(ident, self.net)
		d.synchronized = False
		servo_config = self.config.get_config_for_servo_id(ident)
		d.config = servo_config
		return d
	def get_servo_by_label(self, label):
		servo_config = self.config.get_config_for_servo_label(label)
		assert servo_config
		d = dynamixel.Dynamixel(servo_config["id"], self.net)
		d.config = servo_config
		return d
	def apply_all(self, **kw):
		for ident in self.config.ids:
			d = self.get_servo(int(ident))
			for k, v in kw.items():
				setattr(d, k, v)
