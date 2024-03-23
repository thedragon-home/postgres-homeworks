-- SQL-команды для создания таблиц
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
  	title VARCHAR(50),
  	birth_date date,
  	notes TEXT 
);

SELECT * FROM employees

CREATE TABLE customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    company_name VARCHAR(50),
    contact_name VARCHAR(50),
    email VARCHAR(100)
);

SELECT * FROM customers

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id VARCHAR(50) REFERENCES customers(customer_id),
    employee_id INT REFERENCES employees(employee_id),
    order_date DATE,
    ship_city VARCHAR(15)
);

SELECT * FROM orders
