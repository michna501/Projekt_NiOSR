#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import cv2 as cv
import numpy as np
import math

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
			#dodajemy obszary do samego ruchu +-x
			cv.rectangle(img,(0,0),(400,200),(0,0,80),-1)
			cv.rectangle(img,(0,200),(400,400),(80,0,0),-1)
			#opisy jakies chociaz
			cv.putText(img,'X+',(20,40),cv.FONT_HERSHEY_SIMPLEX,1,(150,150,150),2,cv.LINE_AA)
			cv.putText(img,'X-',(20,380),cv.FONT_HERSHEY_SIMPLEX,1,(150,150,150),2,cv.LINE_AA)
			#cale pole do ruchu
			cv.circle(img,center,150,(80,80,80),-1)
			#ramka <3
			cv.circle(img,center,150,(50,50,50),3)
			#obszar wewnetrzny do samego obrotu +-z
			cv.circle(img,center,50,(50,50,50),-1)
			cv.line(img,(center[0],50),center,(200,10,0),4)
			if on:
				# wyznaczanie kata do obrotu zolwia
				dist = math.dist(center, click)
				angle = math.atan2(click[0] - center[0], -click[1] + center[1])/np.pi
				#jesli miescimy sie w ramce...
				if dist <150:
					#jak klikamy to rysujemy kreche od srodka do klika i koleczko, ez
					cv.line(img,center,click,(10,180,20+200*(dist<50)),3)
					msg.angular.z = -angle * 5.0
					#... i nie jestesmy w ciemnym polu
					if dist >50:
						msg.linear.x = (dist-50) / 100 * 5.0
				else:
					#jesli klikamy poza duzym kolem to robimy sam ruch +-x: czer+ nieb-
					msg.linear.x=((click[1]<center[1])*2-1)*3.0
					msg.angular.z=0.0
				#koleczko rysujemy zawsze przy kliku i tyle w temacie
				cv.circle(img,click,10,(0,20,200),2)
				#print(angle)
			else:
				msg.linear.x = 0.0
				msg.linear.y = 0.0
				msg.angular.z = 0.0

			# publikujemy wiadomosc, albo nic dla !on albo ruch liniowy i obrotowy wybrany przez pozycje klikniecia
			self.publisher_.publish(msg)
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
