from locust import between, task, HttpUser

class MyLocust(HttpUser):
    @task
    def task1(self):
       data1 = {"dealerID":1,"dealerAssociateID":2589,"filterName":"INBOX","pageNo":1,"itemCount":10,"lastMessageReceivedDate":'null','listOfMessageIdsReceivedAtSameTime':'null','dealerDepartmentID':1,'customerID':'null','additionalFilters':{}}

       headers = {
           'accept': 'application/json',
           'authorization': 'Basic YTgyZjQzOGIzMzc4YmRlYTk4ZDA1ZjhlODA3YThhMDhlYTlhZTI4M2I0NzI5MDE5ZDRhMTEyNGNjNGI5MGNmYjoxNzNhNGU2M2RkMjlkNDkzZjJmZjM0NTdhMDE5ZDY0MjViODdhZmUyM2IxZGE4ZThiMTcxZmNlYTE1MmYxYTEz',
           'Content-Type': 'application/json'
       }

       response = self.client.post("/viewapi/getfiltercount", json=data1, headers=headers)
       print(response)

    wait_time = between(1, 3)