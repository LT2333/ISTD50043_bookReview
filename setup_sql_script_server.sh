echo "Transfer bash and SQL scripts"
scp -i database/sql/book_review_key.pem database/sql/load_sql_db.sh ubuntu@ec2-54-244-217-119.us-west-2.compute.amazonaws.com:~
scp -i database/sql/book_review_key.pem database/sql/load_data_sql.sql ubuntu@ec2-54-244-217-119.us-west-2.compute.amazonaws.com:~
scp -i database/sql/book_review_key.pem database/sql/store_user_information.sql ubuntu@ec2-54-244-217-119.us-west-2.compute.amazonaws.com:~
scp -i database/sql/book_review_key.pem database/sql/create_additional_tables.sql ubuntu@ec2-54-244-217-119.us-west-2.compute.amazonaws.com:~

echo "Execute the bash set-up script on the remote sql server"
ssh -i database/sql/book_review_key.pem ubuntu@ec2-54-244-217-119.us-west-2.compute.amazonaws.com 'bash -s' < database/sql/load_sql_db.sh



