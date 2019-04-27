from pymysql import connect

def main():
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='focusdroid')

    cursor = conn.cursor()

    for i in range(100000):
        cursor.execute('insert into test_index value("ha---%d")'% i)

    conn.commit()


if __name__ == '__main__':
    main()