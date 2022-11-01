-- insert for city_master

INSERT INTO city_master (id, city_name, city_state, added_date)
VALUES  (
        1101,
        'Mumbai',
        'Maharashtra',
       DATE '2022-11-01'
    ),
    (
        1102,
        'Pune',
        'Maharashtra',
      DATE  '2022-10-31'
    ),
    (
        1103,
        'Bangalore',
        'Karnataka',
       DATE '2022-10-30'
    ),
     (
        1104,
        'kolkata',
        'West Bengal',
       DATE '2022-10-29'
    ),
     (
        1105,
        'Chennai',
        'Tamil Nadu',
       DATE '2022-10-28'
    )
    
    
   
INSERT INTO user_master (id,name, contact_number, email_id, blood_group, city_id)
 VALUES  (
         100,
         'Charu',
         9920828901,
        'charu@innoctive.com',
        'B+',
        '1101'
     );
     
ALTER TABLE user_master ADD added_date date;

update user_master set added_date='2022-11-01' where id='100';

 


select*from user_master;



