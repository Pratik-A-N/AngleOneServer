from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from SmartApi import SmartConnect
import pyotp
from logzero import logger


api_key = "ULcmdsnK"
username = "P51775178"
pwd = "9007"
token = "PV5G2HDOHFASFDP5TURQQLA664"

# Create your views here.
@api_view(['POST'])
def getLTP(request):
    totp = pyotp.TOTP(token).now()
    smartApi = SmartConnect(api_key)
    try:
        correlation_id = "abcde"
        data = smartApi.generateSession(username, pwd, totp)

        if data['status'] == False:
            logger.error(data)
        else:
            # login api call
            # logger.info(f"You Credentials: {data}")
            authToken = data['data']['jwtToken']
            refreshToken = data['data']['refreshToken']
            print(authToken)
            print(refreshToken)
        data = smartApi.ltpData("NSE","Nifty Media","99926031")
        return Response(data)
    except Exception as e:
        return Response("Invalid Token: The provided token is not valid.")