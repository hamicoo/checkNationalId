from flask import Flask,jsonify

app=Flask(__name__)

def idchecker(nationalid):
    idcasttostr=str(nationalid)
    if len(idcasttostr) != 10 or idcasttostr.isdigit() is False:
        return False,"The Number Of ID Number Is Invalid"
    else:
        a=int(nationalid[9:10])
        b=int(nationalid[0:1]) * 10 + int(nationalid[1:2]) * 9 + int(nationalid[2:3]) * 8 +int(nationalid[3:4]) * 7 + int(nationalid[4:5]) * 6 +int(nationalid[5:6]) * 5 + int(nationalid[6:7]) * 4 +int(nationalid[7:8]) * 3 + int(nationalid[8:9]) * 2
        c = int(b)%11
        if (int(c) < 2 and int(a) == int(c)) or (c>=2 and (11-c)==a):
            return True,"Valid!"
        else:
            return False,"Not Valid !"

def checkUnit():
    return "token12"


@app.route("/checkid/<nationalid>")
def checker(nationalid):
    status,response=idchecker(nationalid)
    return jsonify({"status":status,"message":response})



@app.route("/testapi")
def ctest():
    return jsonify({"message":"it seems every thing is ok!"})


@app.route("/")
def intro():
    #this is my message
    return jsonify({"message":"it seem's every thinbg is ok or not okey from mehdi!?"})


if __name__ == '__main__':
	app.run()




