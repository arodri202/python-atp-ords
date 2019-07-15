# Copyright (c) 2016, 2018, Oracle and/or its affiliates.  All rights reserved.
import io
import json
import os
import sys

from fdk import response
import requests

sys.path.append(".")
from EmployeeInfo import EmployeeInfo


ORDS_REST_SERVICE_ENDPOINT = os.environ.get("ORDS_REST_SERVICE_ENDPOINT")

def handler(ctx, data: io.BytesIO=None):
    empInfo = None
    try:
        body = json.loads(data.getvalue())
        empInfo = EmployeeInfo(body)

    except (Exception, ValueError) as ex:
        return response.Response(
        ctx, response_data=json.dumps(
            {"error": str(ex)}),
        headers={"Content-Type": "application/json"}
        )


    resp = updateEmployee(empInfo)
    return response.Response(
        ctx, response_data=json.dumps(resp, indent=4),
        headers={"Content-Type": "application/json"}
    )

def updateEmployee(empInfo):
    print("Fetching employee info for " + str(empInfo.getEmpno()), file=sys.stderr)
    queryEndpoint = ORDS_REST_SERVICE_ENDPOINT + "employees/" + str(empInfo.getEmpno());
    print("ORDS query endpoint " + queryEndpoint, file=sys.stderr)

    result = "FAILED to fetch employee info"
    try:
        data = vars(empInfo)
        print("Putting " + str(data) + "in the database", file=sys.stderr)
        result = requests.put(queryEndpoint, json=data).status_code

    except Exception as e:
        result = str(e)

    return result
