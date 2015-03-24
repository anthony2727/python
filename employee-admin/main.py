#!/bin/python

from employee import Employee 
from department import Department

em1 = Employee("Anthony", "AnthonyRodriguez.itt@gmail.com")
em2 = Employee("Carlos", "Carlos@gmail.com")
em3 = Employee("Matt", "Matt@gmail.com")



dep = Department("001", "Administration")

dep.addEmployee(em1)
dep.addEmployee(em2)
dep.addEmployee(em3)

print dep.code, dep.name
print "----------------------"
for emp in dep.employee :
	print emp.name, emp.email, "\n\r"