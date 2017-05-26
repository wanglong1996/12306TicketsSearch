#coding:utf-8
"""命令行火车票查看器

Usage:
    test <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    

Example:
    test 北京 上海 2016-10-10
    test 成都 南京 2016-10-10
"""
import requests
from bs4 import BeautifulSoup
from config import *
from pprint import pprint
import json
from prettytable import PrettyTable
from colorama import init,Fore
from docopt import docopt


arguments = docopt(__doc__)
from_station = arguments['<from>']
to_station = arguments['<to>']
train_date = arguments['<date>']

name_to_id = {}
init()
x = PrettyTable(["车次","出发站-到达站","出发时间-到达时间","历时","商务座","特等座","一等座","二等座","高级软卧","软卧","硬卧","硬座","无座"])
x.align["车次"] = 'l'
x.padding_width = 1


def print_trian_info(money_list,*trains_list):	
	
	i = 0
	for train in trains_list:

		from_station_name = ''
		to_station_name = ''
		#根据值找键
		for (key,value) in name_to_id.items():
			if value == train['from_station']:
				from_station_name = key
			if value == train['to_station']:
				to_station_name = key
		
		item = money_list[i]
		i += 1
		
		from_station_name = Fore.BLUE+from_station_name+Fore.RESET
		to_station_name = Fore.GREEN +to_station_name+Fore.RESET
		x.add_row(  [train['train'],
					from_station_name+"\n"+to_station_name,
					train['start_time']+"--"+train['end_time'],
					train['time_consuming'],
					train['A9']+"\n"+item['A9'],
					train['P']+"\n"+item['P'],
					train['M']+"\n"+item['M'],
					train['O']+"\n"+item['O'],
					train['A6']+"\n"+item['A6'],
					train['A4']+"\n"+item['A4'],
					train['A3']+"\n"+item['A3'],
					train['A1']+"\n"+item['A1'],
					train['WZ']+"\n"+item['WZ']] )
	print(x)


def parse_station_name():
	url = 'https://kyfw.12306.cn/otn/leftTicket/init'
	r = requests.get(station_name_url,verify = False)
	r.encoding = 'utf-8'
	l =r.text.split('@')
	
	for i in range(1,len(l)):
		name = l[i].split('|')[1]
		id = l[i].split('|')[2]
		name_to_id[name] = id
	
def search_train(url):
	fromstation = name_to_id.get(from_station)
	tostation = name_to_id.get(to_station)
	final_url = url.format(train_date,fromstation,tostation,people)
	res = requests.get(final_url,verify=False)
	res.encoding = 'utf-8'
		
	rj = json.loads(res.text)
	results = rj['data']['result']
	trains_list= []
	money_list = []
	for item in results:
		trains_info = {}
		seat_info = {}
		l = item.split('|')
		for i in range(len(l)):
			if l[i] == '':
				l[i] = '#'

		
		trains_info['train'] = l[3]
		trains_info['from_station'] = l[6]
		trains_info['to_station'] = l[7]
		trains_info['start_time'] = l[8]
		trains_info['end_time'] = l[9]
		trains_info['time_consuming'] = l[10]

		trains_info['train_no'] = l[2]
		trains_info['from_station_no'] = l[16]
		trains_info['to_station_no'] = l[17]
		trains_info['train_date'] = train_date
		trains_info['seat_types'] = l[-1]

		trains_info['WZ'] = seat_info['WZ'] = l[26]
		trains_info['A4'] = seat_info['A4'] = l[23]
		trains_info['A6'] = seat_info['A6'] = l[21]
		trains_info['M'] = seat_info['M'] = l[31]
		trains_info['O'] = seat_info['O'] = l[30]
		trains_info['A9'] = seat_info['A9'] = l[32]
		trains_info['P'] = seat_info['P'] = l[25]
		trains_info['A3'] = seat_info['A3'] = l[28]
		trains_info['A1'] = seat_info['A1'] = l[29]
		trains_list.append(trains_info)
		money_dic =get_seat_info(trains_info['train_no'],trains_info['from_station_no'],trains_info['to_station_no'],trains_info['seat_types'],trains_info['train_date'],**seat_info)
		money_list.append(money_dic)
	pprint(money_list)
	print_trian_info(money_list,*trains_list)

				
def get_seat_info(train_no,from_station_no,to_station_no,seat_types,train_date,**seat_info):
	final_url = seat_info_url.format(train_no,from_station_no,to_station_no,seat_types,train_date)
	#print(final_url)
	req = requests.get(final_url,verify= False)
	req.encoding = 'utf-8'
	rj = json.loads(req.text)
	rj = rj['data']
	seat_keys_list = seat_info.keys()
		
	money_dic = {}
	for i in seat_keys_list:		
		if i in rj:
			money_dic[i] = rj[i]
		else:
			money_dic[i] = ''
		
	return money_dic
	
	
	
def main():

	parse_station_name()
	search_train(search_url)
	

if __name__ == '__main__':
	main()
    

