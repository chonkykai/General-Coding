SELECT employee.company_code, company.founder,
        COUNT(DISTINCT(employee.lead_manager_code)),
        COUNT(DISTINCT (employee.senior_manager_code)),
        COUNT(DISTINCT(employee.manager_code)),
        COUNT(DISTINCT(employee.employee_code))

FROM company
INNER JOIN employee 
ON company.company_code = employee.company_code
GROUP BY employee.company_code, company.founder;