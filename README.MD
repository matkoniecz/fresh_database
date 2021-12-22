```
sudo apt-get install git -y
cd ~/Desktop
mkdir setup_statistics_service
cd setup_statistics_service
git clone https://github.com/matkoniecz/fresh_database.git
cd fresh_database
bash install.sh
```

run

```
php -S 127.0.0.1:8000
```

in command line to allow locally testing some requests

For example you can visit http://127.0.0.1:8000/get_statistics.php?user_id=1722488 (this user id is for user account https://www.openstreetmap.org/user/Mateusz%20Konieczny/ )

You can obtain user id by visiting specific changeset, say https://www.openstreetmap.org/changeset/100000003 and following "osmChange XML" and looking for `uid=` that gives user id for author of given changeset.
