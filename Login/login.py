from dbconfig import connect, SaveDataIntoTables
from flask import Blueprint, jsonify, request


class LoginModel:
    def __init__(self, CompanyName, OwnerName, CompanyAddr, CountryId, StateId, CityId, ZipCode, Email, Mobile, Password):
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
        Qry = "Insert Into Company(CompanyName, OwnerName, CompanyAddr, CountryId, StateId, CityId, ZipCode) Values(%s, %s, %s, %s, %s, %s, %s)"
        parameter = (loginData.CompanyName, loginData.OwnerName, loginData.CompanyAddr, loginData.CountryId, loginData.StateId, loginData.CityId, loginData.ZipCode)
        msg = SaveDataIntoTables(Qry=Qry, parameter=parameter, InsertIntoMainDb=True)
        return jsonify({"Error:" : {"Message": str(msg)}});
    except Exception as e:
        return jsonify({"Error:" : {"Message: " : str(e)}});