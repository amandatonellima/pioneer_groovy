#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import roslib
import numpy as np
import sys

from pioneer_sumo.msg import *
from pioneer_groovy.msg import *

#th1 = np.array([[-1, 0, 0, 0], [0, 0, -1, 0], [0, -1, 0, 0], [0, 0, 0, 1]])
#th2= np.array([[-0.766, 0.6428, 0, 0],	[0, 0, -1, 0],	[-0.6428, -0.766, 0, 0], [0, 0, 0, 1]])
#th3 = np.array([[-0.5, 0.866, 0, 0], [0, 0, -1, 0], [-0.866, -0.5, 0, 0], [0, 0, 0, 1]])
#th4 = np.array([[-0.1736, 0.9848, 0, 0], [0, 0, -1, 0], [-0.9848, -0.1736, 0, 0], [0, 0, 0, 1]])
#th5 = np.array([[0.1736, 0.9848, 0, 0], [0, 0, -1, 0], [-0.9848, 0.1736, 0, 0], [0, 0, 0, 1]])
#th6 = np.array([[0.5, 0.866, 0, 0], [0, 0, -1, 0], [-0.866, 0.5, 0, 0], [0, 0, 0, 1]])
#th7 = np.array([[0.766, 0.6428, 0, 0], [0, 0, -1, 0], [-0.6428, 0.766, 0, 0], [0, 0, 0, 1]])
#th8 = np.array([[1, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
#th9 = np.array([[1, 0, 0.0003, 0], [0.0003, 0, -1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
#th10 = np.array([[0.766, -0.6428, 0.0005, 0], [0.0004, -0.0003, -1, 0], [0.6428, 0.766, 0, 0], [0, 0, 0, 1]])
#th11 = np.array([[0.1736, -0.9848, 0.0007, 0], [0.0001, -0.0007, -1, 0], [0.9848, 0.1736, 0, 0], [0, 0, 0, 1]])
#th12 = np.array([[0.1736, -0.9848, 0.0021, 0], [0.0004, -0.0021, -1, 0], [0.9848, 0.1736, 0, 0], [0, 0, 0, 1]])
#th13 = np.array([[-0.1736, -0.9848, 0, 0],	[0, 0, -1, 0],	[0.9848, -0.1736, 0, 0], [0, 0, 0, 1]])
#th14 = np.array([[-0.5, -0.866, 0, 0],	[0, 0, -1, 0],	[0.866, -0.5, 0, 0], [0, 0, 0, 1]])
#th15 = np.array([[-0.766, -0.6428, 0, 0],	[0, 0, -1, 0],	[0.6428, -0.766, 0, 0], [0, 0, 0, 1]])
#th16 = np.array([[-1, 0, 0, 0], [0, 0, -1, 0], [0, -1, 0, 0], [0, 0, 0, 1]])
#th=[[[-1, 0, 0], [0, 0, -1], [0, -1, 0]],[[-0.766, 0.6428, 0],	[0, 0, -1],	[-0.6428, -0.766, 0]],[[-0.5, 0.866, 0], [0, 0, -1], [-0.866, -0.5, 0]],[[-0.1736, 0.9848, 0], [0, 0, -1], [-0.9848, -0.1736, 0]],[[0.1736, 0.9848, 0], [0, 0, -1], [-0.9848, 0.1736, 0]],[[0.5, 0.866, 0], [0, 0, -1], [-0.866, 0.5, 0]],[[0.766, 0.6428, 0], [0, 0, -1], [-0.6428, 0.766, 0]],[[1, 0, 0], [0, 0, -1], [0, 1, 0]],[[1, 0, 0.0003], [0.0003, 0, -1], [0, 1, 0]],[[0.766, -0.6428, 0.0005], [0.0004, -0.0003, -1], [0.6428, 0.766, 0]],[[0.1736, -0.9848, 0.0007], [0.0001, -0.0007, -1], [0.9848, 0.1736, 0]],[[0.1736, -0.9848, 0.0021], [0.0004, -0.0021, -1], [0.9848, 0.1736, 0]],[[-0.1736, -0.9848, 0],	[0, 0, -1],	[0.9848, -0.1736, 0]],[[-0.5, -0.866, 0],	[0, 0, -1],	[0.866, -0.5, 0]],[[-0.766, -0.6428, 0],	[0, 0, -1],	[0.6428, -0.766, 0]],[[-1, 0, 0], [0, 0, -1], [0, -1, 0]]]

