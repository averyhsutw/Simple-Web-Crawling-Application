import requests
token_position = '../LineAPI/notifyToken.txt'

f = open(token_position,'r')
myToken = f.read()

def lineNotify(token=myToken, msg=''):
  url = "https://notify-api.line.me/api/notify"
  headers = {
              "Authorization": "Bearer " + token,
              #"Content-Type" : "application/x-www-form-urlencoded"
  }
  payload = {'message': msg}
  r = requests.post(url, headers = headers, params = payload)
  return r.status_code


if __name__=='__main__':
  msg = "早安"
  lineNotify(myToken, msg)
