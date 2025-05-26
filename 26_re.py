# re 正则表达式
import re


# 学习正则表示
# \w 匹配字母、数字和下划线
# \W 匹配非字母、数字和下划线
# \d 匹配数字
# \D 匹配非数字
# \s 匹配空白字符
# \S 匹配非空白字符
# . 匹配除换行符外的任意字符
# ^ 匹配字符串开头
# $ 匹配字符串结尾
# * 匹配前面的字符零次或多次
# + 匹配前面的字符一次或多次
# ? 匹配前面的字符零次或一次
# {n} 匹配前面的字符恰好 n 次
# {n,} 匹配前面的字符至少 n 次
# {n,m} 匹配前面的字符至少 n 次，至多 m 次
# | 匹配多个模式中的任意一个
# [] 匹配括号内的任意一个字符
# () 分组匹配
# (?P<name>...) 命名分组
# (?P=name) 引用命名分组
# (?=...) 正向前瞻
# (?!...) 负向前瞻
# (?<=...) 正向后顾
# (?<!...) 负向后顾
# re.match() 匹配字符串开头
def match_example(string):
    pattern = r'\d{3}-\d{3,8}'
    match = re.match(pattern, string)
    if match:
        print('Match found:', match.group())
    else:
        print('No match found')
# re.search() 搜索字符串
def search_example(string):
    pattern = r'\d{3}-\d{3,8}'
    search = re.search(pattern, string)
    if search:
        print('Search found:', search.group())
    else:
        print('No match found')
# re.findall() 查找所有匹配
def findall_example(string):
    pattern = r'\d{3}-\d{3,8}'
    # string = 'My phone numbers are 010-12345 and 020-67890'
    matches = re.findall(pattern, string)
    print('All matches found:', matches)
# re.sub() 替换匹配的字符串
def sub_example(string):
    pattern = r'\d{3}-\d{3,8}'
    # string = 'My phone number is 010-12345'
    replaced_string = re.sub(pattern, 'XXX-XXXXXX', string)
    print('Replaced string:', replaced_string)
# re.split() 分割字符串
def split_example(string):
    pattern = r'\d{3}-\d{3,8}'
    # string = 'My phone numbers are 010-12345 and 020-67890'
    parts = re.split(pattern, string)
    print('Split parts:', parts)
# re.compile() 编译正则表达式
def compile_example(string):
    pattern = re.compile(r'\d{3}-\d{3,8}')
    # string = 'My phone number is 010-12345'
    match = pattern.match(string)
    if match:
        print('Compiled match found:', match.group())
    else:
        print('No match found with compiled pattern')
# re.escape() 转义特殊字符
def escape_example():
    special_string = 'Hello, (world)!'
    escaped_string = re.escape(special_string)
    print('Escaped string:', escaped_string)

# re.subn() 替换并返回替换次数
def subn_example():
    pattern = r'\d{3}-\d{3,8}'
    string = 'My phone number is 010-12345 and 020-67890'
    replaced_string, count = re.subn(pattern, 'XXX-XXXXXX', string)
    print('Replaced string:', replaced_string)
    print('Number of replacements:', count)

# re.fullmatch() 完全匹配整个字符串
def fullmatch_example():
    pattern = r'\d{3}-\d{3,8}'
    string = '010-12345'
    full_match = re.fullmatch(pattern, string)
    if full_match:
        print('Full match found:', full_match.group())
    else:
        print('No full match found')
# re.finditer() 返回匹配的迭代器
def finditer_example():
    pattern = r'\d{3}-\d{3,8}'
    string = 'My phone numbers are 010-12345 and 020-67890'
    matches = re.finditer(pattern, string)
    for match in matches:
        print('Match found:', match.group(), 'at position:', match.start())

# 正则表达式判断身份证号每一位的规则对错
def validate_id_card(id_card):
    pattern = r'^\d{6}(1[89]\d{2})|(20[012][0-5])\d{7}([\dX])$'
    if re.fullmatch(pattern, id_card):
        print('ID card format is valid')
    else:
        print('Invalid ID card format')


# 正则表达式的用法
def regex_usage_examples():
    match_example('010-12345')
    search_example('My phone number is 010-12345')
    findall_example('My phone numbers are 010-12345 and 020-67890')
    sub_example('My phone number is 010-12345')
    split_example('My phone numbers are 010-12345 and 020-67890')
    compile_example('My phone number is 010-12345')
    escape_example()
    subn_example()
    fullmatch_example()
    finditer_example()
    validate_id_card('11010519491231002X')
