from urllib.request import urlopen
import json
import csv


def getRows(data, target):
    rows = []
    for i in data:
        if target == data:
            rows.append([i, data[i]])
        if target == users:
            rows.append([i, data[i]])
        if target == names:
            rows.append([i, data[i]])
        if target == text:
            rows.append([i, data[i]])
        if str(target) == str(history):
            rows.append([i, data[i]['accounts_age'], data[i]['daily_faves'], data[i]['daily_posts']])
        if target == ratios:
            rows.append([i, data[i]['friends_per_follows']])
        elif target not in options:
            print("Incorrect target request.  Target =", target, "Exiting...")
            exit()

    return rows


def to_csv(data, target):
    if target == history:
        csv_data = 'history.csv'
    if target == ratios:
        csv_data = 'ratios.csv'
    elif target != history and target != ratios:
        csv_data = "data.csv"
    with open(csv_data,'w') as outf:
        outcsv = csv.writer(outf)
        outcsv.writerows(getRows(data, target))


def main():


    """ Un-Comment this section and choose an option to pull data into a csv """
    # target = <YourTargetOption>
    # req = urlopen(str(local+target))
    # json = json.loads(req.read())
    # to_csv(json, target)

    """ The following sections pull data for user history and friend/follower ratios"""
    targetH = history
    reqH = urlopen(str(local+targetH))
    jsonH = json.loads(reqH.read())
    to_csv(jsonH, targetH)

    targetR = ratios
    reqR = urlopen(str(local+targetR))
    jsonR = json.loads(reqR.read())
    to_csv(jsonR, targetR)


# Global
data = "/tweets/data"
users = "/users"
names = "/users/names"
text = "/tweets/text"
history = "/tweets/userhistory"
ratios = "/tweets/ratios"

options = [data, users, names, text, history, ratios]

local = "http://localhost:5000"

if __name__ == '__main__':
    main()
