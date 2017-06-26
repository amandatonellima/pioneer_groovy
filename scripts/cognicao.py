#!/usr/bin/env python
import rospy
import roslib
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
		self.y=0
		self.sensorTras=0
		self.sensorFrente=0
		rospy.loginfo("Num Robo "+ str(num_robo))

		self.pub = rospy.Publisher('vrep_ros_interface/robo'+str(num_robo)+'/motores', motores, queue_size=1)
		#rospy.Subscriber('joy', Joy, self.joy_callback)
		rospy.Subscriber('vrep_ros_interface/robo'+str(num_robo)+'/sensoresChao',sensores_chao,self.sensorChaoCallback)		
		#rospy.spin()
		self.comando=motores()
		#inicio do comando do robo
		while not rospy.is_shutdown():
			if self.sensorFrente >0.1:
				if self.x>0.05:
					self.GiraEsq()
					rospy.loginfo("errado1")
				elif self.x<-0.05:
					self.GiraDir()
					rospy.loginfo("errado2")
				else:
					self.Acelera()
					rospy.loginfo("errado3")
			else:
				self.comando.motEsquerdo=0
				self.comando.motDireito=0
				self.pub.publish(self.comando)

	#Funcao girar para esquerda
	def GiraEsq(self):
		self.comando.motEsquerdo=-0.3
		self.comando.motDireito=0.3
		self.pub.publish(self.comando)
	#Funcao girar para direita
	def GiraDir(self):
		self.comando.motEsquerdo=0.3
		self.comando.motDireito=-0.3
		self.pub.publish(self.comando)
	# Funcao acelerar
	def Acelera(self):
		self.comando.motEsquerdo=3
		self.comando.motDireito=3
		self.pub.publish(self.comando)
			
	#funcao que le o sensor no chao
	def sensorChaoCallback(self,data):
		self.sensorTras=data.dist_tras
		self.sensorFrente=data.dist_frente

	
#Funcao main que chama a classe criada
if __name__ == '__main__':

	#Inicializa o nosso no com o nome
	rospy.init_node('cognicao', anonymous=True)

	#Instancia a classe e entra em um regime de tratamento de eventuais erros
	try:
		obj_no = ControleRobo(1)
	except rospy.ROSInterruptException: pass

