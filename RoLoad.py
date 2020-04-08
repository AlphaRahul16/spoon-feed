from locust import Locust, TaskSet, task, HttpLocust
from faker import Faker
import locust.stats
import random
import string
fake = Faker()


class MyTaskSet(TaskSet):

    @task
    def task1(self):
        VIN = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(17))
        rand = fake.ean8()
        Fullname = fake.name()
        Lname = Fullname.split(" ")[1]
        Fname = Fullname.split(" ")[0]
        #Lname ="pip45138";
        #Fname = "america"
        OpenDate = "2020-02-11"
        ron = "StandOrder-{}".format(rand)
        PartNumber = "Part-{}".format(rand)
        status = "OPENED"
        email = "rahuljon@sharklasers.com"
        phoneC = "1231234567"
        custKey = "LoadCK-{}".format(rand)
        #custKey = "america - 45138"
        VehID = "veh-{}".format(rand)
        saId = "rsdms"
        amt = "3.00"
        data = {
            "username": "a82f438b3378bdea98d05f8e807a8a08ea9ae283b4729019d4a1124cc4b90cfb",
            "password": "173a4e63dd29d493f2ff3457a019d6425b87afe23b1da8e8b171fcea152f1a13"
        }
        params = f"open-header-xml=<ServiceSalesOpen xmlns=\"http://www.dmotorworks.com/pip-extract-service-sales-open\"> <ServiceSalesOpen> <AccountingAccount>KR4CERT-A</AccountingAccount> <ActualHours>1.00</ActualHours> <Address>6644 FOX HILLS RD</Address> <ApptDate/> <ApptFlag/> <ApptIDs/> <ApptTime/> <ErrorLevel>0</ErrorLevel> <ErrorMessage/> <EstCompletionDate>2017-05-05</EstCompletionDate> <EstCompletionTime>08:54:00</EstCompletionTime> <MiscSaleCustomerPay>5.00</MiscSaleCustomerPay> <MiscSaleInternal>0.00</MiscSaleInternal> <MiscSaleWarranty>0.00</MiscSaleWarranty> <Model>HHR</Model> <Name1>{Lname},{Fname}</Name1> <Name2/> <OpenDate>{OpenDate}</OpenDate> <OpenedTime>00:00:00</OpenedTime> <OriginalPromiseDate>2017-05-05</OriginalPromiseDate> <OriginalPromiseTime>21:00:00</OriginalPromiseTime> <OriginalWaiterFlag>N</OriginalWaiterFlag> <TransType/> <PromisedDate>2017-05-05</PromisedDate> <PromisedTime>21:00:00</PromisedTime> <ROComment1/> <ROComment2/> <ROComment3/> <ROComment4/> <ROComment5/> <ROComment6/> <ROComment7/> <ROComment8/> <ROComment9/> <ROLubeSaleCP>0.00</ROLubeSaleCP> <ROLubeSaleIP>0.00</ROLubeSaleIP> <ROLubeSaleWP>0.00</ROLubeSaleWP> <ROMiscSaleCP>0.00</ROMiscSaleCP> <ROMiscSaleIP>0.00</ROMiscSaleIP> <ROMiscSaleWP>0.00</ROMiscSaleWP> <RONumber>{ron}</RONumber> <ROSaleCP>119.50</ROSaleCP> <ROSaleIP>0.00</ROSaleIP> <ROSaleWP>0.00</ROSaleWP> <ROStatusCode>C97</ROStatusCode> <ROStatusCodeDesc>{status}</ROStatusCodeDesc> <ROSubletSaleCP>5.00</ROSubletSaleCP> <ROSubletSaleIP>0.00</ROSubletSaleIP> <ROSubletSaleWP>0.00</ROSubletSaleWP> <Remarks/> <Rental/> <Color>BLUE</Color> <ComebackFlag>N</ComebackFlag> <ContactEmailAddress>{email}</ContactEmailAddress> <ContactPhoneNumber>{phoneC}</ContactPhoneNumber> <CustNo>{custKey}</CustNo> <LaborCost>4.00</LaborCost> <LaborSale>82.00</LaborSale> <LaborSaleCustomerPay>82.00</LaborSaleCustomerPay> <LaborSaleInternal>0.00</LaborSaleInternal> <LaborSaleWarranty>0.00</LaborSaleWarranty> <DeliveryDate>2010-07-06</DeliveryDate> <HostItemID>{VehID}*{ron}</HostItemID> <BookedDate>2017-05-05</BookedDate> <CashierNo/> <CityStateZip>VANCOUVER, WA 98665</CityStateZip> <CloseDate>{OpenDate}</CloseDate> <VIN>{VIN}</VIN> <VehID>{VehID}</VehID> <VoidDate/> <WaiterFlag>N</WaiterFlag> <Year>2003</Year> <Service>KR4CERT-S</Service> <ServiceAdvisor>{saId}</ServiceAdvisor> <ShopChargeSaleAmountCP>10.66</ShopChargeSaleAmountCP> <ShopChargeSaleAmountIP>0.00</ShopChargeSaleAmountIP> <ShopChargeSaleAmountWP>0.00</ShopChargeSaleAmountWP> <SoldByDealer/> <SoldHours>1.10</SoldHours> <SourceFile>L</SourceFile> <SpecialCust/> <StateTaxAmountCP>1.84</StateTaxAmountCP> <StateTaxAmountIP/> <StateTaxAmountWP/> <Supp2TaxAmountCP/> <Supp2TaxAmountIP/> <Supp2TaxAmountWP/> <Supp3TaxAmountCP/> <Supp3TaxAmountIP/> <Supp3TaxAmountWP/> <Supp4TaxAmountCP/> <Supp4TaxAmountIP/> <Supp4TaxAmountWP/> <Tag>T205</Tag> <LastServiceDate>2011-07-19</LastServiceDate> <LocalTaxAmountCP/> <LocalTaxAmountIP/> <LocalTaxAmountWP/> <Make>Honda</Make> <Mileage>75000</Mileage> <MileageLastVisit>14416</MileageLastVisit> <MileageOut>75000</MileageOut> <MiscCost>1.00</MiscCost> <MiscSale>5.00</MiscSale> <PartsCost>5.00</PartsCost> <PartsCostCustomerPay>5.00</PartsCostCustomerPay> <PartsCostInternal>0.00</PartsCostInternal> <PartsCostWarranty>0.00</PartsCostWarranty> <PartsSale>20.00</PartsSale> <PartsSaleCustomerPay>20.00</PartsSaleCustomerPay> <PartsSaleInternal>0.00</PartsSaleInternal> <PartsSaleWarranty>0.00</PartsSaleWarranty> <PickItemID>{ron}</PickItemID> <PostedDate/> <PriorityFlag/> <PriorityValue>1018</PriorityValue> <TotalAmountDue>{amt}</TotalAmountDue> </ServiceSalesOpen> </ServiceSalesOpen>&open-detail-xml=<ServiceSalesOpen xmlns=\"http://www.dmotorworks.com/pip-extract-service-sales-open\"> <ServiceSalesDetailsOpen> <ActualHours>0.50</ActualHours> <AddOnFlag>N</AddOnFlag> <ErrorLevel>0</ErrorLevel> <ErrorMessage/> <OpCode>02</OpCode> <OpCodeDescription> CHANGED OIL  FILTER, LUBE CHASSIS, TOP OFF FLUIDS CK TIRE PRESS. </OpCodeDescription> <TechNo2/> <TechNo3/> <TechNo4/> <TechNo5/> <TechNos>9999</TechNos> <RONumber>{ron}</RONumber> <ComeBack>0</ComeBack> <ComplaintCode>02</ComplaintCode> <LaborCost>4.00</LaborCost> <LaborSale>13.00</LaborSale> <LaborType>C</LaborType> <DispatchCode>CS10</DispatchCode> <DispatchEstimatedDuration>0.5</DispatchEstimatedDuration> <DispatchLineCode>A</DispatchLineCode> <DispatchLineStatus>C93</DispatchLineStatus> <HostItemID>{VehID}*{ron}*1*0</HostItemID> <BookerNo>1</BookerNo> <CampaignCode/> <Causes>L.O.F.</Causes> <VehID>{VehID}</VehID> <ServiceRequest> CHANGED OIL  FILTER, LUBE CHASSIS, TOP OFF FLUIDS CK TIRE PRESS. </ServiceRequest> <SoldHours>0.10</SoldHours> <TechNo>9999</TechNo> <LineCode>A</LineCode> <LopSeqNo>1</LopSeqNo> <MiscCost>1.00</MiscCost> <MiscSale>5.00</MiscSale> <PartsCost>5.00</PartsCost> <PartsFlag>1</PartsFlag> <PartsSale>20.00</PartsSale> <PickItemID>{ron}*1</PickItemID> </ServiceSalesDetailsOpen> </ServiceSalesOpen>&dealerid=1"

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = self.client.post("/api/send", params=params, headers=headers, data=data)
        print('Details are: ', Lname, Fname, ron, custKey,response)


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 2000
    max_wait = 5000

