import requests

response = requests.get("https://www.delftstack.com/howto/python/python-get-json-from-url/")

print(response)
print(response.text)

row_count = 0
# changeset_id,created_by,creation_date,changed_objects,user_id
with open('edits_with_all_declared_software.csv') as fp:
    for line in fp:
        if row_count != 0:
            if "StreetComplete" in line.split(",")[1]:
                print(line)
                print(line.split(",")[-1])
        row_count += 1