from test1 import random_date
import urllib.request as ur
from locust import TaskSet, task, HttpLocust
import random

department = "a2783da8f319d3e795adf0f260ba83e9d35a14d4f3e35082082730371a0ff1b1";
headers = {
    'accept': 'application/json',
    'authorization': 'Basic Rjk2MEZpdHUzUWxDeXpYaC1wTUNGVlI3SWF2RElwdGVJS0NlUUNTOVdkWTpIMlVhRzVGQUhXZHpGTzRpdkRuSW4weW1rVVhwVjIyQTBzR3RXQW1DeHdV',
    'Content-Type': 'application/json'
}

size = [0,1,2,3,4,5,9,12,16,19,30,35,40,50]
pageNo = [1,2,3,4,5,6,7,8,9]
orderNumberPrefix = ["test","rahul","order","noida","pip"]

class MyTaskSet(TaskSet):

    @task
    def task1(self):

        data = {'orderNumberPrefix': random.choice(orderNumberPrefix)}

        print(data)
        response = self.client.post("/department/"+department+"/order/specificSearch", json=data, headers=headers)
        print(response)

    @task
    def task2(self):

        data = {'orderNumberPrefix': random.choice(orderNumberPrefix),
                'pageNo': random.choice(pageNo),
                'size': random.choice(size)}
        print(data)
        response = self.client.post("/department/"+department+"/order/specificSearch", json=data, headers=headers)
        print(response)

    @task
    def task3(self):

        data = {'vin': ur.urlopen("http://randomvin.com/getvin.php?type=real").read().decode('utf-8'),
                'pageNo': random.choice(pageNo),
                'size': random.choice(size)}
        print(data)
        response = self.client.post("/department/"+department+"/order/specificSearch", json=data, headers=headers)
        print(response)

    @task
    def task4(self):

        data = {'toOrderDate': random_date("2018-1-1", "2019-11-28", random.random()),
                'fromOrderDate': random_date("2018-1-1", "2019-11-28", random.random())
                }
        print(data)
        response = self.client.post("/department/"+department+"/order/specificSearch", json=data, headers=headers)
        print(response)

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000


