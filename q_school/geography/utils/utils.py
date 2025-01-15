import re


AO_FORM_REGION_REGEX = re.compile(r'(?P<name>[\s\w]+) \((?P<country>\w+): (?P<territory>\w+), (?P<city>[\s\w]+)\)')
