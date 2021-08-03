from flask import Flask
from controllers.globalwarning import GlobalWarning

app=Flask(__name__)

str_nitrousOxide = 'https://global-warming.org/api/nitrous-oxide-api'
str_co2 = 'https://global-warming.org/api/co2-api'
str_methane = 'https://global-warming.org/api/methane-api'
str_arctic = 'https://global-warming.org/api/arctic-api'

@app.route('/nitrous-oxide', methods=['GET'])
def nitrousOxide():
    return GlobalWarning(str_nitrousOxide).getAll()
@app.route('/co2', methods=['GET'])
def co2():
    return GlobalWarning(str_co2).getAll()
@app.route('/methane', methods=['GET'])
def methane():
    return GlobalWarning(str_methane).getAll()
@app.route('/arctic', methods=['GET'])
def arctic():
    return GlobalWarning(str_arctic).getAll()


app.run()