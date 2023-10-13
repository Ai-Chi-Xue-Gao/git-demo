"""
演示Python pymysql库的基础操作
"""
from pymysql import Connection
# 构建到MySQL数据库的链接
conn = Connection(
    host='localhost',   # 主机名(或IP地址)
    port=3306,          # 端口,默认3306
    user='root',        # 账户名
    password='root123',  # 密码
    autocommit=True
)

# 执行非查询性质SQL
cursor = conn.cursor()     # 获取游标对象
conn.select_db("school")   # 选择数据库
# 使用游标对象,执行sql语句
# cursor.execute("CREATE TABLE test_pymysql(id INT, info VARCHAR(255))")    # 创建一个表
# cursor.execute("DROP TABLE test_pymysql")

# 执行查询性质SQL
# cursor.execute("SELECT * FROM student")
# 获取查询结果
# results: tuple = cursor.fetchall()
# print(results)
# for r in results:
#     print(r)

# 插入数据
cursor.execute("insert into test_pymysql values(02,'天天向上')")
# 通过commit()确认数据更改
# conn.commit()
# 查询数据
cursor.execute("select * from test_pymysql")
results: tuple = cursor.fetchall()
print(results)

# 打印MySQL数据库软件信息
# print(conn.get_server_info())
# 关闭链接
conn.close()