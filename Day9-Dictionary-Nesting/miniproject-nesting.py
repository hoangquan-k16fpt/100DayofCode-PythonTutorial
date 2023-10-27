country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = input() # create list from formatted string
list_of_cities = list_of_cities.split(", ")
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
def add_new_country(country, visits, cities):
    new_country_dict = {}
    new_country_dict["country"] = country
    new_country_dict["visits"] = visits
    new_country_dict["cities"] = cities
    travel_log.append(new_country_dict)
    
add_new_country(country= country, visits= visits, cities= list_of_cities)
print(travel_log)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favorite city is {travel_log[2]['cities'][0]}.")