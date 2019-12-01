# Setting up mysql on a new EC2 instance

Instruction for using our automated script for mysql's installation, data downloading, data sql-loading

## Prerequisites
You need to have wget installed on your instances

```
sudo apt-get install wget
```

## Step 1 - download the setup script from our github repo
```
wget --output-document=new_instance_setup_sql.sh https://raw.githubusercontent.com/Jiankun0830/ISTD50043_bookReview/release/0.1.0/script/mysql_script/new_instance_setup_sql.sh?token=AKWIWQVCR3OQUX6WTMR2WUK53VE7K
```

## Step 2 - run the instance setup bash script

```
chmod +x new_instance_setup_sql.sh
```

```
./new_instance_setup_sql.sh
```