# 15
# -- select Employees.*, Departments.* from Employees
# -- inner join Departments on Employees.department_id = Departments.department_id
# 16
# -- select Employees.*,
# --        case
# --            when Departments.name is not NULL then Departments.name
# --            else 'N/A'
# --        end as department_name
# -- from Employees
# -- left join Departments on Employees.department_id = Departments.department_id;
# 17
# -- select Employees.* from Employees
# -- where department_id is NULL
# 18
# -- select count(*) as employes_amount from Employees
# 19 I wasn't sure if in this question I was asked to provide average per employee or all of them combined so I did both
# -- select Employees.*, avg(salary) as avg_salary from Employees
# -- group by name
# -- select avg(salary) as avg_salary_between_all_employes from Employees
# 20
# -- select max(salary) as biggest_salary, name,department_id from Employees
# -- where department_id not NULL
# -- group by department_id
# 21
# -- select Employees.*, Departments.budget,Departments.building,Departments.name from Employees
# -- left join Departments on Employees.department_id = Departments.department_id
# -- order by seniority asc;
# 22
# -- select avg(salary) as avg_salary_per_seniority,seniority from Employees
# -- group by seniority
# -- order by seniority asc;
# 23
# -- alter table Departments I had to alter and add each column one by one for some reason
# -- add number_of_employees integer,
# -- add avg_salary integer,
# -- add biggest_salary integer,
# -- add avg_seniority integer;
# -- update Departments set number_of_employees = ( select count(*) from Employees where Employees.department_id = Departments.department_id )
# -- update Departments set avg_salary = ( select avg(salary) from Employees where Employees.department_id = Departments.department_id )
# -- update Departments set avg_seniority = ( select round(avg(seniority)) from Employees where Employees.department_id = Departments.department_id )
# -- update Departments set biggest_salary  = ( select max(salary) from Employees where Employees.department_id = Departments.department_id )
