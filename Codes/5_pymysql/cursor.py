import pymysql
import datetime

# 数据库连接配置（集中管理）
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "passwd": "pylor520",
    "db": "onlinedb",
    "port": 3306,
    "charset": "utf8",
}


def get_connection():
    """创建并返回数据库连接"""
    return pymysql.connect(**DB_CONFIG)


def insert_user(ulogin, uname, upwd, uregtime, ucredit, ucity):
    """向 users 表插入一条用户记录"""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = """
            insert into users(ulogin, uname, upwd, uregtime, ucredit, ucity)
            values (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (ulogin, uname, upwd, uregtime, ucredit, ucity))
        conn.commit()
        print("插入成功！")
        return True
    except Exception as e:
        print("插入失败：", e)
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()


# ========== 单独运行本文件时，执行测试插入 ==========
if __name__ == "__main__":
    import numpy as np

    int_ulog = np.random.randint(100000, 999999)
    str_uname = "namescope"
    str_upwd = "password_example@"
    time_uregtime = datetime.datetime.now()
    int_ucredit = 100
    str_ucity = "中国大陆"

    insert_user(int_ulog, str_uname, str_upwd, time_uregtime, int_ucredit, str_ucity)