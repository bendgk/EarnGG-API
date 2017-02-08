import urllib2
import json

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]

key = "insert_key_here"
secret = "insert_secret_here"


def get_balance():
    response = opener.open('http://earn.gg/account/get?key=' + key + '&secret=' + secret)
    resp = json.load(response)
    return resp['result']['balance']

def roll(amount, payout):
    response = opener.open('http://earn.gg/gamble/roll?amount=' + str(int(amount)) + '&payout=' + str(int(payout)) + '&key=' + key + '&secret=' + secret)
    resp = json.load(response)
    return resp['won']
