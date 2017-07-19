#!/usr/bin/env python
import rospy
import roslib
import time
#import sys

from pioneer_sumo.msg import *
#from pioneer_sumo.msg import arma
#from pioneer_sumo.msg import motores
#from pioneer_sumo.msg import sensores_chao
#from pioneer_sumo.msg import sensores_dist


#Cria a classe do noo para publicar no motor
class ControleRobo():

	#Metodo criador da classe
	def __init__(self,num_robo):

		#defininc=do variaveis
		self.x=0
		self.y=5
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
		#rospy.spin()
		self.comando=motores()
		#inicio do comando do robo
		while not rospy.is_shutdown():
			if self.sensordist[0]==-1 and self.sensordist[1]==-1 and self.sensordist[2]==-1 and self.sensordist[3]==-1 and self.sensordist[4]==-1 and self.sensordist[5]==-1 and self.sensordist[6]==-1 and self.sensordist[7]==-1 and self.sensordist[8]==-1 and self.sensordist[9]==-1 and self.sensordist[10]==-1 and self.sensordist[11]==-1 and self.sensordist[12]==-1 and self.sensordist[13]==-1 and self.sensordist[14]==-1 and self.sensordist[15]==-1:
				if self.sensorTras1 >0.11 and self.sensorTras2 >0.11 :
						
					self.Re()
					self.pub.publish(self.comando)
							
				else:
						
					self.comando.motEsquerdo=0
					self.comando.motDireito=0
					self.GiraEsq()
					time.sleep(0.2)
					self.pub.publish(self.comando)
			elif self.sensorTras1 >0.11 and self.sensorTras2 >0.11 :
				if self.x>0.05:
					self.GiraEsq()
					rospy.loginfo("errado1")
				elif self.x<-0.05:
					self.GiraDir()
					rospy.loginfo("errado2")
				else:
					self.Acelera()
					rospy.loginfo("errado3")
			

	#Funcao girar para esquerda
	def GiraEsq(self):
		self.comando.motEsquerdo=-3
		self.comando.motDireito=3

		self.pub.publish(self.comando)
	#Funcao girar para direita
	def GiraDir(self):
		self.comando.motEsquerdo=3
		self.comando.motDireito=-3
		self.pub.publish(self.comando)
	# Funcao acelerar
	def Acelera(self):
		self.comando.motEsquerdo=3
		self.comando.motDireito=3
		self.pub.publish(self.comando)
	def Re(self):
		self.comando.motEsquerdo=-3
		self.comando.motDireito=-3
		self.pub.publish(self.comando)
			
	#funcao que le o sensor no chao
	def sensorChaoCallback(self,data):
		self.sensorTras1=data.dist_tras1
		self.sensorFrente1=data.dist_frente1
		self.sensorTras2=data.dist_tras2
		self.sensorFrente2=data.dist_frente2

	def sensorDistCallback(self,data):	
		self.sensordist=data.distancia

	
#Funcao main que chama a classe criada
if __name__ == '__main__':

	#Inicializa o nosso no com o nome
	rospy.init_node('cognicao', anonymous=True)

	#Instancia a classe e entra em um regime de tratamento de eventuais erros
	try:
		obj_no = ControleRobo(1)
	except rospy.ROSInterruptException: pass

