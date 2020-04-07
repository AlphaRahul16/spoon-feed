
from locust import HttpLocust,TaskSequence, seq_task

class MyTaskSequence(TaskSequence):

    @seq_task(1)
    def task6(self):
        data1 = {'dealerID': 54,
                 'filterName': 'INBOX',
                 'dealerAssociateID': 11836}

        headers = {
            'accept': 'application/json',
            'authorization': 'Basic YTgyZjQzOGIzMzc4YmRlYTk4ZDA1ZjhlODA3YThhMDhlYTlhZTI4M2I0NzI5MDE5ZDRhMTEyNGNjNGI5MGNmYjoxNzNhNGU2M2RkMjlkNDkzZjJmZjM0NTdhMDE5ZDY0MjViODdhZmUyM2IxZGE4ZThiMTcxZmNlYTE1MmYxYTEz',
            'Content-Type': 'application/json'
        }

        response = self.client.post("/viewapi/getfiltercount", json=data1, headers=headers)
        print(response)



class MyLocust(HttpLocust):
    task_set = MyTaskSequence
    min_wait = 1000
    max_wait = 3000