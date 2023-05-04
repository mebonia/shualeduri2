import sqlite3

conn = sqlite3.connect('survey.sqlite')

cur = conn.cursor()


cur.execute("SELECT COUNT(*) FROM Students WHERE SelfStudyHour < 2")
numstudents = cur.fetchone()[0]
print(f"{numstudents} მოსწავლე სწავლობს 2 საათზე ნაკლებს.")





def mosw_raoden(device, age):

    cur.execute("SELECT COUNT(*) FROM Students WHERE Device = ? AND Age = ?", (device, age))
    result = cur.fetchone()[0]
    return result

count = mosw_raoden('Smartphone', 20)
print(count,' მოსწავლე იყენებს smartphone -ს ლექციისთვის რომელთა  ასაკი უდრის 20-ს')




cur.execute("INSERT INTO Students (ID, Age, OnlineClassTime, Device, SelfStudyHour, FitnessTime, Sleep, SocialMedia, SocialMediaPlatform) VALUES (?,?,?,?,?,?,?,?,?)",
               (504, 17, 3, 'Laptop', 1, 0, 8, 1, 'Youtube'))




cur.execute("UPDATE Students SET Device = 'alex' WHERE Age != 21")



conn.commit()
conn.close()


#N2
import json

with open('sample.json', 'r') as f:
    data = json.load(f)

print(data)

print('მისამართი:',data['person']['address'])



friends = data['person']['friends']
friend_names = []
for friend in friends:
    name_parts = friend['name']
    friend_names.append(name_parts)
print(friend_names)

with open('sample.json') as f:
    user_data = json.load(f)['person']

selected_field = input('Enter field name: ')

if selected_field in user_data:
    print(user_data[selected_field])
else:
    print('Field not found')




