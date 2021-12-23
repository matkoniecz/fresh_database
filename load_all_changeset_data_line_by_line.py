#import requests
import

# changeset data can be obtained with https://github.com/matkoniecz/StreetComplete_usage_changeset_analysis#streetcomplete_edits_generate_csv_and_make_quest_summaryphp

row_count = 0
# changeset_id,created_by,creation_date,changed_objects,user_id
os.chdir("~/Desktop/sc_statistics_service_development/sc-statistics-service") # make it more generic
with open('/OSMcache/edits_with_all_declared_software.csv') as fp:
    for line in fp:
        if row_count != 0:
            if "StreetComplete" in line.split(",")[1]:
                print(line)
                user_id = line.split(",")[-1]
                print(user_id)
                os.system("php update_users.php " + user_id)
                #url = "127.0.0.1:8000/get_statistics.php?user_id=" + user_id
            	#response = requests.get(url)
                #print(response.text)
        row_count += 1
