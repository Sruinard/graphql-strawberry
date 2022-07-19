from energy import models


class EmissionsRepo:
    _industries = [
        {
        "name": "other",
        "emission": 10
        },
        {
        "name": "electricity",
        "emission": 25
        },
        {
        "name": "agriculture",
        "emission": 24
        },
        {
        "name": "buildings",
        "emission": 6
        },
        {
        "name": "transportation",
        "emission": 14
        },
        {
        "name": "industry",
        "emission": 21
        },
    ]
    _countries = [
        {
            "name": "china",
            "emission": 30
        },
        {
            "name": "US",
            "emission": 15
        },
        {
            "name": "EU-28",
            "emission": 9
        },
        {
            "name": "india",
            "emission": 7
        },
        {
            "name": "russia",
            "emission": 5
        },
        {
            "name": "japan",
            "emission": 4
        },
        {
            "name": "other",
            "emission": 30
        },
    ]



    def __init__(self, industries=[], countries=[]):
        self.industries = industries
        self.countries = countries
        
        for industry in self._industries:
            self.industries.append(
                models.Industry(
                    name=industry["name"],
                    emission=industry["emission"]
                )
            )
        
        for country in self._countries:
            self.countries.append(
                models.Country(
                    name=country["name"],
                    emission=country["emission"]
                )
            )
            

    def get_industries(self):
        return self.industries

    def get_countries(self):
        return self.countries

    def get_by_industry_name(self, industry_name):
        return [industry for industry in self.industries if industry.name == industry_name]

    def get_by_country_name(self, country_name):
        return [country for country in self.countries if country.name == country_name]


EmissionsRepoImpl = EmissionsRepo()
