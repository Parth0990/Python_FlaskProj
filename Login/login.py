from dbconfig import connect, SaveDataIntoTables
from flask import Blueprint, jsonify, request,json
from datetime import datetime


class LoginModel:
    def __init__(self, CompanyName: str, OwnerName: str, CompanyAddr: str, CountryId: int, StateId: int, CityId: int, ZipCode: str, Email: str, Mobile: str, Password: str):
        self.CompanyName = CompanyName
        self.OwnerName = OwnerName
        self.CompanyAddr = CompanyAddr
        self.CountryId = CountryId
        self.StateId = StateId
        self.CityId = CityId
        self.ZipCode = ZipCode
        self.Email = Email
        self.Mobile = Mobile
        self.Password = Password

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/signup', methods=["POST"])
def SignUpCompany():
    try:
        Data = request.json;
        SignUpData = Data['SignUpData']
        loginData = LoginModel(SignUpData['CompanyName'], SignUpData['OwnerName'], SignUpData['CompanyAddr'], SignUpData['CountryId'], SignUpData['StateId'], SignUpData['CityId'], SignUpData['ZipCode'], SignUpData['Email'], SignUpData['Mobile'], SignUpData['Password'])
        Qry = "Insert Into Company(name, OwnerName, Address, CountryId, StateId, CityId, ZipCode, CreatedDate) Values(%s, %s, %s, %s, %s, %s, %s, %s)"
        CreatedDate = datetime.now()
        parameter = (loginData.CompanyName, loginData.OwnerName, loginData.CompanyAddr, loginData.CountryId, loginData.StateId, loginData.CityId, loginData.ZipCode, CreatedDate)
        response = SaveDataIntoTables(Qry=Qry, parameter=parameter, InsertIntoMainDb=True)
        ResponseData = response.get_json()
        companyId = ResponseData[1]["Last_InsertedId"]
        print(companyId)
        return jsonify({"Response:" : ResponseData[0]}, {"Success": True});
    except Exception as e:
        return jsonify({"Error:" : {"Message: " : str(e)}});