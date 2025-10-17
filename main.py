# 从键盘获取输入的一行字符
input_str = input()
# 初始化四种字符的计数为 0
letter_count = 0
digit_count = 0
space_count = 0
other_count = 0

# 遍历输入字符串中的每个字符
for char in input_str:
    # 判断是否为英文字符（字母）
    if char.isalpha():
        letter_count += 1
    # 判断是否为数字
    elif char.isdigit():
        digit_count += 1
    # 判断是否为空格
    elif char.isspace():
        space_count += 1
    # 其他情况则为其他字符
    else:
        other_count += 1

# 按照测试要求的格式输出（注意冒号为中文冒号，且冒号后有一个空格）
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
