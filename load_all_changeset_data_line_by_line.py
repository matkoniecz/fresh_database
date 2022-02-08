#import requests
import sys
import os


"""
script that loads file listing changesets and based on that
requests SC statistics database to fetch data about SC mappers

Tested on Lubuntu 20.04. Unix is supported, Windows not.
"""

def main():
    # changeset data can be obtained with https://github.com/matkoniecz/StreetComplete_usage_changeset_analysis#streetcomplete_edits_generate_csv_and_make_quest_summaryphp

    if len(sys.argv) != 2:
        print("call it with a single arguments specifying location of a csv file")
        print("csv file must be made in format changeset_id,created_by,ANY_FIELD,ANY_FIELD,user_id")
        print("(for example by https://github.com/matkoniecz/StreetComplete_usage_changeset_analysis#streetcomplete_edits_generate_csv_and_make_quest_summaryphp )")
        return

    # just start it there...
    #os.chdir("~/Desktop/sc_statistics_service_development/sc-statistics-service") # make it more generic

    procesed_users = set()
    users_with_sc_edits_with_lower_than_this_are_processed = 1 # allows quick restart of script after processing part of data
    file_location = sys.argv[1]
    # changeset_id,created_by,creation_date,changed_objects,user_id
    with open(file_location) as fp:
        next(fp) # skip header
        for line in fp:
            editor = line.split(",")[1]
            if "StreetComplete" in editor or "Zażółć" in editor or "Zazolc" in editor:
                user_id = int(line.split(",")[-1])
                if int(line.split(",")[0]) < users_with_sc_edits_with_lower_than_this_are_processed:
                    if user_id not in procesed_users:
                        # it is not necessary to process the same user multiple times
                        # on repeated reruns of the script
                        procesed_users.add(user_id)
                    continue
                if user_id not in procesed_users:
                    procesed_users.add(user_id)
                    print(line)
                    print(user_id)
                    command = "php update_users.php " + user_id
                    print(command)
                    os.system(command)
                    #url = "127.0.0.1:8000/get_statistics.php?user_id=" + user_id
                    #response = requests.get(url)
                    #print(response.text)

main()
