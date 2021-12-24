Describes setting up [sc-statistics-service](https://github.com/streetcomplete/sc-statistics-service)

```
sudo apt-get install git -y
cd ~/Desktop
mkdir sc_statistics_service_development
cd sc_statistics_service_development
git clone https://github.com/matkoniecz/fresh_database.git
cd fresh_database
bash install.sh
cd ..
cd sc-statistics-service
```

`const DB_HOST = "localhost";` in the config file ( note https://github.com/streetcomplete/sc-statistics-service/compare/master...matkoniecz:patch-3 - test this Visual Studio Container thingy )

after that you need to set username and password in the config file (mandatory?)

run

```
php -S 127.0.0.1:8000
```

in command line in `sc_statistics_service_development/sc-statistics-service` to allow locally testing some requests

For example you can visit http://127.0.0.1:8000/get_statistics.php?user_id=1722488 (this user id is for user account https://www.openstreetmap.org/user/Mateusz%20Konieczny/ )

You can obtain user id by visiting specific changeset, say https://www.openstreetmap.org/changeset/100000003 and following "osmChange XML" and looking for `uid=` that gives user id for author of given changeset.

# Looking around the database

to run command manually following would be the best to enter mysql prompt `sudo mysql -u root`

Following commands may be nice initial ones to look around
```
SHOW DATABASES;
SHOW GRANTS FOR statistics_user@localhost;
USE statistics; #switch to statistics database
SHOW TABLES; # once on specific database
SELECT * from changesets; # this should show that database started to be used after initial queries
```

# Importing data for testing

To request loading of changeset data (for example for user testing) one needs user ids for all users who ever used StreetComplete.

This can be obtained from changeset dumps which can be parsed, for example with [this script](https://github.com/matkoniecz/StreetComplete_usage_changeset_analysis#streetcomplete_edits_generate_csv_and_make_quest_summaryphp).

If this script will not be used [documentation there on obtaining changeset dump](https://github.com/matkoniecz/StreetComplete_usage_changeset_analysis#obtaining-input-data) can be still of interest.

After user ids are obtained then calling `php update_users.php $USER_ID` for each user id will fetch relevant changesets.
