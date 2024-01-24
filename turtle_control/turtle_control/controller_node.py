#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import cv2 as cv
import numpy as np


on=False #czy jest wcisnieta myszka
center = (200,200) # tak o
click = center # tu wpisujemy kursora poz


#co robic gdy myszka w oknie
def turtleClick(event,x,y,flags,param):
	global on, click
	if event == cv.EVENT_LBUTTONDOWN:
#jak klikniemy to zapisujemy gdzie i ustawiamy rysowanie wskaznika
		on = True
		#print(f'{x} {y}')
		click = (x,y)
	elif event == cv.EVENT_RBUTTONDBLCLK:
#hehe
		print("that's RIGHT(right)!! ^_^")
	elif event == cv.EVENT_LBUTTONUP:
#jak puscimy to przestajemy
		on = False
		click = center
		#print("puszczono!")
	elif event == cv.EVENT_MOUSEMOVE:
# jak ruszymy to update pozycji i tyle
		click = (x,y)


class TurtleController(Node):
	global on, click,center
	def __init__(self):
		#jakis start
		super().__init__('turtle_controller')
		#robimy publisher zeby bylo to widac 
		self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
		#self.get_logger().info('proba123')
		msg = Twist()
		#robimy okno i piszemy co sie dzieje na klik
		cv.namedWindow("Turtle Controller")
		cv.setMouseCallback("Turtle Controller",turtleClick)

		while True:
			#x=float(input('podaj x: '))
			#msg.linear.x = x
			#self.publisher_.publish(msg)
			#zaczynamy rysowac, blank + front
			img = np.zeros((400,400,3), np.uint8)
			cv.line(img,(center[0],0),center,(200,10,0),4)
			if on:
				#jak klikamy to rysujemy kreche od srodka do klika i koleczko, ez
				cv.line(img,center,click,(10,180,20),3)
				cv.circle(img,click,10,(0,20,200),2)
				print(click)
			#rysujemy kolo na srodku
			cv.circle(img,center,10,(200,200,30),-1)
			#print(click)
			#pokazujemy image
			cv.imshow("Turtle Controller",img)
			#wcisniecie q wylacza controller
			k=cv.waitKey(50)
			if k == ord('q'):
				break



def main(args=None):
	rclpy.init(args=args)
	turtle_node=TurtleController()
	rclpy.shutdown()

if __name__ =='__main__':
	main()
