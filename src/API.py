from dotenv import load_dotenv
from os import environ
from Utility import hash, randstring
from time import time
from requests import get

class API:
    def __init__(self):
        load_dotenv()

        self.key = environ["KEY"]
        self.secret = environ["SECRET"]

    def getdata(self):
        return {"time": int(time()), "rand": randstring(6, "0123456789")}

    def url(self, method, params):
        crrdata = self.getdata()
        tmpparams = params
        tmpparams.append(["apiKey", self.key])
        tmpparams.append(["time", crrdata["time"]])
        tmpparams.sort()

        params_string =  "&".join([f"{v[0]}={str(v[1])}" for v in tmpparams])
        hash_string = f"{crrdata['rand']}/{method}?{params_string}#{self.secret}"
        
        hash_string = hash(hash_string)

        return f"https://codeforces.com/api/{method}?{params_string}&apiSig={crrdata['rand']}{hash_string}"

    def apicall(self, url):
        return get(url).json()

    def call(self, method, params):
        url = self.url(method, params)
        return self.apicall(url)

if __name__ == "__main__":
    caller = API()
    data = [["contestId", 1605], ["handles", "TranGiaHuy;SanguineChameleon;socpite;Kawaii"]]
    
    # print(caller.call("contest.standings", data))

    pass