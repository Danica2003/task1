from selenium import webdriver
import Constants
import requests


def TestLogIn(email, password):
    body={
        "email":email,
        "password":password
    }

    response = requests.post('https://www.insidemaps.com/property/evoK0wBOkZ/project/HOWbkk8B4y/listing?env=production&projectId=HOWbkk8B4y/api/v1/user/login',data=body)
    if(response.status_code==200):
        print('Good login')
        resBody=response.status_code
        print(resBody)
    else:
        print('Bad login')
        resBody=response.status_code   
        print(response)

TestLogIn("dantonijevic@mail.com","123123")

