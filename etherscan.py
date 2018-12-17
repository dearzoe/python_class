#!/usr/bin/python
#coding:utf-8

"""
@author: wenzhe
@software: PyCharm
@file: etherscan.py
@time: 2018/12/17 9:33 PM
"""

import requests
from bs4 import BeautifulSoup
import json

class Crawler(object):
	def __init__(self):
		self.url = "https://etherscan.io/txs?p={}"
		self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
		self.data_list = []

	def get_url_list(self):
		list = []
		for pageNum in range(1, 5):
			list.append(self.url.format(pageNum))
		return list

	def send_request(self, url):
		data = requests.get(url, headers=self.headers).content.decode('utf-8')
		return data

	def bs4_data(self, data):
		bs4_data = BeautifulSoup(data, 'lxml')
		deal_list = bs4_data.select(".table-responsive table tbody tr")
		for pro_deal in deal_list:
			deal_dict = {}
			deal_dict['TxHash'] = pro_deal.select('td')[0].get_text()
			deal_dict['Block'] = pro_deal.select('td')[1].get_text()
			deal_dict['Age'] = pro_deal.select('td')[2].get_text()
			deal_dict['From'] = pro_deal.select('td')[3].get_text()
			deal_dict['To'] = pro_deal.select('td')[5].get_text()
			deal_dict['Value'] = pro_deal.select('td')[6].get_text()
			self.data_list.append(deal_dict)

	def save_deal_data(self):
		json.dump(self.data_list, open("deal.json", "w"))

	def start(self):
		url_list = self.get_url_list()
		for pro_url in url_list:
			data = self.send_request(pro_url)
			self.bs4_data(data)
		self.save_deal_data()

Crawler().start()