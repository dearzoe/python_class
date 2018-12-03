import urllib.request
import urllib.parse
import string

def get_params():
	url = "http://www.baidu.com/s?"

	params= {
		"wd":"中文",
		"key":"zhang",
		"value":"san"
	}
	a = "张三"
	#判断

	#将字典转换成参数形式的字符串
	# result = str(params)
	# print(result)
	# 这个方法也可以将url转换成计算机可以识别的状态
	str_params = urllib.parse.urlencode(params)
	print(str_params,type(str_params))
	final_url = url+str_params

	#将带有中文的url转换成计算机可以识别的url
	#如果你的url已经是计算机可以识别的状态,那么不转换
	# end_url = urllib.parse.quote(final_url,safe=string.printable)

	response = urllib.request.urlopen(final_url)
	data = response.read().decode("utf-8")
	print(data)





get_params()