class CompanyModel:
    def __init__(self, CompanyName: str, OwnerName: str, CompanyAddr: str, CountryId: int, StateId: int, CityId: int, ZipCode: str):
        self.CompanyName = CompanyName
        self.OwnerName = OwnerName
        self.CompanyAddr = CompanyAddr
        self.CountryId = CountryId
        self.StateId = StateId
        self.CityId = CityId
        self.ZipCode = ZipCode

class LoginModel:
    def __init__(self, Mobile: str, Email: str, Password: str, IsActive: int, UserType: int):
        self.Mobile = Mobile
        self.Email = Email
        self.Password = Password
        self.IsActive = IsActive
        self.UserType = UserType