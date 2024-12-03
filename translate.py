import re


def get():
    
    with open('dict.txt', 'r', encoding='utf-8') as f:
        data = f.read()
    # 使用正则表达式提取时期名称和年份
    pattern = r'(\S+):(?:前)?(\d+)年—(?:前)?(\d+)年'

    # 使用 findall 查找所有匹配
    matches = re.findall(pattern, data)

    for match in matches:
        name = match[0]  # Period name (元光, 元朔)
        start_year = match[1]  # Start year
        end_year = match[2]  # End year
        print(f"时期名称: {name}, 起始年份: {start_year}, 结束年份: {end_year}")

def translate_startyear(Emperor: str):
    with open('dict.txt', 'r', encoding='utf-8') as f:
        data = f.read()
    
    # 使用正则表达式提取时期名称和年份
    pattern = f'{Emperor}:(?:前)?(\d+)年—(?:前)?(\d+)年'

    # 使用 findall 查找所有匹配
    matches = re.findall(pattern, data)

    # 如果有匹配项，打印对应的结果
    if matches:
        for match in matches:
            start_year = match[0]  # 起始年份
            end_year = match[1]  # 结束年份
            print('Translate OK')
            return True,int(start_year)
    else:
        print(f"未找到 {Emperor} 的相关信息")
        return False,None
        
if __name__ == '__main__':
    _,year=translate_startyear('元光')
    print(year)
    