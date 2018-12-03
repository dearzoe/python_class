import urllib.request
import urllib.parse
import string

def get_method_params():
	url = "http://www.baidu.com/s?wd="
	#拼接参数
	name = "美女"

	final_url = url+name
	print(final_url)
	#将包含汉字的网址进行转译
	encode_new_url = urllib.parse.quote(final_url,safe=string.printable)
	print(encode_new_url)

	#代码发送网络请求
	response=urllib.request.urlopen(encode_new_url)

	#读取内容
	data = response.read().decode("utf-8")
	#保存到本地
	with open("02-baidu.html","w",encoding="utf-8")as f:
		f.write(data)
#ascii' codec can't encode characters
# in position 10-11: ordinal not in range(128)
#python是解释性语言;解析器只支持ascii(0-127)

get_method_params()