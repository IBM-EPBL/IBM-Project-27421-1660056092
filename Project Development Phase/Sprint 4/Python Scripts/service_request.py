
import time
import numpy as np

from ibmcloudant.cloudant_v1 import CloudantV1
from ibmcloudant import CouchDbSessionAuthenticator
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

authenticator = BasicAuthenticator('apikey-v2-2vji5kegi5d7aaygtccqtt616y5u2yva2mpawe7ps7gp','15bc42554c2a4881a11889247e6ab66e')
                                                                                             
service = CloudantV1(authenticator=authenticator)
print(service)
service.set_service_url('https://apikey-v2-2vji5kegi5d7aaygtccqtt616y5u2yva2mpawe7ps7gp:15bc42554c2a4881a11889247e6ab66e@58980990-cf73-48b6-bbee-db90262aae86-bluemix.cloudantnosqldb.appdomain.cloud')
current_requests=0
def print_requests():
    try:
        response = service.post_all_docs(
            db='service-request',
            ).get_result()
        global current_requests;
        current_requests=response["total_rows"]
        print("Number of unresolved requests:"+str(current_requests))
        print("Live Service Requests")
        print("---------------------")
        print("PNR\t\t Requests")
        for row in response["rows"]:
            row_response = service.get_document(
            db='service-request',
            doc_id=row["id"]
            ).get_result()
            s=str(row_response["pnr"])
            key=row_response.keys()
            k=[x for x in key if row_response[x]==True]
            for val in k:
                s+="\t "+val
            print(s)

    except Exception as e :
        print(e)
        time.sleep(5)

print_requests()
while True:
    time.sleep(30)
    if current_requests<service.post_all_docs(
        db='service-request',
        ).get_result()["total_rows"]:
        print_requests()


