from locust import TaskSet, task, HttpLocust
from faker import Faker
import locust.stats
fake = Faker()

# department = "a2783da8f319d3e795adf0f260ba83e9d35a14d4f3e35082082730371a0ff1b1";
# userUuid = "ee3e0146ce4d81377a019c007dda9e6b7d486c2696c54d9c86945c7634f8bf23";
#
# headers = {
#     'accept': 'application/json',
#     'authorization': 'Basic bXBUM3lHNlZ0T2pXYTFLQmN5NzMxaVN4RW9CeVV0Wk1WZUg1RzZIYy1WNDpHdGJhY1ZXS2FEWHJEOVFuSkpiUXlpVzEzckN6a0F5ZGVkOHd3Vm9rUFpj',
#     'Content-Type': 'application/json'
# }

department = "da5e7f64e1751971b6cc46a6b3d6b6f04c6ef3f38d2781ff49b702c0851f5d88";
userUuid = "c0451df44082cc7ee9b71c8eb1300c93bfeee6667307a76bd73c385a509d9ea2";

headers = {
    'accept': 'application/json',
    'authorization': 'Basic cjUxOE0tTzB3S0ZKNVZtT1RkTTV2T1JtSjA0dkFST2UtY0RYMXFESWpKNDo2SEFZbzZ3NzdLUnVXdThoZGwzUFRtTnJReHRuT2lZYkdqQVBpQ1hoNDh3',
    'Content-Type': 'application/json'
}

con = 1

def increment(con):
    con+=1
    return con


class MyTaskSet(TaskSet):
    @task
    def task1(self):
        body = "Load "+fake.ean8()+" Test "+str(increment(con))

        print(body)
        #csvfile = pd.read_csv('custGuid.csv')
        #avList = csvfile['GUID'].values
        #customerGuid= np.random.choice(avList, 1)
        #print(customerGuid[0])'
        customerGuid = "dOcydOQSC40mB1REXrsgfHT5_bA8S_2TYlMB-27gChE"


        data ={
            "messageAttributes": {
               "body": body,
                "draftAttributes": {
                    "draftStatus": "SCHEDULED"
                },
               "isManual": "False",
               "protocol": "TEXT",
               "type": "DRAFT"
            },
            "messageSendingAttributes": {
              "addFooter": "true",
              "addSignature": "true",
              "addTCPAFooter": "false",
              "overrideHolidays": "true",
              "overrideOptoutRules": "false"

            }
        }
        response = self.client.post("/department/"+department+"/user/"+userUuid+"/customer/"+customerGuid+"/message",json=data, headers=headers)
        print(response.text)

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000