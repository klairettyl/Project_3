import data
import build_data

full_data = build_data.get_data()

# part 1 - Total Population
def population_total(counties: list[data.CountyDemographics]) -> int:
    return sum(county.population["2014 Population"] for county in counties)


#Part 2 - Filter Counties by State
def filter_by_state(counties: list[data.CountyDemographics], state: str) -> list[data.CountyDemographics]:
    return [county for county in counties if county.state == state]

#Part 3 - Calculate sub-populations
def population_by_education(counties: list[data.CountyDemographics], key: str) -> float:
    return sum(county.education.get(key, 0) * county.population["2014 Population"] / 100 for county in counties)

def population_by_ethnicity(counties: list[data.CountyDemographics], key: str) -> float:
    return sum(county.ethnicities.get(key, 0) * county.population["2014 Population"] / 100 for county in counties)

def population_below_poverty_level(counties: list[data.CountyDemographics]) -> float:
    return sum(county.income["Persons Below Poverty Level"] * county.population["2014 Population"] / 100 for county in counties)

#Part 4 - Calculate Overall Percentages
def percent_by_education(counties: list[data.CountyDemographics], key: str) -> float:
    total_population = population_total(counties)
    if total_population == 0:
        return 0.0
    subpopulation = population_by_education(counties, key)
    if subpopulation == 0:
        return 0.0
    return (subpopulation / total_population) * 100

def percent_by_ethnicity(counties: list[data.CountyDemographics], key: str) -> float:
    total_population = population_total(counties)
    if total_population == 0:
        return 0.0
    subpopulation = population_by_ethnicity(counties, key)
    if subpopulation == 0:
        return 0.0
    return (subpopulation / total_population) * 100

def percent_below_poverty_level(counties: list[data.CountyDemographics]) -> float:
    total_population = population_total(counties)
    if total_population == 0:
        return 0.0
    return (population_below_poverty_level(counties) / total_population) * 100

#Part 4 - Filter Counties by Demographic Thresholds
def education_greater_than(counties: list[data.CountyDemographics], key: str, threshold: float) -> list[data.CountyDemographics]:
    return [county for county in counties if key in county.education and county.education[key] > threshold]

def education_less_than(counties: list[data.CountyDemographics], key: str, threshold: float) -> list[data.CountyDemographics]:
    return [county for county in counties if key in county.education and county.education[key] < threshold]

def ethnicity_greater_than(counties: list[data.CountyDemographics], key: str, threshold: float) -> list[data.CountyDemographics]:
    return [county for county in counties if key in county.ethnicities and county.ethnicities[key] > threshold]

def ethnicity_less_than(counties: list[data.CountyDemographics], key: str, threshold: float) -> list[data.CountyDemographics]:
    if not counties:
        return []
    matches = []
    for county in counties:
        if key in county.ethnicities and county.ethnicities[key] < threshold:
            matches.append(county)
    return matches

def below_poverty_level_greater_than(counties: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    return [county for county in counties if county.income["Persons Below Poverty Level"] > threshold]

def below_poverty_level_less_than(counties: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    return [county for county in counties if county.income["Persons Below Poverty Level"] < threshold]
