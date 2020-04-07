import requests


headers = {
    'Content-Type': 'text/xml'
}


params  = "<soapenv:Envelope xmlns:soapenv=\"http://www.w3.org/2003/05/soap-envelope\" " \
        "xmlns:tran=\"http://www.starstandards.org/webservices/2005/10/transport\"" \
        "xmlns:wsa=\"http://schemas.xmlsoap.org/ws/2004/08/addressing\"><soapenv:Header><wsse:Security mustUnderstand=\"1\"" \
                                                                                                                        "xmlns:wsse=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd\"" \
                                                                                                                        "xmlns:wsu=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd\">" \
        "<wsse:UsernameToken>" \
        "<wsse:Username>DTk@aryA</wsse:Username>" \
				"<wsse:Password>w34$Rp9</wsse:Password>" \
        "<wsu:Created>2018-10-12T00:00:00Z</wsu:Created>" \
			"</wsse:UsernameToken>" \
		"</wsse:Security>" \
        "</soapenv:Header><soapenv:Body>" \
        "<AppointmentAdd xmlns=\"opentrack.dealertrack.com\">" \
        "<Dealer><EnterpriseCode>ZE</EnterpriseCode><CompanyNumber>ZE7</CompanyNumber><ServerName>arkonap.arkona.com</ServerName>" \
        "</Dealer><Appointment><CompanyNumber>ZE7</CompanyNumber><OpenTransactionDate>20180805</OpenTransactionDate>" \
        "<CustomerKey>1000064</CustomerKey><CustomerName>Test, Marry1171495</CustomerName><CustomerPhoneNumber>3108170196" \
        "</CustomerPhoneNumber><ServiceWriterID>100</ServiceWriterID><TotalEstimate>0.00</TotalEstimate><VIN>1B3BV55K6GG694729</VIN>" \
        "<StockNumber /><Truck>N</Truck><FranchiseCode>NS</FranchiseCode><OdometerIn>1005</OdometerIn><AppointmentDateTime>201908231600</AppointmentDateTime>" \
        "<Details><AppointmentDetail><ServiceLineNumber>1</ServiceLineNumber><LineType>A</LineType><SequenceNumber>0</SequenceNumber>" \
        "<TransDate>20070730</TransDate><Comments>LABOR OP</Comments><ServiceType>MR</ServiceType><LinePaymentMethod>W</LinePaymentMethod>" \
        "<TechnicianID>TEC</TechnicianID><LaborOpCode>LABOR</LaborOpCode><LaborHours>1.50</LaborHours><LaborCostHours>0.00</LaborCostHours>" \
        "<ActualRetailAmount>400.00</ActualRetailAmount></AppointmentDetail></Details></Appointment></AppointmentAdd>" \
        "</soapenv:Body></soapenv:Envelope>"

response = requests.post("https://otstaging.arkona.com/opentrack/serviceapi.asmx", params=params, headers=headers)
print(response)


