# hip
# knee
# heel

HIP_TURN_SHIFT=90
HIP_REST_SHIFT=128
LEG_REST_SHIFT=250
KNEE_UP_FACTOR=1.6

FL_RIGHT=1
FL_LEFT=2
FL_FRONT=4
FL_MIDDLE=8
FL_BACK=16
FL_REVERSE=32
 
class Leg:
	def __init__(self, spider, hip_d, knee_d, heel_d, flags=0):
		self.spider = spider
		self.hip_d = hip_d
		self.knee_d = knee_d
		self.heel_d = heel_d
		self.hip_d.moving_speed=spider.moving_speed
		self.knee_d.moving_speed=spider.moving_speed
		self.heel_d.moving_speed=spider.moving_speed
		self.flags = flags
		self.disabled = False
	def hip_rest_shift(self):
		hip_shift = 0
		if not (self.flags & FL_MIDDLE):
			if self.flags & FL_REVERSE:
				hip_shift = HIP_REST_SHIFT
			else:
				hip_shift = -HIP_REST_SHIFT
		return hip_shift
	def leg_rest_shift(self):
		if self.flags & FL_REVERSE:
			return LEG_REST_SHIFT
		else:
			return -LEG_REST_SHIFT
	def hip_turn_shift(self):
		if self.flags & FL_LEFT:
			return -HIP_TURN_SHIFT
		else:
			return HIP_TURN_SHIFT
	def reset(self):
		self.center()
		self.down()
	def center(self):
		self.heel_d.goal_position = 512 + self.leg_rest_shift()
		self.hip_d.goal_position = 512 + self.hip_rest_shift()
	def front(self):
		if self.disabled:
			return
		self.hip_d.goal_position = 512 + self.hip_rest_shift() + self.hip_turn_shift()
	def back(self):
		if self.disabled:
			return
		self.hip_d.goal_position = 512 + self.hip_rest_shift() - self.hip_turn_shift()
	def up(self):
		if self.disabled:
			return
		self.knee_d.goal_position =  512 + int(KNEE_UP_FACTOR * self.leg_rest_shift())
		self.heel_d.goal_position = 512 + int(1.2 * self.leg_rest_shift())
	def down(self):
		if self.disabled:
			return
		self.knee_d.goal_position = 512 + self.leg_rest_shift()
		self.heel_d.goal_position = 512 + self.leg_rest_shift()
class Leg2(Leg):
	def front(self):
		if self.disabled:
			return
		sign = 1 if (self.flags & FL_REVERSE) else -1
		sign2 = 1 if (self.flags & FL_BACK) else 0
		self.heel_d.goal_position = 512+sign*(256+100*sign2)
	def back(self):
		if self.disabled:
			return
		sign = 1 if (self.flags & FL_REVERSE) else -1
		sign2 = 0 if (self.flags & FL_BACK) else 1
		self.heel_d.goal_position = 512+sign*(256+100*sign2)
	def up(self):
		if self.disabled:
			return
		self.knee_d.goal_position = 512 + int(KNEE_UP_FACTOR * self.leg_rest_shift())
	def down(self):
		if self.disabled:
			return
		self.knee_d.goal_position = 512 + self.leg_rest_shift()

class Spider:
	moving_speed = 0
	def __init__(self, leg_f_l, leg_f_r, leg_m_l, leg_m_r, leg_b_l, leg_b_r):
		self.leg_f_l = leg_f_l
		self.leg_f_r = leg_f_r
		self.leg_m_l = leg_m_l
		self.leg_m_r = leg_m_r
		self.leg_b_l = leg_b_l
		self.leg_b_r = leg_b_r
		self.legs = [leg_f_l, leg_f_r, leg_m_l, leg_m_r, leg_b_l, leg_b_r]

class KingSpider(Spider):
	def __init__(self, net):
		Spider.__init__(self,
			Leg(self, net[2], net[4], net[6], FL_LEFT | FL_FRONT | FL_REVERSE),
			Leg(self, net[1], net[3], net[5], FL_RIGHT | FL_FRONT),
			Leg(self, net[8], net[10], net[12], FL_LEFT | FL_MIDDLE),
			Leg(self, net[7], net[9], net[11], FL_RIGHT | FL_MIDDLE | FL_REVERSE),
			Leg(self, net[14], net[16], net[18], FL_LEFT | FL_BACK),
			Leg(self, net[13], net[15], net[17], FL_RIGHT | FL_BACK | FL_REVERSE)
		)
	def reset(self):
		for leg in self.legs:
			leg.reset()	
