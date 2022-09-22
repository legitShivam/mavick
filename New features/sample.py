import textwrap

str1 = 'shivam is a good boy. He knows Python, JavaScript, HTML, xml, CSS, SQL, '

str = textwrap.wrap(str1, width=20)

dic = {}
for  index, line in enumerate(str):
	var = " "
	endWhiteSpaceCount = 0
	while var == " ":
		if line.endswith(' '):
			endWhiteSpaceCount += 1
		var = line[-1]

	dic.update({index : endWhiteSpaceCount})
print(dic)
for i in str:
	print(i)


