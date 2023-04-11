print(user1.get("email"))
print(users.get("luukasz"))
print(users.get("luukasz", "invalid username"))
print(users["lukasz"])
print(users["admin"])
#print(users["aadmin"])username = "aadmin"if username in users.keys():
    print(users[username])
	
users["alice"] = "alice@gmail.com"print(users)
users["alice"] = "alice2@gmail.com"print(users)
for e in users:
    print(e)
for e in users.keys():
    print(e)
for e in users.values():
    print(e)
print(users.items())
for key, value in users.items():
    print("key is " + str(key) +" values "+ str(value))
user1.update({"password": "haslo"})
print(user1)
if "passwoooooord" in user1:
    del user1["passwoooooord"]
if "password" in user1:
    del user1["password"]
print(user1)
user1.update({"password": "haslo"})
print(user1)
print(user1.pop("password"))
print(user1)
sorted_dict={}
for key in sorted(users):
    value = users[key]
    sorted_dict[key] = valueprint(sorted_dict)
users = {"lukasz": 75,
         "joe": 60,
         "test": 80,
         "admin": 99}
def get_value(item):
    return item[1]
sorted_value = sorted(users.items(), key=get_value)
sorted_value = dict(sorted_value)
print(sorted_value)
dict_list = []
dict_list.append(user1)
dict_list.append(user2)
dict_list.append(user3)
dict_list.append(user4)
print(dict_list)
print(len(dict_list))
print(len(user1))
for i in range(0,len(dict_list)):
    dict_list[i]["password"] = "afgaGSDFHG"dict_list.append({"name": "alice", "email": "alice@email.com"})
for i in range(0,len(dict_list)):
    if "password" not in dict_list[i]:
        dict_list[i]["password"] = "nowe"print(dict_list)
for i in range(0,len(dict_list)):
    dict_list[i]["adresy"] = ["koszykowa 86", "akademicka 9"]
print(dict_list)
for i in range(0,len(dict_list)):
    dict_list[i]["adresy"] = {"adres_zamieszkania": "koszykowa 86", "adres_kor": "akademicka 9"}
print(dict_list)
filename = "students.txt"with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
students = ["alice", "bob"]
filename = "studentsOut.txt"with open(filename,"w") as file_object:
    for e in students:
        line = f" Witaj {e}\n"        file_object.write(line)
def send_email(subject, body, sender, recipients, password):
 msg = MIMEText(body)
 msg['Subject'] = subject msg['From'] = sender msg['To'] = ', '.join(recipients)
 print(msg)
 smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
 smtp_server.login(sender, password)
 smtp_server.sendmail(sender, recipients, msg.as_string())
 smtp_server.quit()
subject = "Email wysłany z Python'a"body = "To jest wiadomość wysłana za pomocą SMTP"sender = "test@gmail.com"recipients = ["test2@gmail.com"]
password = "haslo app gmaila"send_email(subject, body, sender, recipients, password)
    
    
      Expand (130 lines)
      Collapse
    
  
  
