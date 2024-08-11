from dbconfig import connect, SaveDataIntoTables
from flask import Blueprint, jsonify, request
from datetime import datetime
from Models.CommonModels import CompanyModel, LoginModel
from Methods.CommonMethods import generate_alphanumeric_string

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/signup', methods=["POST"])
def SignUpCompany():
    try:

        Data = request.json;
        SignUpData = Data['SignUpData']

        CompanyData = CompanyModel(SignUpData['CompanyName'], SignUpData['OwnerName'], SignUpData['CompanyAddr'], SignUpData['CountryId'], SignUpData['StateId'], SignUpData['CityId'], SignUpData['ZipCode'])

        Qry = "Insert Into Company(name, OwnerName, Address, CountryId, StateId, CityId, ZipCode, CreatedDate) Values(%s, %s, %s, %s, %s, %s, %s, %s)"

        CreatedDate = datetime.now()
        parameter = (CompanyData.CompanyName, CompanyData.OwnerName, CompanyData.CompanyAddr, CompanyData.CountryId, CompanyData.StateId, CompanyData.CityId, CompanyData.ZipCode, CreatedDate)

        response = SaveDataIntoTables(Qry=Qry, parameter=parameter, InsertIntoMainDb=True)

        ResponseData = response.get_json() 

        if int(ResponseData[1]["Last_InsertedId"]) > 0:
            LoginData = LoginModel(SignUpData['Mobile'], SignUpData['Email'], SignUpData['Password'], 0, SignUpData['UserType'])
            
            Qry = "Insert Into LoginDetails(Mobile, Email, Password, IsActive, UserType, AccessToken, LastLoginDate, CreatedDate) Values(%s, %s, %s, %s, %s, %s, %s, %s)"

            AccessToken = generate_alphanumeric_string()
            parameter = (LoginData.Mobile, LoginData.Email, LoginData.Password, 0, LoginData.UserType, AccessToken, CreatedDate, CreatedDate)

            response1 = SaveDataIntoTables(Qry=Qry, parameter=parameter, InsertIntoMainDb=True)

            ResponseData1 = response1.get_json()
            LoginId = ResponseData[1]["Last_InsertedId"]
            
            if LoginId > 0:
                return jsonify({"Response:" : {"Message:": "Sign-Up Successfully."}}, {"Success": True});
            else:
                return jsonify({"Response:" : ResponseData1[0]}, {"Success": False});
    
        else:
            return jsonify({"Response:" : ResponseData[0]}, {"Success": False});

    except Exception as e:
        return jsonify({"Error:" : {"Message: " : str(e)}});

@login_blueprint.route('/verifyuser', methods=["GET"])
def VerifyUser():
    try:
        Data = request.json
        UserData = Data['UserData']
        print(UserData)
    except Exception as e:
        return jsonify({"Error:" : {"Message: " : str(e)}});