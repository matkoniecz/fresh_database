cd ..
git clone https://github.com/streetcomplete/sc-statistics-service.git
cd sc-statistics-service
cp  config.sample.php config.php # this setting file can be modified, not just blindly copied (in such case amend later lines)
cd ..
sudo apt-get install -y php mariadb-server
# ideally following would read from config.php rather than assume that it is unmodified
sudo mysql -u root -e "CREATE DATABASE statistics;"
sudo mysql -u root -e "CREATE USER statistics_user@localhost IDENTIFIED BY 'statistics_pw';"
sudo mysql -u root -e "GRANT ALL PRIVILEGES ON statistics.* TO statistics_user@localhost;"
sudo mysql -u root -e "FLUSH PRIVILEGES;"

# to run command manually following would be the best to enter mysql prompt
# sudo mysql -u root
#
# following commands may be nice initial ones to look around
# SHOW DATABASES;
# SHOW GRANTS FOR statistics_user@localhost;
# USE statistics; #switch to statistics database
# SHOW TABLES; # once on specific database
# SELECT * from changesets; # this should show that database started to be used after initial queries
