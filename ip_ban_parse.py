# -*- coding: utf-8 -*-
# @Author: cyang
# @Date:   2018-06-09 10:57:03
# @Last Modified by:   cyang
# @Last Modified time: 2018-06-09 11:52:05

out_file_name = 'merge.txt'

def ip_parse(in_file_name):
	total = 0
	out = open(out_file_name, 'a+')
	out.write('----------------------- %s --------------------------------\n'%in_file_name)

	with open(in_file_name, "r") as f:
		content = f.readlines()
		for line in content:
			ip, count = line.split('=')
			if int(count) > 10:
				print('ip:',ip,'count', count)
				out.write(line)
			total += 1

	print('total', total)			

def find_duplicate(in_file_name):
	ip_dict = {}

	with open(in_file_name, 'r') as f:
		content = f.readlines()
		for line in content:
			if '--' not in line:
				# print(line)
				ip = line.split('=')[0].rstrip()
				# print(ip)
				if ip not in ip_dict:
					ip_dict[ip] = 1
				else:
					ip_dict[ip] += 1

	for key in ip_dict:
		if ip_dict[key] > 1:
			print(key, ip_dict[key])

	# print(ip_dict)				 		

if __name__ == '__main__':
	# ip_parse('mm_ban.txt')
	# ip_parse('ny_ban.txt')
	# ip_parse('do_ban.txt')

	find_duplicate(out_file_name)
