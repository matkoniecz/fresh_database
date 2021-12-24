cd ..
git clone https://github.com/streetcomplete/sc-statistics-service.git
cd sc-statistics-service
cp  config.sample.php config.php # this setting file can be modified, not just blindly copied (in such case amend later lines)
cd ..
sudo apt-get install -y php mariadb-server php-mysql php-curl php-xml
# ideally following would read from config.php rather than assume that it is unmodified
sudo mysql -u root -e "CREATE DATABASE statistics;"
sudo mysql -u root -e "CREATE USER statistics_user@localhost IDENTIFIED BY 'statistics_pw';"
sudo mysql -u root -e "GRANT ALL PRIVILEGES ON statistics.* TO statistics_user@localhost;"
sudo mysql -u root -e "FLUSH PRIVILEGES;"
