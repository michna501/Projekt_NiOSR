#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleController(Node):
	def __init__(self):
		super().__init__('turtle_controller')
		self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
		self.get_logger().info('proba123')
		msg = Twist()
		while True:
			x=float(input('podaj x: '))
			msg.linear.x = x
			self.publisher_.publish(msg)


def main(args=None):
	rclpy.init(args=args)
	turtle_node=TurtleController()
	rclpy.shutdown()

if __name__ =='__main__':
	main()
