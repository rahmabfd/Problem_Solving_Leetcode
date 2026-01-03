# Write your MySQL query statement below
select EU.unique_id , E.name 
from Employees as E
Left join EmployeeUNI as EU ON E.id=EU.id