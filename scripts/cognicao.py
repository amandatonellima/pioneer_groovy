#!/usr/bin/env python
import rospy
import roslib
import time
#import sys

from pioneer_sumo.msg import *
from pioneer_groovy.msg import coord
#from pioneer_sumo.msg import motores
#from pioneer_sumo.msg import sensores_chao
#from pioneer_sumo.msg import sensores_dist


#Cria a classe do noo para publicar no motor
class ControleRobo():

	#Metodo criador da classe
	def __init__(self,num_robo):

		#defininc=do variaveis
		self.x1=0
		self.y1=0
		self.sensordist=[None]*16
		self.sensorTras1=0
		self.sensorFrente1=0
		self.sensorTras2=0
		self.sensorFrente2=0
		rospy.loginfo("Num Robo "+ str(num_robo))

		self.pub = rospy.Publisher('vrep_ros_interface/robo'+str(num_robo)+'/motores', motores, queue_size=1)
		#rospy.Subscriber('joy', Joy, self.joy_callback)
		rospy.Subscriber('vrep_ros_interface/robo'+str(num_robo)+'/sensoresChao',sensores_chao,self.sensorChaoCallback)	
		rospy.Subscriber('vrep_ros_interface/robo'+str(num_robo)+'/sensoresDist',sensores_dist,self.sensorDistCallback)	
		rospy.Subscriber('vrep_ros_interface/robo'+str(num_robo)+'/coordenadas', coord, self.coordCallback)	
		#rospy.spin()
		self.comando=motores()
		#inicio do comando do robo
		while not rospy.is_shutdown():
			if self.x1==0 and self.y1==0:
				if self.sensorTras1 >0.11 and self.sensorTras2 >0.11 :
						
					self.Re()
					self.pub.publish(self.comando)
							
				else:
						
					self.comando.motEsquerdo=0
					self.comando.motDireito=0
					self.GiraEsq()
					time.sleep(1)
					self.pub.publish(self.comando)
			elif self.sensorTras1 >0.11 and self.sensorTras2 >0.11 :
				if self.y1>0 and self.x1>0:
					self.comando.motEsquerdo=0
					self.comando.motDireito=0
					
					self.GiraEsq1()
					time.sleep(0.5)
					self.Acelera()
					self.pub.publish(self.comando)
					
				elif self.y1>0 and self.x1<0:
					self.comando.motEsquerdo=0
					self.comando.motDireito=0
					
					self.GiraDir1()
					time.sleep(0.5)
					self.Re()
					self.pub.publish(self.comando)
				elif self.y1<0 and self.x1<0:
					self.comando.motEsquerdo=0
					self.comando.motDireito=0
					time.sleep(0.5)
					
					self.GiraEsq1()
					time.sleep(0.5)
					self.Re()
					self.pub.publish(self.comando)
				else:
					self.comando.motEsquerdo=0
					self.comando.motDireito=0
					time.sleep(0.5)
					self.GiraDir1()
					time.sleep(0.5)
					self.Acelera()
					self.pub.publish(self.comando)
					
			

	#Funcao girar para esquerda
	def GiraEsq(self):
		self.comando.motEsquerdo=-1.5
		self.comando.motDireito=1.5

		self.pub.publish(self.comando)
	#Funcao girar para direita
	def GiraDir(self):
		self.comando.motEsquerdo=1.5
		self.comando.motDireito=-1.5
		self.pub.publish(self.comando)
	def GiraEsq1(self):
		self.comando.motEsquerdo=-0.3
		self.comando.motDireito=0.3

		self.pub.publish(self.comando)
	#Funcao girar para direita
	def GiraDir1(self):
		self.comando.motEsquerdo=0.3
		self.comando.motDireito=-0.3
		self.pub.publish(self.comando)
	# Funcao acelerar
	def Acelera(self):
		self.comando.motEsquerdo=1.5
		self.comando.motDireito=1.5
		self.pub.publish(self.comando)
	def Re(self):
		self.comando.motEsquerdo=-1.5
		self.comando.motDireito=-1.5
		self.pub.publish(self.comando)
			
	#funcao que le o sensor no chao
	def sensorChaoCallback(self,data):
		self.sensorTras1=data.dist_tras1
		self.sensorFrente1=data.dist_frente1
		self.sensorTras2=data.dist_tras2
		self.sensorFrente2=data.dist_frente2

	def sensorDistCallback(self,data):	
		self.sensordist=data.distancia
	def coordCallback(self,data):	
		self.x1=data.x
		self.y1=data.y

	
#Funcao main que chama a classe criada
if __name__ == '__main__':

	#Inicializa o nosso no com o nome
	rospy.init_node('cognicao', anonymous=True)

	#Instancia a classe e entra em um regime de tratamento de eventuais erros
	try:
		obj_no = ControleRobo(1)
	except rospy.ROSInterruptException: pass

