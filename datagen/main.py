
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import random
cred = credentials.Certificate("cryptotracker316-firebase-adminsdk-z6t6n-c9e58626d5.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


# docs = db.collection(u'users').stream()
# arr = []
# for doc in docs:
#     arr.append(doc.id)

# print(arr)


users = ['061efWttVbUmLdVqJ9xJ2uPuGHq1', '1SIZdCgnMKPC6K6T3WrU0Uydxfx1', '3VbM5cWzGSbgx8yuzGMk6qlFLLv2', '3qENBBybbcWok8zALU6jQ5pZvzc2', '5CSm6NYMWIXrYUBGhPbzLdc8Pjs2', '5Gv9lcQKbPgxfyL89pA4AuenNkx2', '5W5xH37nYndGv47gPUA0cnGR7SN2', '5aMV8bnRmATjjmDWRjBDwaQDV6v2', '7QBpFO0uO0MfGi58RJKhbZIURGr2', '7tiiO0pvGmaRHQBsgMTUSYsHmLR2', '8GqiHMnZEphZrx6Ct9Xauwbb70n2', '9VLXJr5Tffbk57BOQ5Gqr3WG4xC2', '9uvYoaZPsUOoqlBChuZD9ufZAv02', 'A3RbflLANmSAoQ7DEMakO86pXBC2', 'BflR8H7XGPZRzk2UyVpjmZ5ndjm2', 'CdiVuu74oOf9BpZur2pS5ZmspuQ2', 'DEIFl8sjIcSlkgbj5nrfLDsehS23', 'EciR2H33NxZi0ZTinbiJtGMFdZh2', 'GViCLLd4p8bXAcYXGwRXoceaAAp2', 'H8q7uCLaD4dyp1C5M5fhtMaLK203', 'I5tQ6tf7WFPDUjZ49SlMGfLt0xu2', 'Iy4ssfiv7iW25MyhyP4FdExoWzr2', 'LEDJvp5lxmUqQGwVMNdyCmTwXjH2', 'NSwtoHMnkTRlnp3ftIvVijQ2E5q2', 'O0LLC1LjDzSDNR8cJCtJP2rkgAo1', 'Og6eRK7y3vZ06cpd7RoTSsQWgEe2', 'P3TpvyK5KNNceZzy2pTvZ0APEO03', 'PaFOCGC4uygYWREGuEQJ2ndrKIl1', 'QuLdX9kv5sS6tSIL0qbyLR8mtXg1', 'RD4S3WOmzQdNbvPBn4YKUQqEM1U2', 'S1qv22jynqbJlioouleRRir9s5v1', 'SNwUGsVJ8yUDqi8mpvxsM7Fzcqm2', 'ThJQ6aZNtbgMGNCPaUWLuIPhK582', 'UcmekEdZ6tcX6y4ABglncACDfM33', 'YJyFFfO39fMZZUeYFYCvf5ZNovz2', 'YOfp2YNZwfTwaCUZv0CuPP4hOW23', 'YhBynh44UlQ2OMspFsNn5l5z9dJ3', 'ZNLuxhy9xWRmq2J2PjLCNEZ1z1L2', 'ZWhUffSe9iWWATwMsPUvh7DYRt62', 'b7WsxRfmwTeuxbeiSLX5aldANo22', 'bb1O5Ds7hOdo2MvOtZuXgKcdwYp2', 'c06IUcHCwRUSi4lHBI28V1xMITe2', 'db6ZFIXn2VSYYro3w8C0FqbxDWp2', 'e9tGetyWEzRmWlfCY4VRxlXdnpd2', 'eHSE0RRiMNSUripmQR44UsmLvQu2', 'f7DVFLPUdUUBv9WVE1dDda6ZK8t2', 'hS7H5jwWztQl54Tuaj6uksXkkjU2', 'iavHNG0obFfFYSsVHvykgHkPvXB3', 'ibJDJztx7sdBRbkoaNi3XrxwEwQ2', 'irE3ggoLCFbdkfJGZ2ZSn6SjJNo2', 'j3KrlvLtMlhtn9wpnlG8JMFeGhj2', 'j9WRoqe4DbcLIUcXGFGL1qHz1u42', 'jtAmQON08dVlLP6tbCMIYPy4xUE2', 'kSY786QHyxMbBOrakQHSUTA5eXl2', 'kwKb4xxhZfMEVIGs736OdrmDrDk1', 'lqmNFkTiE8esQvdhxQRBMRFeyYw2', 'n3C1VxLy4ZXVoXNYwHFKgybpHHo2', 'pNW91zgoSsPQ3Ugp6fcXqyWBaok2', 'sstFGGtfVEdJmGeiNjxfYzmepSF3', 'uBhyMYWcSSSGewI2IiX7ud3dzWs2', 'uCUGIaYlzrNbHqGw35TN9Upm5D43', 'w1oI92EictVCkkTs0c4lQYPqVBe2', 'wPKoKqdtbBUaSxXZK0gNSjylPfU2', 'wtzCl1Nj0VdX8tRNFbKA1R6UpVf2', 'x10v99akL2ToKgyrAYGt4DTZTfF2', 'xLJbFitmdtOy80eahZeGCyVGjf13', 'xnJgj0qkzdQEqwjUlVtWgj2y6Mn1', 'yJYWSmTPTrV8W4XuPUqBViiZozj2', 'zs8iZ3fStGhrC1IujlKbKAKlWyt2']


cur = ["BTC",'ETH','LINK','LTC','XRP','DOGE','BCH','BNB']
map = {
       'BTC':'Bitcoin',
       'XRP':'Ripple',
       'LTC':'Litecoin',
       'DOGE':'Dogecoin',
       'ETH':'Ethereum',
       'LINK':'Chainlink',
       'BCH':'Bitcoin Cash',
       'BNB':'Binance Coin'       
   }

for i in range(0,100):
    cc = random.choice(cur)
    lim = 50
    if cc=='BTC' or cc=='BCH':
        lim=10
    am = round(random.uniform(1,lim), 4)
    uu = random.choice(users)
    ll = random.randint(0,15)

    print(cc + " " + str(am) + " " + uu + " " + str(ll))
    dref = db.collection(u'transaction').document()
    dref.set({
        u'amount': am,
        u'caption': u'Buy {} if you too want a lamboo haha #knowledge #buymycourse. Only 🤡s buy {} '.format(map[cc],random.choice(cur)),
        u'comment_count':0,
        u'like_count':0,
        u'stock': u'{}'.format(cc),
        u'time': firestore.SERVER_TIMESTAMP ,
        u'type':u'buy',
        u'uid': uu
    })


    for i in range(0,ll):
        g = random.choice(users)
        db.collection(u'likes').document().set({
            u'transid': u'{}'.format(dref.id),
            u'uid':u'{}'.format(g)
        })
    

    # time.sleep(3)

    ll = random.randint(0,15)

    dref = db.collection(u'transaction').document()
    dref.set({
        u'amount': am,
        u'caption': u'{} is so overrated tbh I would rather buy {}'.format(map[cc],random.choice(cur)),
        u'comment_count':0,
        u'like_count':0,
        u'stock': u'{}'.format(cc),
        u'time': firestore.SERVER_TIMESTAMP ,
        u'type':u'sell',
        u'uid': uu
    })

    for i in range(0,ll):
        g = random.choice(users)
        db.collection(u'likes').document().set({
            u'transid': u'{}'.format(dref.id),
            u'uid':u'{}'.format(g)
        })