import json

country_data = []
#sovereigns = []
#sovereigns_count = 0
try:
    flag_fh = open('flag-descriptions.json')
    flag_descriptions = json.load(flag_fh)
    with open('src/main/resources/countriesV3.1.json') as fh:
        data = json.load(fh)
        for country_count, country in enumerate(data):
            flag_data = None
            # Query country's common name.
		    # For countries that share common names e.g. Guinea,
			# query country's official name
            if country['name']['common'] in flag_descriptions:
                flag_country_name = country['name']['common']
            elif country['name']['official'] in flag_descriptions:
                flag_country_name = country['name']['official']
            try:
                if country['independent'] == True:
                    #sovereigns.append(country['name']['common'])
                    #sovereigns_count += 1
                    flag_data = {'flagImages': country['flags'],
                                'flagDescription': flag_descriptions[flag_country_name]}
            except KeyError:
                # Don't alter data of non-independent countries
                pass
            finally:
                country_data.append(country)
                if flag_data is not None:
                    country_data[country_count]['flags'] = flag_data
finally:
    flag_fh.close()
with open('src/main/resources/countriesV3.1.json', 'w', encoding='utf-8') as write_fh:
        json.dump(country_data, write_fh, indent=2, separators=(", ", ": "))
#print(len(country_data))
#print(sovereigns_count)
#print(sorted(sovereigns))