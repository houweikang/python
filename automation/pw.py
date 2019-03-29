import re

phoneNumRegex = re.compile(r'(\(\d{3}\))-(\d{3}-\d{4})')
text = 'djlaksjfeiafjdkajhahafoka(012)-456-4895fdasifhiea'
print('电话号码：' + phoneNumRegex.search(text).group(2))