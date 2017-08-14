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

		#definindo variaveis
		self.x1=0
		self.y1=0
		self.sensordist=[None]*16
		self.sensorTras1=0
		self.sensorFrente1=0
		self.sensorTras2=0
		self.sensorFrente2=0
		self.torqueMotDir=0
		self.torqueMotEsq=0
		rospy.loginfo("Num Robo "+ str(num_robo))

		self.pub = rospy.Publisher('vrep_ros_interface/robo'+str(num_robo)+'/motores', motores, queue_size=1)
		#rospy.Subscriber('joy', Joy, self.joy_callback)
		rospy.Subscriber('vrep_ros_interface/robo'+str(num_robo)+'/sensoresChao',sensores_chao,self.sensorChaoCallback)	
		rospy.Subscriber('vrep_ros_interface/robo'+str(num_robo)+'/sensoresDist',sensores_dist,self.sensorDistCallback)	
		rospy.Subscriber('vrep_ros_interface/robo'+str(num_robo)+'/coordenadas', coord, self.coordCallback)
		rospy.Subscriber('vrep_ros_interface/robo'+str(num_robo)+'/torqueMot', motores, self.torqueMotCallback)	
		#rospy.spin()
		self.comando=motores()
		#inicio do comando do robo
		while not rospy.is_shutdown():
			print("Direito", self.torqueMotDir)
			print("Esquerdo", self.torqueMotEsq)
			if self.sensorTras1 == 0:
				self.Acelera(1.5)
				self.GiraDir(1.5)
			if self.sensorTras2 == 0:
				self.Acelera(1.5)
				self.GiraEsq(1.5)
			if self.sensorFrente1 == 0:
				self.Re(1.5)
				self.GiraEsq(1.5)
			if self.sensorFrente2 == 0:
				self.Re(1.5)
				self.GiraDir(1.5)
			if self.torqueMotEsq == 3 and self.torqueMotDir == 3:
				time.sleep(1.5)
				if self.torqueMotEsq == 3 and self.torqueMotDir == 3:
					i = 0
					while i < 70 and self.sensorTras1 >0.11 and self.sensorTras2 >0.11 and self.sensorFrente1 >0.11 and self.sensorFrente2 >0.11 :
						self.Acelera(1.5)
						time.sleep(0.1)
						self.GiraDir(1.2)
						time.sleep(0.08)
						i += 1
						print("entrou no loop 1")
						print(i)
			elif self.torqueMotEsq == -3 and self.torqueMotDir == -3:
				time.sleep(1.5)
				if self.torqueMotEsq == -3 and self.torqueMotDir == -3:
					i = 0
					while i < 70 and self.sensorTras1 >0.11 and self.sensorTras2 >0.11 and self.sensorFrente1 >0.11 and self.sensorFrente2 >0.11 :
						self.Re(1.5)
						time.sleep(0.1)
						self.GiraDir(1.2)
						time.sleep(0.08)
						i += 1
						print("entrou no loop 2")
						print(i)
			if self.x1==0 and self.y1==0:
				if self.sensorTras1 >0.11 and self.sensorTras2 >0.11:
					self.Re(1.5)
				else:						
					self.comando.motEsquerdo=0
					self.comando.motDireito=0
					self.GiraEsq(1.5)
					time.sleep(0.8)
					self.pub.publish(self.comando)
			elif self.sensorTras1 >0.11 and self.sensorTras2 >0.11 and self.sensorFrente1 >0.11 and self.sensorFrente2 >0.11:
				if self.x1>0.1 and self.x1<0.5:
					if self.y1<0.1 and self.y1>-0.1:
						self.Acelera(1.5)
					elif self.y1>0.095:
						self.GiraEsq(1.5)
						time.sleep(0.1)
					elif self.y1<-0.095:
						self.GiraDir(1.5)
						time.sleep(0.1)
				elif self.x1<-0.1 and self.x1>-0.5:
					if self.y1<0.1 and self.y1>-0.1:
						self.Re(1.5)
					elif self.y1>0.095:
						self.GiraDir(1.5)
						time.sleep(0.1)
					elif self.y1<-0.095:
						self.GiraEsq(1.5)
						time.sleep(0.1)
				elif self.x1>0.5:
					self.Acelera(1.5)
				elif self.x1<-0.5:
					self.Re(1.5)

	#Funcao girar para esquerda
	def GiraEsq(self,i):
		self.comando.motEsquerdo=-i
		self.comando.motDireito=i
		self.pub.publish(self.comando)
	#Funcao girar para direita
	def GiraDir(self,i):
		self.comando.motEsquerdo=i
		self.comando.motDireito=-i
		self.pub.publish(self.comando)
	# Funcao acelerar
	def Acelera(self,i):
		self.comando.motEsquerdo=i
		self.comando.motDireito=i
		self.pub.publish(self.comando)
	def Re(self,i):
		self.comando.motEsquerdo=-i
		self.comando.motDireito=-i
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
	def torqueMotCallback(self,data):
		self.torqueMotDir=data.motDireito
		self.torqueMotEsq=data.motEsquerdo

	
#Funcao main que chama a classe criada
if __name__ == '__main__':

	#Inicializa o nosso no com o nome
	rospy.init_node('cognicao', anonymous=True)

	#Instancia a classe e entra em um regime de tratamento de eventuais erros
	try:
		obj_no = ControleRobo(2)
	except rospy.ROSInterruptException: pass