import requests
import datetime

'''
Fiscal Device Gateway API can be accessed using HTTPS protocol only. 
All Fiscal Device Gateway API methods except registerDevice and getServerCertificate use CLIENT AUTHENTICATION CERTIFICATE
which is issued by FDMS.
'''



class Device:
    def __init__(self, test_mode=False, *args):
        self.args = args
        if test_mode:
            self.base_url = 'https://fdmsapitest.zimra.co.zw/Device/'
        else:
            self.base_url = 'https://fdmsapi.zimra.co.zw/Device/'

        self.deviceBaseUrl = f'{self.base_url}{self.deviceID}'


        self.operationID = None #set by getConfig(), 
        self.fiscalDayNo = None #set by openDay()
        self.fiscalDayOpened = None
        self.taxPayerName = None
        self.taxPayerTIN = None
        self.vatNumber = None
        self.deviceSerialNo = None
        self.deviceBranchName = None
        self.deviceBranchAddress = None
        self.deviceBranchContacts = None
        self.deviceOperatingMode = None
        self.taxPayerDayMaxHrs = None
        self.applicableTaxes = None
        self.certificate = None
        self.certificateValidTill = None
        self.qrUrl = None
        self.serialNo = None
        self.taxpayerDayEndNotificationHrs = None
        self.deviceID = None
        self.activationKey = None


    def register(self):
        pass

    def verifyTaxpayerInformation(self):
        url = f'{self.deviceBaseUrl}/VerifyTaxpayerInformation'
        pass

    def getConfig(self):
        '''Uses self.deviceID to get the device configuration
        and updates the self attributes with the response data
        ''' 
        url = f'{self.deviceBaseUrl}/GetConfig'
        response = requests.get(url, headers={'accept': 'application/json'})
        
        if response.status_code == 200:
            data = response.json()
            
            self.operationID = data.get('operationID') # only the pressing operations
            self.taxPayerName = data.get('taxPayerName')
            self.taxPayerTIN = data.get('taxPayerTIN')
            self.vatNumber = data.get('vatNumber')
            self.deviceSerialNo = data.get('deviceSerialNo')
            self.deviceBranchName = data.get('deviceBranchName')
            self.deviceBranchAddress = data.get('deviceBranchAddress')
            self.deviceBranchContacts = data.get('deviceBranchContacts')
            self.deviceOperatingMode = data.get('deviceOperatingMode')
            self.taxPayerDayMaxHrs = data.get('taxPayerDayMaxHrs')
            self.applicableTaxes = data.get('applicableTaxes')
            self.certificateValidTill = data.get('certificateValidTill')
            self.qrUrl = data.get('qrUrl')
            self.taxpayerDayEndNotificationHrs = data.get('taxpayerDayEndNotificationHrs')
            return 'Device configuration updated'
        else:
            return(f"Error: {response.status_code} - {response.text}")

    def issueCertificate(self):
        '''uses self.deviceID and self.certificate'''
        url = f'{self.deviceBaseUrl}/IssueCertificate'
        headers = {
            'DeviceModelName': self.deviceModelName,
            'DeviceModelVersion': self.deviceModelVersion,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.post(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            self.certificate = data.get('certificate', None)
            return 'Certificate issued'
        else:
            print(f"Failed to issue certificate. Status code: {response.status_code}")
            print(response.text)

    def getStatus(self):
        '''returns a dictionary with the following example data:
        {
            "operationID": "0HMPH8CBL0I62:00000001",
            "fiscalDayStatus": "FiscalDayClosed",
            "fiscalDayReconciliationMode": "Auto",
            "fiscalDayServerSignature": {
                "certificateThumbprint": "b785a0b4d8a734a55ba595d143b4cf72834cd88d",
                "hash": "//To59fLHvuoRe2slUpN2grJu5adaodOW6kW1OYvf/c=",
                "signature": "YyXTSizBBrMjMk4VQL+sCNr+2AC6aQbDAn9JMV2rk3yJ6MDZwie0wqQW3oisNWrMkeZsuAyFSnFkU2A+pKm91sOHVdjeRBebjQgAQQIMTCVIcYrx+BizQ7Ib9iCdsVI+Jel2nThqQiQzfRef6EgtgsaIAN+PV55xSrHvPkIe+Bc="
            },
            "fiscalDayClosed": "2023-03-30T20:15:40",
            "lastFiscalDayNo": 101,
            "lastReceiptGlobalNo": 9931
        }'''
        url = f'{self.deviceBaseUrl}/GetStatus'
        response = requests.get(url, headers={'accept': 'application/json'})

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return(f"Error: {response.status_code} - {response.text}")

    def openDay(self, fiscalDayNo: int, fiscalDayOpened=None)->dict:
        '''if successful, updates the fiscalDayNo with the response data and returns the following example data:
        {
        "operationID": "0HMPH9AF0QKKE:00000005",
        "fiscalDayNo": 102
        }'''
        if fiscalDayOpened is None:
            fiscalDayOpened = datetime.datetime.now().isoformat()
            
        url = f'{self.deviceBaseUrl}/OpenFiscalDay'
        headers = {
            'DeviceModelName': self.deviceModelName,
            'DeviceModelVersion': self.deviceModelVersion,
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        payload = {
            "fiscalDayNo": fiscalDayNo,
            "fiscalDayOpened": fiscalDayOpened
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  # Will raise an HTTPError for bad responses
            data = response.json()
            
            # Update attributes with response data
            self.fiscalDayNo = data.get("fiscalDayNo")

            return data

        except requests.exceptions.RequestException as e:
            print(f"HTTP request failed: {e}")
        except ValueError:
            print("Invalid JSON response")

    def submitReceipt(self, receiptData):
        '''uses self.deviceID and receipt data to submit receipt'''
        url = f'{self.deviceBaseUrl}/SubmitReceipt'
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        if hasattr(self, 'deviceModelName'):
            headers['DeviceModelName'] = self.deviceModelName
        
        if hasattr(self, 'deviceModelVersion'):
            headers['DeviceModelVersion'] = self.deviceModelVersion

        payload = {
            "receipt": {
                "receiptType": receiptData["receiptType"],
                "receiptCurrency": receiptData["receiptCurrency"],
                "receiptCounter": receiptData["receiptCounter"],
                "receiptGlobalNo": receiptData["receiptGlobalNo"],
                "invoiceNo": receiptData["invoiceNo"],
                "buyerData": receiptData["buyerData"],
                "receiptNotes": receiptData["receiptNotes"],
                "receiptDate": receiptData["receiptDate"],
                "creditDebitNote": receiptData["creditDebitNote"],
                "receiptLinesTaxInclusive": receiptData["receiptLinesTaxInclusive"],
                "receiptLines": receiptData["receiptLines"],
                "receiptTaxes": receiptData["receiptTaxes"],
                "receiptPayments": receiptData["receiptPayments"],
                "receiptTotal": receiptData["receiptTotal"],
                "receiptPrintForm": receiptData["receiptPrintForm"],
                "receiptDeviceSignature": receiptData["receiptDeviceSignature"]
            }
        }
        
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return response.text

    def closeDay(self):
        '''Uses self.deviceID to close the fiscal day'''
        url = f'{self.deviceBaseUrl}/CloseFiscalDay'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        if hasattr(self, 'deviceModelName'):
            headers['DeviceModelName'] = self.deviceModelName
        
        if hasattr(self, 'deviceModelVersion'):
            headers['DeviceModelVersion'] = self.deviceModelVersion

        try:
            response = requests.post(url, headers=headers)
            response.raise_for_status() 
            data = response.json()
            
            return data

        except requests.exceptions.RequestException as e:
            return f"HTTP request failed: {e}"
        except ValueError:
            return f"Invalid JSON response"