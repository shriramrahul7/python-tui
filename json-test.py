import requests
import json

# data = {
#     'name': 'Shriram Rahul', 
#     'age' : 20, 
#     'designation': 'student',
#     'favourite-animes': [
#         'Naruto', 'JJba', 'DeathNote', 'Kaguya-Sama'
#     ]
# }

response = requests.get("https://type.fit/api/quotes")
print(response)