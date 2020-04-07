from locust import HttpLocust,TaskSequence, seq_task

class MyTaskSequence(TaskSequence):

    @seq_task(1)
    def task1(self):

       data1= {'eventName': 'DISMISS_AS_ALREADY_RESPONDED', 'dealerID': 1, 'customerID': 75817245, 'threadID': 14180988,
         'dealerDepartmentID': 1, 'threadUpdatedDate': 'null', 'isThreadDelegated': 'null', 'previousThreadOwnerDAID': 'null',
         'isPreviousOwnerSystemUser': 'null', 'currentThreadOwnerDAID': 'null', 'isCurrentOwnerSystemUser': 'null',
         'lastMessageOn': 'null', 'deviceID': 'null', 'assigneeName': 'null', 'status': 'null', 'eventRaisedBy': 2589}

       headers = {
           'accept': 'application/json',
           'authorization': 'Basic YTgyZjQzOGIzMzc4YmRlYTk4ZDA1ZjhlODA3YThhMDhlYTlhZTI4M2I0NzI5MDE5ZDRhMTEyNGNjNGI5MGNmYjoxNzNhNGU2M2RkMjlkNDkzZjJmZjM0NTdhMDE5ZDY0MjViODdhZmUyM2IxZGE4ZThiMTcxZmNlYTE1MmYxYTEz',
           'Content-Type': 'application/json'
       }

       response = self.client.post("/viewapi/registerthreadevent", json=data1, headers=headers)
       print(response)

    @seq_task(2)
    def task2(self):
        data1 = {'eventName': 'DISMISS_AS_ALREADY_RESPONDED', 'dealerID': 1, 'customerID': 75817487,
                 'threadID': 14181009,
                 'dealerDepartmentID': 1, 'threadUpdatedDate': 'null', 'isThreadDelegated': 'null',
                 'previousThreadOwnerDAID': 'null',
                 'isPreviousOwnerSystemUser': 'null', 'currentThreadOwnerDAID': 'null',
                 'isCurrentOwnerSystemUser': 'null',
                 'lastMessageOn': 'null', 'deviceID': 'null', 'assigneeName': 'null', 'status': 'null',
                 'eventRaisedBy': 2589}

        headers = {
            'accept': 'application/json',
            'authorization': 'Basic YTgyZjQzOGIzMzc4YmRlYTk4ZDA1ZjhlODA3YThhMDhlYTlhZTI4M2I0NzI5MDE5ZDRhMTEyNGNjNGI5MGNmYjoxNzNhNGU2M2RkMjlkNDkzZjJmZjM0NTdhMDE5ZDY0MjViODdhZmUyM2IxZGE4ZThiMTcxZmNlYTE1MmYxYTEz',
            'Content-Type': 'application/json'
        }

        response = self.client.post("/viewapi/registerthreadevent", json=data1, headers=headers)
        print(response)

    @seq_task(3)
    def task3(self):
        data1 = {'dealerID': 1,
                 'filterName': 'RESPONDED_TO',
                 'dealerAssociateID': 2589}

        headers = {
            'accept': 'application/json',
            'authorization': 'Basic YTgyZjQzOGIzMzc4YmRlYTk4ZDA1ZjhlODA3YThhMDhlYTlhZTI4M2I0NzI5MDE5ZDRhMTEyNGNjNGI5MGNmYjoxNzNhNGU2M2RkMjlkNDkzZjJmZjM0NTdhMDE5ZDY0MjViODdhZmUyM2IxZGE4ZThiMTcxZmNlYTE1MmYxYTEz',
            'Content-Type': 'application/json'
        }

        response = self.client.post("/viewapi/getfiltercount", json=data1, headers=headers)
        print(response)

    @seq_task(4)
    def task4(self):
        data1 = {'eventName': 'ADD_TO_WAITING_FOR_RESPONSE', 'dealerID': 1, 'customerID': 75817245,
                 'threadID': 14180988,
                 'dealerDepartmentID': 1, 'threadUpdatedDate': 'null', 'isThreadDelegated': 'null',
                 'previousThreadOwnerDAID': 'null',
                 'isPreviousOwnerSystemUser': 'null', 'currentThreadOwnerDAID': 'null',
                 'isCurrentOwnerSystemUser': 'null',
                 'lastMessageOn': 'null', 'deviceID': 'null', 'assigneeName': 'null', 'status': 'null',
                 'eventRaisedBy': 2589}

        headers = {
            'accept': 'application/json',
            'authorization': 'Basic YTgyZjQzOGIzMzc4YmRlYTk4ZDA1ZjhlODA3YThhMDhlYTlhZTI4M2I0NzI5MDE5ZDRhMTEyNGNjNGI5MGNmYjoxNzNhNGU2M2RkMjlkNDkzZjJmZjM0NTdhMDE5ZDY0MjViODdhZmUyM2IxZGE4ZThiMTcxZmNlYTE1MmYxYTEz',
            'Content-Type': 'application/json'
        }

        response = self.client.post("/viewapi/registerthreadevent", json=data1, headers=headers)
        print(response)

    @seq_task(5)
    def task5(self):
        data1 = {'eventName': 'ADD_TO_WAITING_FOR_RESPONSE', 'dealerID': 1, 'customerID': 75817487,
                 'threadID': 14181009,
                 'dealerDepartmentID': 1, 'threadUpdatedDate': 'null', 'isThreadDelegated': 'null',
                 'previousThreadOwnerDAID': 'null',
                 'isPreviousOwnerSystemUser': 'null', 'currentThreadOwnerDAID': 'null',
                 'isCurrentOwnerSystemUser': 'null',
                 'lastMessageOn': 'null', 'deviceID': 'null', 'assigneeName': 'null', 'status': 'null',
                 'eventRaisedBy': 2589}

        headers = {
            'accept': 'application/json',
            'authorization': 'Basic YTgyZjQzOGIzMzc4YmRlYTk4ZDA1ZjhlODA3YThhMDhlYTlhZTI4M2I0NzI5MDE5ZDRhMTEyNGNjNGI5MGNmYjoxNzNhNGU2M2RkMjlkNDkzZjJmZjM0NTdhMDE5ZDY0MjViODdhZmUyM2IxZGE4ZThiMTcxZmNlYTE1MmYxYTEz',
            'Content-Type': 'application/json'
        }

        response = self.client.post("/viewapi/registerthreadevent", json=data1, headers=headers)
        print(response)

    @seq_task(6)
    def task6(self):
        data1 = {'dealerID': 1,
                 'filterName': 'ACTIVE_MESSAGES',
                 'dealerAssociateID': 2589}

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