
# coding=utf-8
import re
from lxml import etree

root = etree.XML('''\
<?xml version = "1.0"?>
<!DOCTYPE root SYSTEM "test" [<!ENTITY tasty "parnips">]>
<table border = "1">
<tr align="center" bgcolor="#4CBB17"><td><a href="./update.php?casenum=824461">Update</a></td><td>gogogog</td><td>F1</td><td>New</td><td>BeiJing</td><td>EALC</td><td>Clear</td><td>2019-06-03</td><td>2019-06-04</td><td>1</td><td><a href="./personal_detail.php?casenum=824461" target="_blank" title="6.3 8:00面签，全程排队查材料录指纹面试约1小时，VO给了蓝条显示通过，仅收走护照。回来查询显示AP。6.4 10:30查询显示issued。">detail</a> <img src="notes.png" align="top"></td></tr>
 <tr align="center"><td><a href="./update.php?casenum=824508">Update</a></td><td>求早日过che</td><td>H1</td><td>Renewal</td><td>BeiJing</td><td>ME</td><td>Pending</td><td>2019-06-01</td><td>0000-00-00</td><td>59</td><td><a href="./personal_detail.php?casenum=824508" target="_blank">detail</a></td></tr>
<tr align="center" bgcolor="red"><td><a href="./update.php?casenum=825032">Update</a></td><td>回到解放前</td><td>F1</td><td>New</td><td>BeiJing</td><td>EE</td><td>Reject</td><td>2019-06-01</td><td>2019-06-24</td><td>23</td><td><a href="./personal_detail.php?casenum=825032" target="_blank">detail</a></td></tr>
</table>
''')

print(u'所有内容:')

# res = r'<a .*?>(.*?)</a>'
# contents=root.xpath("//td")

# for i in range(1,2):
# contents=root.xpath('//table[@border="1"]/tr[1]/td')
contents = root.xpath('//tr[@align="center"]/td')

for content in contents:
    text = content.text
    print(text)
    
