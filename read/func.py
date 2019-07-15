# Copyright (c) 2016, 2018, Oracle and/or its affiliates.  All rights reserved.
import io
import json
import os
import sys

from fdk import response
import requests


ORDS_REST_SERVICE_ENDPOINT = os.environ.get("ORDS_REST_SERVICE_ENDPOINT")

def handler(ctx, data: io.BytesIO=None):
    empID = ""
    try:
        body = json.loads(data.getvalue())
        empID = str(body.get("empno"))
    except Exception as ex:
        print(str(ex), file=sys.stderr)

    resp = fetchEmployee(empID)
    return response.Response(
        ctx, response_data=json.dumps(resp, indent=4),
        headers={"Content-Type": "application/json"}
    )

def fetchEmployee(empID):
    queryEndpoint = None
    result = "FAILED to fetch employee info"
    try:
        if empID == "":
            print("Getting all employees...", file=sys.stderr)
            queryEndpoint = ORDS_REST_SERVICE_ENDPOINT + "employees"
        else:
            print("Fetching employee info for " + empID, file=sys.stderr)
            queryEndpoint = ORDS_REST_SERVICE_ENDPOINT + "employees/" + empID;

        print("ORDS query endpoint " + queryEndpoint, file=sys.stderr)

        employeeInfo = requests.get(queryEndpoint)
        print("Got result", file=sys.stderr)
        result = employeeInfo.json()

    except Exception as e:
        result = str(e)

    return result
