#!/usr/bin/env python
import rospy
import roslib
import time
#import sys

from pioneer_sumo.msg import *
from pioneer_groovy.msg import coord
#from pioneer_sumo.msg import arma
#from pioneer_sumo.msg import motores
#from pioneer_sumo.msg import sensores_chao
#from pioneer_sumo.msg import sensores_dist


#Cria a classe do noo para publicar no motor
class Bater():

	#Metodo criador da classe
	def __init__(self,num_robo):

		#defininc=do variaveis
		rospy.loginfo("Num Robo "+ str(num_robo))

		#self.pub = rospy.Publisher('vrep_ros_interface/robo'+str(num_robo)+'/motores', motores, queue_size=1)
		self.pub1 = rospy.Publisher('vrep_ros_interface/robo'+str(num_robo)+'/arma', arma, queue_size=1)
		rospy.Subscriber('vrep_ros_interface/robo'+str(num_robo)+'/coordenadas', coord, self.coordCallback)
		#rospy.Subscriber('joy', Joy, self.joy_callback)
		#rospy.Subscriber('vrep_ros_interface/robo'+str(num_robo)+'/sensoresChao',sensores_chao,self.sensorChaoCallback)	
		#rospy.Subscriber('vrep_ros_interface/robo'+str(num_robo)+'/sensoresDist',sensores_dist,self.sensorDistCallback)		

		#rospy.spin()
		#self.comando=motores()
		self.x1=0
		self.y1=0
		self.x=1;
		self.comando1=arma()
		#inicio do comando do robo
		#self.arma2(2)
		#time.sleep(1)
		#self.arma2(0)

		
		#self.arma1(2)
		#self.arma1(0)
		

		while not rospy.is_shutdown():

			if self.x==1:
				self.arma1(2)
				self.arma1(2)
				self.arma1(0)
				self.arma2(2)
				self.arma2(0)

			self.x=0
			'''if self.x1>0.1 and self.x1<0.5:
				while self.y1<0.1 and self.y1>-0.1:
					self.arma1(2)
					self.arma1(0)
					self.arma2(2)
					self.arma2(0)
					
			elif self.x1<-0.1 and self.x1>-0.5:
				while self.y1<0.1 and self.y1>-0.1:
					self.arma1(-2)
					self.arma1(0)
					self.arma2(2)
					self.arma2(0)'''
				
				

					
					

	#Funcao girar para esquerda
	def arma2(self,i):			
			self.comando1.motArma2=i
			self.pub1.publish(self.comando1)
			time.sleep(2)

	def arma1(self,i):			
			self.comando1.motArma1=i
			self.pub1.publish(self.comando1)
			time.sleep(1)

	def arma3(self,i):			
			self.comando1.motArma2=i
			self.comando1.motArma1=i
			self.pub1.publish(self.comando1)
			time.sleep(1)

	def coordCallback(self,data):	
		self.x1=data.x
		self.y1=data.y
#Funcao main que chama a classe criada
if __name__ == '__main__':

	#Inicializa o nosso no com o nome
	rospy.init_node('mapeamento', anonymous=True)

	#Instancia a classe e entra em um regime de tratamento de eventuais erros
	try:
		obj_no = Bater(1)
	except rospy.ROSInterruptException: pass

