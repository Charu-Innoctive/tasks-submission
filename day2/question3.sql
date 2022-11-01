SELECT name, contact_number, email_id, city_state
FROM user_master
INNER JOIN city_master ON user_master.city_id = city_master.id where (blood_group='A+' or blood_group='B+' and name like '%a%') 
order by user_master.id 
limit 5,10;