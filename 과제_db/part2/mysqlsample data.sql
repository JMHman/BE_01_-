USE classicmodels;

# 고객 조회
SELECT * FROM customers;

# 특정 제품 라인 제품들 조회
SELECT * FROM products
WHERE productLine = 'Classic Cars';

# 최근 주문 10건
SELECT * FROM orders
ORDER BY orderDate DESC
LIMIT 10;

# 최소 금액 이상 결제
SELECT * FROM payments
WHERE amount >= 100;

# 제품 라인별 제품 개수
SELECT productLine, COUNT(*) AS productCount
FROM products
GROUP BY productLine;

# 고객 별 총 주문 금액
SELECT customers.customerNumber, 
       customers.customerName, 
       SUM(orderdetails.quantityOrdered * orderdetails.priceEach) AS totalAmount
FROM customers
JOIN orders ON customers.customerNumber = orders.customerNumber
JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
GROUP BY customers.customerNumber, customers.customerName;

# 가장 많이 팔린 제품 top3
SELECT productName, SUM(quantityOrdered) AS totalQuantity
FROM orderdetails od
JOIN products p ON od.productCode = p.productCode
GROUP BY productName
ORDER BY totalQuantity DESC
LIMIT 3;

# 매출이 높은 사무실 순위 5
SELECT o.city, SUM(od.quantityOrdered * od.priceEach) AS totalSales
FROM orders ord
JOIN orderdetails od ON ord.orderNumber = od.orderNumber
JOIN customers c ON ord.customerNumber = c.customerNumber
JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
JOIN offices o ON e.officeCode = o.officeCode
GROUP BY o.city
ORDER BY totalSales DESC
LIMIT 5;

# 특정 금액 이상 주문 내역
SELECT orderNumber, SUM(quantityOrdered * priceEach) AS totalAmount
FROM orderdetails
GROUP BY orderNumber
HAVING totalAmount > 500;

# 평균 이상 구매 고객 목록
SELECT customerNumber, SUM(amount) AS totalPayment
FROM payments
GROUP BY customerNumber
HAVING totalPayment > (SELECT AVG(amount) FROM payments);

# 아직 주문이 없는 고객
SELECT customerName
FROM customers
WHERE customerNumber NOT IN (SELECT customerNumber FROM orders);

# 최대 매출 고객 top_3
SELECT c.customerName, SUM(od.quantityOrdered * od.priceEach) AS totalSpent
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
GROUP BY c.customerName
ORDER BY totalSpent DESC
LIMIT 3;

#신규 고객 추가 - 고객 넘버를 지정해주지 않아서 없데이트 안됨
INSERT INTO customers (customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
VALUES ('New Customer', 'Lastname', 'Firstname', '123-456-7890', '123 Street', 'Suite 1', 'City', 'State', 'PostalCode', 'Country', 1002, 50000.00);

# 제품 가격 인상
UPDATE products
SET buyPrice = buyPrice * 1.10
WHERE productLine = 'Classic Cars';

# 고객 이메일 추가 - 고객 정보 테이블의 행에는 이메일이 없어서 업데이트 안됨
UPDATE customers
SET email = 'newemail@example.com'
WHERE customerNumber = 103;

# 직원 전보
UPDATE employees
SET officeCode = '2'
WHERE employeeNumber = 1002;