from locust import TaskSet, task, HttpLocust
from faker import Faker
import urllib.request as url
fake = Faker()
import pandas

result = pandas.read_csv('/Users/rahul/Desktop/custGuid.csv')
print(result.shape)

class MyTaskSet(TaskSet):

    @task
    def task1(self):

        department = "ddcf0cd71d42b4c4748151632b37ded667188d52cbfb8b4a9f38a120549b3a1f";
        headers = {
            'accept': 'application/json',
            'authorization': 'Basic Rjk2MEZpdHUzUWxDeXpYaC1wTUNGVlI3SWF2RElwdGVJS0NlUUNTOVdkWTpIMlVhRzVGQUhXZHpGTzRpdkRuSW4weW1rVVhwVjIyQTBzR3RXQW1DeHdV',
            'Content-Type' : 'application/json'
        }

        for i in range(len(result)):
            vehUuid = result.loc[i, "UUID"]
            custUUID = result.loc[i, "GUID"]
            vin = result.loc[i, "VIN"]
            print(vin,custUUID,vehUuid)
            rand = fake.ean8()
            orderNum = "OR"+rand
            status = "PRE-INVOICED"
            advisorNumber = "rahuldms"
            data = {
	           "order": {
                 "header": {
                    "orderNumber": ""+orderNum+"",
                    "serviceAccount": "KEVENT1-S",
                    "accountingAccount": "KEVENT1-A",
                    "dmsStatus": "C97",
                    "status": ""+status+"",
                    "deptType": "KEVENT1-S",
                    "advisorNumber": ""+advisorNumber+"",
                    "advisorName": "",
                    "appointmentNumber": "",
                    "tagNumber": "T859",
                    "mileageIn": 18204,
                    "mileageOut": 18204,
                    "createDate": "2020-04-11",
                    "createTime": "18:35:15",
                    "promisedDate": "2020-04-11",
                    "promisedTime": "21:00:00",
                    "voidDate": "",
                    "closeDate": "",
                    "closeTime": "",
                    "waiter": "N",
                    "rental": "",
                    "soldHours": "0.00",
                    "actualHours": "0.00",
                    "laborCost": "0.00",
                    "laborSale": "150.00",
                    "laborSaleCustomer": "150.00",
                    "laborSaleInternal": "0.00",
                    "laborSaleWarranty": "0.00",
                    "partsCost": "0.00",
                    "partsCostCustomer": "0.00",
                    "partsCostInternal": "0.00",
                    "partsCostWarranty": "0.00",
                    "partsSale": "0.00",
                    "partsSaleCustomer": "0.00",
                    "partsSaleInternal": "0.00",
                    "partsSaleWarranty": "0.00",
                    "lubeSale": "",
                    "lubeSaleCustomer": "0.00",
                    "lubeSaleInternal": "0.00",
                    "lubeSaleWarranty": "0.00",
                    "miscSale": "0.00",
                    "miscSaleCustomer": "0.00",
                    "miscSaleInternal": "0.00",
                    "miscSaleWarranty": "0.00",
                    "subletSale": "",
                    "subletSaleCustomer": "0.00",
                    "subletSaleInternal": "0.00",
                    "subletSaleWarranty": "0.00",
                    "customerPayAmount": "150.00",
                    "customerPayStateTax": "",
                    "internalPayAmount": "0.00",
                    "warrantyPayAmount": "0.00"
                },
                "jobs": [
                    {
                        "jobNumberString": "A",
                        "lopSeqNumber": "1",
                        "laborOpCode": "00",
                        "laborOpCodeDesc": "CLEAN OFF OFF OVERSPRAY ON VEHICLE",
                        "laborType": "C",
                        "laborSale": "150.00",
                        "soldHours": "0.00",
                        "actualHours": "0.00",
                        "partsSale": "0.00",
                        "miscSale": "0.00",
                        "bookerNo": "301",
                        "dispatchLineStatus": "C93",
                        "techNo": "null",
                        "campaignCode": "",
                        "gog": [
                            {
                                "itemType": "",
                                "itemDescription": "",
                                "jobNumber": "131",
                                "quantity": "",
                                "saleTotal": "",
                                "salePrice": "",
                                "laborType": ""
                            }
                        ],
                        "techHours": [
                            {
                                "techNo": "413",
                                "partSeqNo": "",
                                "laborCost": "",
                                "laborSale": "",
                                "soldHours": "",
                                "otherHours": "",
                                "laborType": ""
                            }
                        ],
                        "comments":     [
                                     {
                                      "comment": "test comm"
                                      }
                                         ],
                        "ccc": {
                            "complaint": "THERE IS OVERSPRAY ON THE ENTRIE VEHICLE",
                            "complaintCode": "00",
                            "cause": "",
                            "correction": ""
                        }
                    }
                ],
                "vehicle": {
                	"uuid": ""+vehUuid+"",
                    "vin": ""+vin+""
                },

                "customer": {
                    "uuid": ""+custUUID+""
                }
            }
            }
            print(data)
            response = self.client.put("/order/v2/department/"+department+"/order", json=data, headers=headers)
            print(response.text)


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 3000
    max_wait = 5000