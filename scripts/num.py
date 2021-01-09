#!/usr/bin/env python3

# SPDX-License-Identifier: BSD-3-Clause
#
#	Copyright (C) 2021  Ayaka Yui and Ryuichi Ueda. All right reserved.


import rospy
import random
import math
from std_msgs.msg import Int32

#素数を判定
def prime():
	i = 0
	flag = True
	
	x = random.randint(2, 100)
	
	if x == 2:		#2は素数
		pub.publish(x)
		return
		
	for i in range(2, (int(math.sqrt(x))) + 1):	#2からx^(1/2)まで
		if (x % i) == 0:	#あまり0はbreak
			flag = False
			break
			
	if i == (int(math.sqrt(x))) and flag == True:
		pub.publish(x)
		
		
if __name__ == '__main__':
	rospy.init_node('num')
	pub = rospy.Publisher('num', Int32, queue_size = 1)
	rate = rospy.Rate(5)
	
	while not rospy.is_shutdown():
		prime()
		rate.sleep()
