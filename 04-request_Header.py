import urllib.request

def load_baidu():

	url = "https://www.baidu.com/"

	#请求网络
	#创建一个请求对象
	request = urllib.request.Request(url)
	#动态的去添加head的信息
	#添加了浏览器的信息
	request.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36")

	#urlopen此函数没有提供增加请求头的参数
	response = urllib.request.urlopen(request)
	data = response.read().decode("utf-8")

	#响应头
	# print(response.headers)
	#请求头
	# request_header = request.headers
	# print(request_header)

	with open("03-header.html","w")as f:
		f.write(data)

	#讲了一种 获取header的信息 百度查询一下第二种打印header的信息
	#设置header的信息 百度查询一下创建request的时候就添加请求头信息

load_baidu()