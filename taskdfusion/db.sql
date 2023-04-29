--Working on arrays (examples)
--INSERT INTO array_sample (userid) values(ARRAY ['1']) WHERE name='sri';
--UPDATE array_sample SET userid=ARRAY_APPEND(userid, '1') WHERE name='sri';

taskdfusion=# \d accounts
                           Table "public.accounts"
  Column  |         Type          | Collation | Nullable |      Default       
----------+-----------------------+-----------+----------+--------------------
 uid      | uuid                  |           |          | uuid_generate_v4()
 name     | character varying(40) |           |          | 
 email    | character varying(40) |           |          | 
 password | character varying(40) |           |          | 

taskdfusion=# \d todo
                              Table "public.todo"
  Column   |          Type          | Collation | Nullable |      Default       
-----------+------------------------+-----------+----------+--------------------
 tid       | uuid                   |           |          | uuid_generate_v4()
 descript  | character varying(400) |           |          | 
 projectid | character varying(40)  |           |          | 
 status    | character varying(20)  |           |          | 
 assignee  | character varying(40)  |           |          | 

taskdfusion=# \d projects
                          Table "public.projects"
 Column |         Type          | Collation | Nullable |      Default       
--------+-----------------------+-----------+----------+--------------------
 pid    | uuid                  |           |          | uuid_generate_v4()
 prname | character varying(40) |           |          | 
 userid | character varying(40) |           |          | 

taskdfusion=# \d type
                        Table "public.type"
  Column   |         Type          | Collation | Nullable | Default 
-----------+-----------------------+-----------+----------+---------
 userid    | character varying(40) |           |          | 
 projectid | character varying(40) |           |          | 

taskdfusion=# \d array_sample 
                   Table "public.array_sample"
 Column |         Type          | Collation | Nullable | Default 
--------+-----------------------+-----------+----------+---------
 userid | character varying[]   |           |          | 
 name   | character varying(20) |           |          | 
