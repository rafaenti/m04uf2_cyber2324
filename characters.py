#!/usr/bin/python3

from xml.dom import minidom


facx = minidom.parse('characters.facx')


characters = facx.getElementsByTagName('character')

for character in characters:
	id = character.getAttribute('id')

	name = character.getElementsByTagName('name')
	name_value = name[0].firstChild.nodeValue

	age = character.getElementsByTagName('age')
	age_value = age[0].firstChild.nodeValue

	gender = character.getElementsByTagName('gender')
	gender_value = gender[0].getAttribute('value')

	level = character.getElementsByTagName('level')
	level_value = level[0].getAttribute('value')

	print(f"{id}\t {name_value}\t {age_value}\t {gender_value}\t {level_value}")


	print("-"*64)
