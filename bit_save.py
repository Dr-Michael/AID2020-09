"""
二进制文件存储
"""

import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8')
cur = db.cursor()

# #   存储文件
##    注意图片后缀,如存储图片和导出图片后缀名不一样,则导出后无法查看
# with open('mysql.jpeg','rb') as fd:
#     data = fd.read()
# print(data)
# try:
      ##    注意图片后缀,如存储和导出图片后缀名不一样,则导出后无法查看
#     sql = "INSERT INTO Images (filename,data) VALUES ('mysql.jpeg',%s);"
#     #   用execute自动传参的方法将二进制内容传入语句
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print("Error:",e)

#   获取文件
sql = "SELECT * FROM Images where id=16;"
cur.execute(sql)
data = cur.fetchone()
print(data[2])
with open(data[1],"wb") as fd:
    # while True:
    #
    #     if not data:
    #         break
    fd.write(data[2])
    # fd.close()



cur.close()
db.close()