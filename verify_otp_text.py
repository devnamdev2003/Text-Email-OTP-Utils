import requests


def verification(number):
    print("your Number is:", number)
    input("Press Enter To Generate OTP")
    url = "https://verificationapi-v1.sinch.com/verification/v1/verifications"
    payload = "{\n  \"identity\": {\n  \"type\": \"number\",\n  \"endpoint\": \"" + \
        number+"\"\n  },\n  \"method\": \"sms\"\n}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ODdjMTUzYTAtNjBlYy00ZjgzLWE2MzQtYTAwMDhmMjQzMTQ1OjZELzBIZkJtblVDRXZuYjVPNFlrUGc9PQ=='
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    while True:
        otp = input("Enter otp: ")
        url = "https://verificationapi-v1.sinch.com/verification/v1/verifications/number/"+number
        payload = "{ \"method\": \"sms\", \"sms\":{ \"code\": \""+otp+"\" }}"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ODdjMTUzYTAtNjBlYy00ZjgzLWE2MzQtYTAwMDhmMjQzMTQ1OjZELzBIZkJtblVDRXZuYjVPNFlrUGc9PQ=='
        }
        response = requests.request("PUT", url, headers=headers, data=payload)
        check1 = response.json()
        check = {"status": "", "message": ""}
        for i in check1:
            if i == "status":
                check["status"] = check1[i]
            elif i == "message":
                check["message"] = check1[i]
        if check["status"] == "SUCCESSFUL":
            print(check["status"], "👍")
            break
        else:
            print(check["message"], "⚠️")
            print()
            continue
    return -1

# verification('+919926040407')
