import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='4887',
    db='airbnb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    # 문제1 : 새로운 제품 추가
    # sql = "INSERT INTO products (productName, price, stockQuantity) VALUES(%s, %s, %s)"
    # cursor.execute(sql, ('Python book', 29.00, 50 ))
    # connection.commit()
    
    # 책이름 잘못 적어서 업데이트 함
    # sql = "UPDATE products SET productName = %s WHERE productid = %s"
    # cursor.execute(sql, ('Python Book',12))
    # connection.commit()

    # # 문제2 : 제품 정보 조회
    # cursor.execute("SELECT * FROM products")
    # for book in cursor.fetchall():
    #     print(book)

    # 문제3 : 제품 재고 업데이트
    # sql = "UPDATE products SET stockQuantity = stockQuantity - %s WHERE productid = %s"
    # cursor.execute(sql, (1,1))
    # connection.commit()

    # 문제4 : 고객별 총 주문 금액 계산
    # sql = "SELECT customerID, sum(totalAmount) FROM Orders GROUP BY customerID"
    # cursor.execute(sql)
    # datas = cursor.fetchall()
    # print(datas)

    # 문제5 : 고객 이메일 업데이트
    # spl = "UPDATE Customers SET email = %s WHERE customerID = %s"
    # cursor.execute(spl, ('update@email.com', 1))
    # connection.commit()

    # 문제6 :  주문 취소
    # sql = "DELETE FROM Orders WHERE orderID = %s"
    # cursor.execute(sql, (15))
    # connection.commit()

    # 문제7 : 특정 제품 검색
    # LIKE 쿼리는 특정 단어를 포함하는 정보를 찾을수 있게 해준다.
    # LIKE 쿼리는 LIKE 문법을 사용한다.(단어에 앞뒤로 %를 붙여준다.)
    # sql = "SELECT * FROM Products WHERE productName LIKE %s"
    # cursor.execute(sql, ('%Book%'))
    # datas = cursor.fetchall()

    # for data in datas:
    #     print(data['productName'])

    # 문제8 : 특정 고갱의 모든 주문 조회
    # spl = "SELECT * FROM Orders WHERE customerID = %s"
    # cursor.execute(spl, (2))
    # datas = cursor.fetchall()

    # for data in datas:
    #     print(data)

    # 문제9 : 가장 많이 주문한 고객 찾기(주문 횟수가 가장 많은 고객을 뽑아라.)
    sql = """
            SELECT customerID, COUNT(*) as ordercount 
            FROM Orders GROUP BY customerID 
            ORDER BY ordercount DESC LIMIT 1
            """
    cursor.execute(sql)
    
    data = cursor.fetchall()
    print(data)



cursor.close()