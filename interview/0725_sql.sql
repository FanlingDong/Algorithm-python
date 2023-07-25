-- 三个表，1。 customers，2.shippers, 3.orders
-- q1: get all customers' info

select * from customers

-- q2.Get all customer residing in Finland and their shipper ID
-- Customer Name, Shipper Id
select distinct c.name, s.shipperID
from customers c
join shippers s on c.shipperID = s.shipperID
join orders o on o.customerID = c.customerID
where c.country = 'Finland'

-- q3. Find the customer (CustomerName) with the most number of orders
select c.CustomerName, count(o.ordersID)
from customers c
join orders o on o.customerID = c.customerID
group by c.CustomerID
order by count(o.ordersID) limit 1
