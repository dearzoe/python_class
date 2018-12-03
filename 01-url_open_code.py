import urllib.request

def load_data():

	#url地址:
	url = "http://www.baidu.com/"
	#get请求 http请求
	#resonse 返回的响应对象
	resonse = urllib.request.urlopen(url)
	print(resonse)
# 	读取内容 bytes类型
	data = resonse.read()
	# print(data)
	#将文件获取的内容转换成字符串
	str_data = data.decode("utf-8")
	print(str_data)

	#将数据写入文件
	with open("baidu.html","w",encoding="utf-8")as f:
		f.write(str_data)


#如果你爬取回来的是bytes类型:但是你写入的时候需要字符串类型decode("utf-8")
#如果你爬取回来的是str类型:但是你写入的是bytes类型
	#将字符串类型转换成bytes类型
	str_name = "baidu"
	byte_name = str_name.encode("utf-8")
	print(byte_name)


load_data()


