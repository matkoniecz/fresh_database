#import requests
import sys
import os

def main():
    # changeset data can be obtained with https://github.com/matkoniecz/StreetComplete_usage_changeset_analysis#streetcomplete_edits_generate_csv_and_make_quest_summaryphp

    if len(sys.argv) != 2:
        print("call it with a single arguments specifying location of a csv file")
        print("csv file must be made in format ANY_FIELD,created_by,ANY_FIELD,ANY_FIELD,user_id")
        print("(for example by https://github.com/matkoniecz/StreetComplete_usage_changeset_analysis#streetcomplete_edits_generate_csv_and_make_quest_summaryphp )")
        return

    # just start it there...
    #os.chdir("~/Desktop/sc_statistics_service_development/sc-statistics-service") # make it more generic

    file_location = sys.argv[1]
    row_count = 0
    # changeset_id,created_by,creation_date,changed_objects,user_id
    with open(file_location) as fp:
        for line in fp:
            if row_count != 0:
                if "StreetComplete" in line.split(",")[1]:
                    print(line)
                    user_id = line.split(",")[-1]
                    print(user_id)
                    command = "php update_users.php " + user_id
                    print(command)
                    os.system(command)
                    #url = "127.0.0.1:8000/get_statistics.php?user_id=" + user_id
                    #response = requests.get(url)
                    #print(response.text)
            row_count += 1

main()