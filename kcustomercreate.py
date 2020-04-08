from locust import TaskSet, task, HttpLocust
from faker import Faker
import urllib.request as url
fake = Faker()

class MyTaskSet(TaskSet):

    @task
    def task1(self):

        department = "ddcf0cd71d42b4c4748151632b37ded667188d52cbfb8b4a9f38a120549b3a1f";
        headers = {
            'accept': 'application/json',
            'authorization': 'Basic Rjk2MEZpdHUzUWxDeXpYaC1wTUNGVlI3SWF2RElwdGVJS0NlUUNTOVdkWTpIMlVhRzVGQUhXZHpGTzRpdkRuSW4weW1rVVhwVjIyQTBzR3RXQW1DeHdV',
            'Content-Type' : 'application/json'
        }

        vin = url.urlopen("http://randomvin.com/getvin.php?type=real").read().decode('utf-8')
        rand = fake.ean8()
        Fullname = fake.name()
        Lname = Fullname.split(" ")[1]
        Fname = Fullname.split(" ")[0]
        customerkey = "CO"+rand
        vehkey = "VO"+rand


        data = {
  'customer': {
    'company': 'Mykaarma',
    'customerKey': ""+customerkey+"",
    'emails': [
      {
        'emailAddress': 'rahulqa02@sharklasers.com',
        'isPreferred': 'true',
        'label': 'home',
        'okToEmail': 'true'
      }
    ],
    'firstName': ""+Fname+"",
    'lastName': ""+Lname+"",
    'phoneNumbers': [
      {
        'isPreferred': 'true',
        'label': 'cell',
        'okToCall': 'true',
        'okToText': 'true',
        'phoneNumber': '+12073521046'
      }
    ],
    'preferredCommunication': 'phone'
  },

  'validateVin': 'true',
  'vehicles': [
    {

      'vehicleKey': ""+vehkey+"",
      'vin': ""+vin+""
    }
  ]
}
        print(data)
        response = self.client.post("/customer/v2/department/"+department+"/customer", json=data, headers=headers)
        print(response.text)

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 3000
    max_wait = 5000