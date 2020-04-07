from locust import TaskSet, task, HttpLocust

class MyTaskSet(TaskSet):

    @task
    def task1(self):

        department = "a2783da8f319d3e795adf0f260ba83e9d35a14d4f3e35082082730371a0ff1b1";
        headers = {
            'accept': 'application/json',
            'authorization': 'Basic YTgyZjQzOGIzMzc4YmRlYTk4ZDA1ZjhlODA3YThhMDhlYTlhZTI4M2I0NzI5MDE5ZDRhMTEyNGNjNGI5MGNmYjoxNzNhNGU2M2RkMjlkNDkzZjJmZjM0NTdhMDE5ZDY0MjViODdhZmUyM2IxZGE4ZThiMTcxZmNlYTE1MmYxYTEz',
            'Content-Type' : 'application/json'
        }

        data = {'dealerAssociateUuid': '7f07954f746869e84591cec98006800a4f70a3d01864f4fe0e6dd2004d6fa7fa',
                'fromOpenDate': '2019-10-14',
                'pageNo': '0',
                'size': '1',
                'sortOrder': 'ASC',
                'sortableField': 'SPECIAL_ORDER_NUMBER',
                'toOpenDate': '2019-10-15'}

        response = self.client.post("/department/"+department+"/specialOrder/index", json=data, headers=headers)
        print(response)

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000