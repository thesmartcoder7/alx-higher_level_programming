-- creates the MySQL server user user_0d_1

-- Check if the user already exists
SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = 'user_0d_1');

-- If the user doesn't exist, create the user and grant privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
