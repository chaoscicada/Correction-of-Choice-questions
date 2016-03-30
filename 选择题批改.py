student = open('F:\\助教\\text.txt', 'r')    
#将学生答案保存到text.txt中，不限答案形式

answer = open('F:\\助教\\answer.txt', 'r')                              
#将正确答案保存到answer.txt中，不限形式

a0 = list()  
for line in answer.readlines():                     #依次读取每行  
    line = line.strip()                             #去掉每行头尾空白  
    if not len(line) or line.startswith('#'):       #判断是否是空行或注释行  
        continue  
    a0.append(line)
a1 = ''.join(a0)
# print (str)

a2=''.join(x for x in a1 if (x >= 'a' and x <='z' )or(x >= 'A' and x <='Z' ))
#import re
#rule=re.compile(r'[^a-zA-z]')
#a2 = rule.sub('',a1)
#判断字符串str中的每个字符是否属于A-Z或a-z，是就提取并粘到一起

a3 = a2.upper()
#将提取后的字符全部大写
#print ('The right answers are:     ',a3)

s0 = list()  
for line in student.readlines():                    #依次读取每行  
    line = line.strip()                             #去掉每行头尾空白  
    if not len(line) or line.startswith('#'):       #判断是否是空行或注释行  
        continue  
    s0.append(line)
s1 = ''.join(s0)
# print (str)

s2=''.join(x for x in s1 if (x >= 'a' and x <='z' )or(x >= 'A' and x <='Z' ))

#import re
#rule = re.compile(r'[^a-zA-z]')
#s2 = rule.sub('',s1)
#判断字符串str中的每个字符是否属于A-Z或a-z，是就提取并粘到一起

s3 = s2.upper()
#将提取后的字符全部大写

#print ("The student's answers are: ",s3)

length=len(s3)
#检测字符串处理后的长度

print('number of answers:',length)

value=0
for i in range(0, length):
	if s3[i] == a3[i]:
		value = value + 1
#将字符串与标准答案进行比对，正确一个加一分

print ('score:',value)