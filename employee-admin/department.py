#!/bin/python

class Department :
	employee = []
	def __init__(self, code, name) :
		self.code = code 
		self.name = name 

	def addEmployee(self, employee) :
		self.employee.append(employee)