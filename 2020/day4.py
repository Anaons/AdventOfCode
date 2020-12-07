sample = [
"ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
"byr:1937 iyr:2017 cid:147 hgt:183cm",
"",
"iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
"hcl:#cfa07d byr:1929",
"",
"hcl:#ae17e1 iyr:2013",
"eyr:2024",
"ecl:brn pid:760753108 byr:1931",
"hgt:179cm",
"",
"hcl:#cfa07d eyr:2025 pid:166559648",
"iyr:2011 ecl:brn hgt:59in",
""
]

from dataclasses import dataclass
import re

@dataclass
class Passport:
    '''Class for keeping the Passport details'''
    d: dict

def parseLine(line: list, passport: Passport):
    rawvalues = line.split()
    for raw in rawvalues:
        key, value = raw.split(':')
        passport.d[key] = value

def read_input(lines: list):
    passports = []
    passport = Passport(d = {})
    for line in lines:
        # I've added extra empty lines at teh end of the input to simplify the parsing         
        if line == "":
            passports.append(passport)
            passport = Passport(d = {})
        else:
            parseLine(line, passport)
    return passports

def isPassportValid(passport: Passport, dataValidation: bool):
    expectedFields = [
        "byr", # (Birth Year)
        "iyr", # (Issue Year)
        "eyr", # (Expiration Year)
        "hgt", # (Height)
        "hcl", # (Hair Color)
        "ecl", # (Eye Color)
        "pid", # (Passport ID)
        #"cid", # (Country ID)   # OPTIONAL
    ]

    for field in expectedFields:
        if field not in passport.d.keys():
            return False
        elif dataValidation and field == "byr":
            if not 1920 <= int(passport.d[field]) <= 2002:
                return False
        elif dataValidation and field == "iyr":
            if not 2010 <= int(passport.d[field]) <= 2020:
                return False
        elif dataValidation and field == "eyr":
            if not 2020 <= int(passport.d[field]) <= 2030:
                return False
        elif dataValidation and field == "hgt":
            h = passport.d[field]
            if not h.endswith("cm") and not h.endswith("in"):
                return False
            elif h[-2:] == "cm":
                if not 150 <= int(h[:-2]) <= 193:
                    return False
            elif h[-2:] == "in":
                if not 59 <= int(h[:-2]) <= 76:
                    return False
        elif dataValidation and field == "hcl":
            if not re.match("^#[0-9a-f]{6}$", passport.d[field]):
                return False
        elif dataValidation and field == "ecl":
            if passport.d[field] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
        elif dataValidation and field == "pid":
            if not re.match("^[0-9]{9}$", passport.d[field]):
                return False
    return True

def checkPassports(passports: list, dataValidation = False):
    nb = 0
    for passport in passports:
        if isPassportValid(passport, dataValidation):
            nb += 1
    return nb

# read input
values = []
with open('2020/input4.txt') as f:
    values = f.read().splitlines()
# print(repr(values[0]))
# print(repr(values[3]))
# print(repr(values[-1]))

# part 1
print(checkPassports(read_input(sample)))
print(checkPassports(read_input(values)))

# part 2
print(checkPassports(read_input(values), dataValidation = True))
