import strawberry as sb
from energy import schemas
from energy import repo
from typing import List, Optional

@sb.input
class Filter:
    name: str

# QUERY CONSTRUCTOR

@sb.type
class Query:
    @sb.field
    def retrieve_emissions_per_country(self, filter: Optional[Filter] = None) -> Optional[List[schemas.Country]]:
        countries = repo.EmissionsRepoImpl.get_countries()
        if filter is not None:
            countries = repo.EmissionsRepoImpl.get_by_country_name(
                country_name=filter.name)
        return countries

    @sb.field
    def retrieve_emissions_per_industry(self, filter: Optional[Filter] = None) -> Optional[List[schemas.Industry]]:
        industries = repo.EmissionsRepoImpl.get_industries()
        if filter is not None:
            industries = repo.EmissionsRepoImpl.get_by_industry_name(
                industry_name=filter.name)
        return industries
        
