from xml.dom import minidom

from world.domain import Country

document = minidom.parse("resources/countries.xml")

countries = document.documentElement.getElementsByTagName("country")


def find_countries(predicate, sorter):
    result = []
    for country in countries:
        a_country = Country()
        a_country.code = country.getElementsByTagName("Code")[0].childNodes[0].data
        a_country.name = country.getElementsByTagName("Name")[0].childNodes[0].data
        a_country.continent = country.getElementsByTagName("Continent")[0].childNodes[0].data
        a_country.nufus = country.getElementsByTagName("Population")[0].childNodes[0].data
        a_country.surfaceArea = float(country.getElementsByTagName("SurfaceArea")[0].childNodes[0].data)
        if predicate(a_country):
            result.append(a_country)
    result.sort(key=sorter)
    return result


for _country in find_countries(
        lambda ctry: ctry.continent == "Europe",
        lambda ctry: ctry.nufus
):
    print(_country)