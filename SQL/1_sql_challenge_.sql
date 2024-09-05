"""
In the dynamic world of web hosting, 
providing customers with a clear overview of their assets is key to enhancing user experience. 
A development team must create a feature for an online hosting customers panel 
that generates a dashboard report of all customers and the number of active websites they own.

The results should include the following columns:

email: the email address of the customer
total_active_sites: the total number of active websites for each customer
The results should be sorted in ascending order by email.

Note:

Only active websites should be included.
"""

SELECT customers.email, COUNT(sites.customer_id) AS total_active_sites
FROM customers
INNER JOIN sites
    ON customers.id = sites.customer_id
WHERE sites.is_active = 1
GROUP BY sites.customer_id
ORDER BY customers.email;