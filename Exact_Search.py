from locust import Locust, TaskSet, task, HttpLocust

headers = {
    'accept': 'application/json',
    'authorization': 'Basic YTgyZjQzOGIzMzc4YmRlYTk4ZDA1ZjhlODA3YThhMDhlYTlhZTI4M2I0NzI5MDE5ZDRhMTEyNGNjNGI5MGNmYjoxNzNhNGU2M2RkMjlkNDkzZjJmZjM0NTdhMDE5ZDY0MjViODdhZmUyM2IxZGE4ZThiMTcxZmNlYTE1MmYxYTEz',
    'Content-Type': 'application/json'
}
class MyTaskSet(TaskSet):


    @task
    def task1(self):

        data = {'dealerUUIDList': [ "7e9530895e5bd2d079facc91eb359bfcaf071f71a42e1d37b8fd43167f109770"],
            "includeDealerOrderInfo": "true",
            "orderType": "SERVICE",
            "queryOperator": "AND",
            "searchMap": {"VIN_EXACT": [ "1HGCM82633A004352"]
            }
                }
        response = self.client.post("/customer/list/exact", json=data, headers=headers)
        print(response)

    @task
    def task2(self):
        data = {'dealerUUIDList': [ "7e9530895e5bd2d079facc91eb359bfcaf071f71a42e1d37b8fd43167f109770"],
            "includeDealerOrderInfo": "true",
            "orderType": "SERVICE",
            "queryOperator": "AND",
            "searchMap": {"COMMUNICATIONVALUE_EXACT": [ "9257264358"]
            }
                }
        response = self.client.post("/customer/list/exact", json=data, headers=headers)
        print(response)

    @task
    def task3(self):
        data = {'dealerUUIDList': [ "7e9530895e5bd2d079facc91eb359bfcaf071f71a42e1d37b8fd43167f109770"],
            "includeDealerOrderInfo": "true",
            "orderType": "SERVICE",
            "queryOperator": "AND",
            "searchMap": {"COMMUNICATIONVALUE_EXACT": [ "tdtpjyvd@sharklasers.com"]
            }
                }
        response = self.client.post("/customer/list/exact", json=data, headers=headers)
        print(response)

    @task
    def task4(self):
        data = {'dealerUUIDList': [ "7e9530895e5bd2d079facc91eb359bfcaf071f71a42e1d37b8fd43167f109770"],
            "includeDealerOrderInfo": "true",
            "orderType": "SERVICE",
            "queryOperator": "AND",
            "searchMap": {"VIN_EXACT": [ "KNDJT2A55D7597080"]
            }
                }
        response = self.client.post("/customer/list/exact", json=data, headers=headers)
        print(response)


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 2000
    max_wait = 5000