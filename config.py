#coding:utf-8

station_name_url = 'http://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9009'

#test_url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-06-06&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=CQW&purpose_codes=ADULT'
#test_url2 = 'https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=55000K115240&from_station_no=01&to_station_no=15&seat_types=43&train_date=2017-06-06'

search_url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes={}'


seat_info_url = 'https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no={}&from_station_no={}&to_station_no={}&seat_types={}&train_date={}'

#from_station = '上海'
#to_station = '重庆'
#train_date = '2017-06-06'
people = 'ADULT'