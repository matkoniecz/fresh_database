#import requests
import sys
import os
import time

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
                    fetch_info_about_user(user_id)

def fetch_info_about_user(user_id):
    attempt = 1
    while(True):
        print(user_id)
        command = "php update_users.php " + str(user_id)
        print(command)
        status = os.system(command)
        if os.WIFEXITED(status) and os.WEXITSTATUS(status) == 0:
            return
        else:
            print(os.WIFEXITED(status))
            print(os.WEXITSTATUS(status))
            print("user update failed! Will retry!")
            print("please check whether config.php of statistics script contains login data - logged in users are allowed much higher quota")
            print("it was attempt", attempt)
            time.sleep(100)
            print("sleeping ended")
            print("--------------------------------")
            print()
            print()
            attempt += 1

    #calling API - note that it is running only a partial update
    #url = "127.0.0.1:8000/get_statistics.php?user_id=" + user_id
    #response = requests.get(url)
    #print(response.text)
print("""
Is there an API to detect deleted users?

See https://www.openstreetmap.org/api/0.6/user/4909211 vs https://api.openstreetmap.org/api/0.6/user/1722488

I can just assume that empty XML indicates deletion of user but sooner or later I will receive truncated/damaged/garbled response and misclassify such user as deleted

I only discovered what is going on by visiting https://resultmaps.neis-one.org/osm-discussion-comments?uid=4909211

See also https://github.com/streetcomplete/sc-statistics-service/issues/22
""")

fetch_info_about_user(4909211)
main()
