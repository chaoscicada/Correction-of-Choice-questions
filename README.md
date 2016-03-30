# Correction-of-Choice-questions

由于学生在SAKAI上提交的选择题答案形式各种各样，因此写了这个代码，这也是我的第一个有实际应用的代码 :)

本代码用于进行选择题评分，学生答案以及正确答案的形式不限

当文本中有中文括号与数字连在一起时，会在读取文件解码时出错

当文本不含中文字符时，可以使用正则表达式，在处理大文本（>300mb）速度稍快，但内存使用量较高

使用时，需要将学生答案、标准答案分别保存至text.txt、answer.txt文件中，需要在代买中指定两个文件的位置，默认的是我自己的存放位置，一定要修改。

虽然达不到自动化的程度，但是半自动我已经很开心了
