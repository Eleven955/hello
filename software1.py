import re

source_txt = open("c.txt").read()
goal_words = {"auto", "break", "case", "char", "const",
              "continue", "default", "do", "double", "else",
              "enum", "extern", "float", "for", "goto",
              "if", "int", "long", "register", "return",
              "short", "signed", "sizeof", "static", "struct",
              "switch", "typedef", "union", "unsigned", "void",
              "volatile", "while"}
source_words = re.split('\\W+', source_txt)
# print(source_words)
total_num = 0
switch_num = 0
case_num = {}
case_num_index = 0
check_words = {"switch", "case", "if", "else"}
for word in source_words[::-1]:
    if word in goal_words:
        # print(word)
        total_num = total_num + 1
    else:
        source_words.remove(word)
for word in source_words[::-1]:
    if word not in check_words:  # remove不存在元素会出错
        source_words.remove(word)
# 列表删除元素问题:倒序删除，不口以正序删除
# print(source_words)
print("total num:", total_num)

source_words_len = len(source_words)
for i in range(source_words_len):
    if source_words[i] == "switch":
        switch_num = switch_num + 1
        j = i + 1
        # print(i)
        while source_words[j] == "case":
            j = j + 1
        # print(j)
        case_num[case_num_index] = j - i - 1
        i = j
        case_num_index = case_num_index + 1
    # if source_words[i] == "if":

print("switch num:", switch_num)
print("case num:", end=" ")
for num in case_num:
    print(case_num[num], end=" ")
print("\t")
# 这里如果print(num)会打印索引值，有点奇怪子

# 这个if else还嵌套来嵌套去的 估计需要重新切割 想办法让elseif黏在一起
source_txt = open("c.txt").read()
source_words = re.split('(\\W+)', source_txt)
# print(source_words)
# 抓取if else (else if)
if_elseif_words = []  # 集合与字典区别？？ 集合无序 列表有序
source_words_len = len(source_words)
while i < source_words_len:
    if source_words[i] == "else":
        if source_words[i + 1] == " " and source_words[i + 2] == "if":
            if_elseif_words.append("elseif")
            i = i + 3  # 不能用for只能用while，for每次都从range里取下一个
            continue
        else:
            if_elseif_words.append("else")
    elif source_words[i] == "if":
        if_elseif_words.append("if")
    i += 1
# print(if_elseif_words)
# 碰到else时可能结束 什么情况可以结束？
if_else_num = 0
if_elseif_else_num = 0
else_num = 0
if_elseif_words_len = len(if_elseif_words)
for i in range(if_elseif_words_len):
    if if_elseif_words[i] == "else":
        else_num += 1
        if if_elseif_words[i - 1] == "if":
            if_else_num += 1
print("if-else num:", if_else_num)
print("if-elseif-else num:", else_num - if_else_num)
