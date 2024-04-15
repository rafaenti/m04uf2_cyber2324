#!/usr/bin/python3

from xml.dom import minidom


facx = minidom.parse('characters.facx')


characters = facx.getElementsByTagName('character')

for character in characters:
	name = character.getElementsByTagName('name')
	print(name[0].tagName)

	age = character.getElementsByTagName('age')
	print(age[0].tagName)
