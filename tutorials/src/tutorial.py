#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import PoseStamped, Quaternion
import tf
 
pub = []
msg = PoseStamped()
 
def callback(data):
	msg.header.frame_id = "map"
	msg.header.seq = 0
	msg.header.stamp = rospy.Time.now()
	q = tf.transformations.quaternion_from_euler(0, 0, data.theta)
	msg.pose.orientation = Quaternion(q[0],q[1],q[2],q[3])
	msg.pose.position.x = data.x
	msg.pose.position.y = data.y
	pub.publish(msg)
	
if __name__ == '__main__':
	rospy.init_node('pose_rviz_python')
	pub = rospy.Publisher('pose_output', PoseStamped, queue_size=10)
	rospy.Subscriber('/turtle1/pose', Pose, callback, queue_size=1)
	rospy.spin()
