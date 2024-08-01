from enum import Enum
import json
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta


class BarSizeType(Enum):
    S = 'sec'
    M = 'min'
    H = 'hour'
    D = 'day'
    W = 'week'
    MM = 'month'


class Auth(object):
    def __init__(self) -> None:
        self.__login = False
        self.__customer_symbols = []
        self.__customer_data = None
        self.__development_toggle = False
        self.__beta_toggle = False
        self.__ms_track_url = 'http://track.algodojo.com:8005/'
        self.__ms_auth_url = 'https://auth.algodojo.com/'
        self.__DATEFORMAT = "%Y-%m-%d %H:%M:%S"
        self.__VERSION = "0.3.4"
        self.requestCount = 1

    def sign_in(self, token, broker):
        self.__post_authentication(token, broker)

    def post_order_data(self, data):
        self.__post_order(data)

    def __post_order(self, data):
        url = self.__ms_track_url+"order/save_order_data"
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        payload = {"token": self.__customer_data,
                   "data": json.dumps(data)}
        requests.post(url, data=payload, headers=header)

    def check_bata(self):
        if self.__beta_toggle:
            raise ValueError(
                "The function is currently not supported in the BETA version")

    def check_status(self):
        if self.__development_toggle:
            return

        if not self.__login:
            print('no login')
            span = 'Token is fail, before useing the algodojo api, you must first register it! Please go the https://www.algodojo.com/'
            raise ValueError(span)
        
        return self.__customer_data

    def check_symbol(self, symbol):
        if 'ALL' in self.__customer_symbols:
            return

        if self.__development_toggle:
            return

        if not symbol in self.__customer_symbols:
            span = 'Get Data is fail, before useing the symbol, you must first register it! Please go the https://www.algodojo.com/'
            raise ValueError(span)

    def process_market(self, contractParams, requestParams):
        try:
            symbol = contractParams.get('symbol')
            secType = contractParams.get('secType')
            currency = contractParams.get('currency')
            data = {
                "symbol": symbol,
                "secType": secType,
                "currency": currency,
                "barSize": requestParams.get('barSize'),
            }
            self.__post_marketdata(data)
        except:
            pass

    def post_historydata(self, data):
        self.__post_historydata(data)

    def process_history(self, contract, requstParams):
        try:
            symbol = contract.get('symbol')
            secType = contract.get('secType')
            currency = contract.get('currency')
            endDateTime = requstParams.get('endDateTime') + ' 00:00:00'
            startDateTime = requstParams.get('startDateTime') + ' 00:00:00'
            barSize = requstParams.get('barSize').split(' ')
            barSizeType = barSize[1]
            barSizeValue = barSize[0]
            valueList_sec = ['5', '10', '15', '30']
            valueList_min = ['5', '10', '15', '30']
            valueList_hour = ['5', '10', '15', '30']
            valueList_day = ['5', '10', '15', '30']
            valueList_week = ['5', '10', '15', '30']
            valueList_month = ['5', '10', '15', '30']
            if (barSizeType == BarSizeType.S.value) and (not barSizeValue in valueList_sec):
                raise ValueError("barSize only supports 5,10,15,30 sec")

            barSizeType = BarSizeType(barSize[1]).name
            barSize = barSize[0]
            data = {
                "symbol": symbol,
                "secType": secType,
                "currency": currency,
                "startDateTime": startDateTime,
                "endDateTime": endDateTime,
                "barSize": barSize,
                "barSizeType": barSizeType,
            }
            return data
        except AssertionError as msg:
            raise(msg)

    def __getStartDate(self, barSize, barSizeType, endDate):
        startDate = endDate
        if barSizeType == BarSizeType.S.value:
            startDate = startDate - relativedelta(seconds=barSize)
        elif barSizeType == BarSizeType.m.value:
            startDate = startDate - relativedelta(minutes=barSize)
        elif barSizeType == BarSizeType.H.value:
            startDate = startDate - relativedelta(hours=barSize)
        elif barSizeType == BarSizeType.D.value:
            startDate = startDate - relativedelta(days=barSize)
        elif barSizeType == BarSizeType.W.value:
            startDate = startDate - relativedelta(weeks=barSize)
        elif barSizeType == BarSizeType.M.value:
            startDate = startDate - relativedelta(months=barSize)
        elif barSizeType == BarSizeType.Y.value:
            startDate = startDate - relativedelta(years=barSize)
        return startDate

    def __post_historydata(self, data):
        try:
            url = self.__ms_track_url+"inquire/save_history_data"
            header = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            nowTime = datetime.now().strftime(self.__DATEFORMAT)
            payload = {"token": self.__customer_data,
                       "symbol": data.get('symbol'),
                       "secType": data.get('secType'),
                       "currency": data.get('currency'),
                       "startDateTime": data.get('startDateTime'),
                       "endDateTime": data.get('endDateTime'),
                       "barSize":  data.get('barSize'),
                       "barSizeType": data.get('barSizeType'),
                       }
            response = requests.post(url, data=payload, headers=header)
        except:
            pass

    def __post_marketdata(self, data):
        strspan = 'send the post_marketdata'
        try:
            url = self.__ms_track_url+"inquire/save_market_data"
            header = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            nowTime = datetime.now().strftime(self.__DATEFORMAT)
            payload = {"token": self.__customer_data,
                       "symbol": data.get('symbol'),
                       "secType": data.get('secType'),
                       "currency": data.get('currency'),
                       "startDateTime": nowTime,
                       "endDateTime": nowTime,
                       "barSize":  data.get('barSize'),
                       "barSizeType": "sec",
                       }
            response = requests.post(url, data=payload, headers=header)
        except Exception as ex:
            print(f"{strspan} error: {ex}")
            pass

    def __post_authentication(self, token, broker):
        url = self.__ms_auth_url+"auth/customer"
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        payload = {"token": token,
                   "broker": broker}
        response = requests.post(url, data=payload, headers=header)
        response = json.loads(response.content)
        self.__login = response["result"]
        if response["result"]:
            self.__customer_data = response["customer_data"]
            self.__customer_symbols = response["customer_symbols"]
            if 'ALL' in self.__customer_symbols:
                self.requestCount = 50
            if self.__VERSION != response["version"]:
                print('A new version of the AlgoDojo API is available. Please update to the latest version to maintain compatibility using the command: "python -m pip install --upgrade algodojo"')
