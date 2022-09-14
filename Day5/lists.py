# 1
from traceback import print_tb


empty = []
print(empty)

# 2
fiveele = [1, 2, 3, 4, 5]
print(fiveele)

# 3
print(len(fiveele))

# 4
print(fiveele[::2])

# 5
mixedDataTypes = ["Mukesh", 21, 158.65, "Single", "17-24,Sangareddy Telangana"]
print(mixedDataTypes)

# 6
itCompanies = ["Facebook", "Google", "Microsoft",
               "Apple", "IBM", "Oracle", "Amazon"]

# 7
print(itCompanies)

# 8
print(len(itCompanies))

# 9
half = int(len(itCompanies)/2)
print(itCompanies[0], itCompanies[half], itCompanies[-1])

# 10
itCompanies[6] = "Coding Minutes"
print(itCompanies)

# 11
itCompanies.append("Amazon")
print(itCompanies)

# 12
itCompanies.insert(half, "Cognizant")
print(itCompanies)


# 13
itCompanies[0] = itCompanies[0].upper()
print(itCompanies)


# 14
itCompaniesHash = "#".join(itCompanies)
print(itCompaniesHash)


# 15
print("Coding Minutes" in itCompanies)

# 16
itCompanies.sort()
print(itCompanies)

# 17
itCompanies.reverse()
print(itCompanies)


# 18
print(itCompanies[2:])
# 19
print(itCompanies[-3:])
# 20
half = int(len(itCompanies)/2)
print(itCompanies[half:half+1])

# 21
itCompanies.remove(itCompanies[0])
print(itCompanies)

# 22
itCompanies.remove(itCompanies[half])
print(itCompanies)


# 23
itCompanies.remove(itCompanies[-1])
print(itCompanies)

# 24
itCompanies.clear()
print(itCompanies)

# 25
del itCompanies

# 26
frontEnd = ['HTML', 'CSS', 'JS', 'React', 'Redux']
backEnd = ['Node', 'Express', 'MongoDB']
print(frontEnd+backEnd)

# 27
fullStack = frontEnd+backEnd
print(fullStack)



###########################Exercise:Level2###########################
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages[0],ages[-1])
ages.append(ages[0])
ages.append(ages[-1])
print(len(ages))
median=((len(ages)/2)+(len(ages)+1)/2)/2
print(median)
average=sum(ages)/len(ages)
print(average)
print(abs(ages[0] - sum(ages) / len(ages)))
print(abs(ages[-1] - sum(ages) / len(ages)))
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]

print([countries[i]
       for i in range((len(countries) // 2) - (1 if int(len(countries)) % 2 == 0 else 0), len(countries) // 2 + 1)])
length = len(countries)
if length % 2 == 0:
    first_half = countries[:length // 2]
    second_half = countries[length // 2:]
else:
    first_half = countries[:length // 2 + 1]
    second_half = countries[length // 2 + 1:]
print(first_half)
print(second_half)

spclLists=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandicCountries=spclLists[3:]
print(scandicCountries)