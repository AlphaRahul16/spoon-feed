from locust import Locust, TaskSet, task, HttpLocust
import json

headers = {
    'accept': 'application/json',
    'authorization': 'Basic Rjk2MEZpdHUzUWxDeXpYaC1wTUNGVlI3SWF2RElwdGVJS0NlUUNTOVdkWTpIMlVhRzVGQUhXZHpGTzRpdkRuSW4weW1rVVhwVjIyQTBzR3RXQW1DeHdV',
    'Content-Type': 'application/json'
}

dealeruuid = "7e9530895e5bd2d079facc91eb359bfcaf071f71a42e1d37b8fd43167f109770"
deptuuid = "d4e4d379f36a9ba41ed3b607f5a76a0815bf3586fad5d5c8bbaea197e6b418a9"
phone = "2073521046"
class MyTaskSet(TaskSet):


    @task
    def task1(self):
        response = self.client.get("/dealer/"+dealeruuid+"/department/"+deptuuid+"/commType/TEXT/commValue/"+phone+"/status", headers=headers)
        json_response = json.loads(response.text)
        print(json_response['optoutStatus'])



class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 2000
    max_wait = 5000