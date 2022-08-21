print("Welcome to Christ University\n",
    "\n",
    "*   Establishment on 15 July 1969\n",
    "*   UGC Approved\n",
    "\n",
    "Our Vision:\n",
    "\n",
    "\n",
    "\n",
    "CHRIST (Deemed to be University), a premier educational institution, is an academic fraternity of individuals dedicated to the motto of 'EXCELLENCE AND SERVICE.'\n",
    "\n",
    "Our Mission:\n",
    "\"CHRIST (Deemed to be University) is a nurturing ground for an individual's holistic development to make an effective contribution to the society in a dynamic environment.\"\n",
    "\n",
    "Core Values:\n",
    "\n",
    "\n",
    "*   Faith in God\n",
    "*   Moral Uprightness\n",
    "*   Love of Fellow Beings\n",
    "*   Social Responsibility\n",
    "*   Pursuit of Excellence bold text\n \n \n"
      "The following are the different english courses in Christ University:-\n"
    "101:Bachelor of Arts Liberal Arts ( Bangalore Bannerghatta Road Campus)\n"
    "312:Bachelor of Arts (BA) Communication and Media, English and Psychology.\n"
    "134:Bachelor of Arts Journalism, Psychology, English.\n"
    "524:Bachelor of Arts Psychology, Sociology, English.\n"
    "176:Bachelor of Arts Performing Arts, English, Psychology\n\n")

student=input("Please type your name=")
age=int(input("Please type your age="))
Email=input("Please type your email ID=")

class_list = dict()
data = input(' University_code(3 digit code),Course,& Campus_name : ')
temp = data.split(':')
class_list[int(temp[0])] = [(temp[1]), (temp[2])]

# Displaying the dictionary
for key, value in class_list.items():
    print('University_code: {}, Course,& Campus_name: {}'.format(key, value))