th1 = np.matrix('-1.0 0 0 0.1064; 0 0 1.0 0.1382; 0 1.0 0 0; 0 0 0 1.0')
th2 = np.matrix('-0.7660 0 0.6428 0.1554; 0.6428 0 0.7660 0.1250; 0 1.0 0 0; 0 0 0 1.0')
th3 = np.matrix('-0.5000 0 0.8660 0.1906; 0.8660 0 0.50 0.0831; 0 1.0 0 0; 0 0 0 1.0')
th4 = np.matrix(' 0.1736 0 0.9848 0.2092; 0.9848 0 0.1736 0.0273; 0 1.0 0 0; 0 0 0 1.0')
th5 = np.matrix('0.1736 0 0.9848 0.2092; 0.9848 0 -0.1736 -0.0273; 0 1.0 0 0; 0 0 0 1.0000')
th6 = np.matrix('0.5000 0 0.8660 0.1906; 0.8660 0 -0.5000 -0.0785; 0 1.0000 0 0; 0 0 0 1.0000')
th7 = np.matrix('0.7660 0 0.6428 0.1555; 0.6428 0 -0.7660 -0.1202; 0 1.0000 0 0; 0 0 0 1.0000')
th8 = np.matrix('1.0000 0 0 0.1064; 0 0 -1.0 -0.1381; 0 1.0000 0 0; 0 0 0 1.0000')
th9 = np.matrix('1.0000 0 0 -0.1103; 0 0 -1.0 -0.1382; 0 1.0000 0 0; 0 0 0 1.0000')
th10 = np.matrix('0.7660 0 -0.6428 -0.1595; -0.6428 0 -0.7660 -0.1202; 0 1.0000 0 0; 0 0 0 1.0000')
th11 = np.matrix('0.5000 0 -0.8660 -0.1946; -0.8660 0 -0.5000 -0.0785; 0 1.0000 0 0; 0 0 0 1.0000')
th12 = np.matrix('0.1736 0 -0.9848 -0.2132; -0.9848 0 -0.1736 -0.0273; 0 1.0000 0 0; 0 0 0 1.0000')
th13 = np.matrix('-0.1736 0 -0.9848 -0.2132; -0.9848 0 0.1736 0.0273; 0 1.0000 0 0; 0 0 0 1.0000')
th14 = np.matrix('-0.5000 0 -0.8660 -0.1946; -0.8660 0 0.5000 0.0785; 0 1.0000 0 0; 0 0 0 1.0000')
th15 = np.matrix('-0.7660 0 -0.6428 -0.1595; -0.6428 0 0.7660 0.1203; 0 1.0 0 0; 0 0 0 1.0')
th16 = np.matrix('-1.0 0 0.0 -0.1103; 0.0 0 1.0 0.1382; 0 1.0 0 0; 0 0 0 1.0')
th = [th1, th2, th3, th4, th5, th6, th7, th8, th9, th10, th11, th12, th13, th14, th15, th16]

#Cria a classe do noo para publicar na msg coord
class CoordOponente():

	#Metodo criador da classe
	def __init__(self,num_robo):
		
		#definindo variaveis
		self.d = np.empty([1,16])
		self.vetcaixa = np.empty([2,1])

		rospy.loginfo("Num Robo "+ str(num_robo))

		self.pub = rospy.Publisher('vrep_ros_interface/robo'+str(num_robo)+'/coordenadas', coord, queue_size=1)
		rospy.Subscriber('/vrep_ros_interface/robo'+str(num_robo)+'/sensoresDist',sensores_dist,self.sensorDistCallback)
		#rospy.spin()
		coordcaixa=coord()

		while not rospy.is_shutdown():
			dist = np.amin(np.abs(self.d))
			indice = np.argmin(np.abs(self.d))
			transensor=np.array([[0],[0],[dist], [1]])
			if dist == 1:
				coordcaixa.x=0
				coordcaixa.y=0
				self.pub.publish(coordcaixa)
			else:
				vetcaixa=np.dot(th[indice],transensor)
				
				coordcaixa.x=vetcaixa[0]
				coordcaixa.y=vetcaixa[1]
				#rospy.loginfo(coordcaixa.x)
				self.pub.publish(coordcaixa)


	#Funcao que retorna a distancia (d)
	def sensorDistCallback(self,data):
		#rospy.loginfo(data)
		self.d = data.distancia


#Funcao main que chama a classe criada
if __name__ == '__main__':

	#Inicializa o nosso no com o nome
	rospy.init_node('th', anonymous=True)

	#Instancia a classe e entra em um regime de tratamento de eventuais erros
	try:
		obj_no = CoordOponente(2)
	except rospy.ROSInterruptException: pass