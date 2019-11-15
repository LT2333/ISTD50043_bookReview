start=`date +%s`

# Get kindle_reviews.csv
# estimated running time: 8s on EC2
wget https://database-project-50043.s3-us-west-2.amazonaws.com/kindle_reviews.csv
wget https://database-project-50043.s3-us-west-2.amazonaws.com/bookinfo.csv

# Load all the tables 
# estimated running time: 21s
ls
mysql -u root < load_data_sql.sql
mysql -u root < store_user_information.sql
mysql -u root < create_additional_tables.sql

end=`date +%s`

runtime=$((end-start))




# Print the running time
echo "Runtime was $runtime"



