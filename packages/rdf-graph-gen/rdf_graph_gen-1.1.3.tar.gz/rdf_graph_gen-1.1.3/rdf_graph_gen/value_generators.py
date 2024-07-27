import csv
import math
import random
from exrex import *
from exrex import _randone
from rdflib import XSD, Literal, URIRef, Namespace
from datetime import date
from dateutil.relativedelta import relativedelta
from rdf_graph_gen.shacl_mapping_generator import SCH
import pkg_resources

"""
Reads data from a CSV file and returns the content as a list of values.

Parameters:
-----------
file_name (str): The name of the CSV file from which data will be read.

Returns:
--------
list: A list containing the values read from the CSV file.
"""


def get_path(file_name):
    file_path = pkg_resources.resource_filename('rdf_graph_gen', f'datasets/{file_name}')
    return file_path


def get_array_from_csv(file_name):
    results = []  # Initialize an empty list to store the values
    with open(file_name, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:  # Iterate through each row in the CSV file
            results = results + row  # Append values from each row to the results list
    return results  # Return the list containing values from the CSV file

dataset_dictionary = {'streetAddress': get_array_from_csv(get_path("street_name.csv")),
                      'givenNameMale': get_array_from_csv(get_path("male_first_name.csv")),
                      'givenNameFemale': get_array_from_csv(get_path("female_first_name.csv")),
                      'familyName': get_array_from_csv(get_path("surnames.csv")),
                      'gender': ['male', 'female', 'non-binary'],
                      'jobTitle': get_array_from_csv(get_path("job_title.csv")),
                      'bookAward': get_array_from_csv(get_path("book_awards.csv")),
                      'bookGenre': get_array_from_csv(get_path("book_genre.csv")),
                      'bookTitle': get_array_from_csv(get_path("book_titles.csv")),
                      'movieGenre': get_array_from_csv(get_path("movie_genre.csv")),
                      'movieAward': get_array_from_csv(get_path("movie_awards.csv")),
                      'movieTitle': get_array_from_csv(get_path("movie_titles.csv")),
                      'tvSeriesTitle': get_array_from_csv(get_path("tvseries_titles.csv"))
                      }


def getBookFormat():
    return URIRef(SCH[random.choice(["AudiobookFormat", "EBook", "GraphicNovel", "Hardcover", "Paperback"])])


def get_date_between_two_dates(date1, date2):
    days_between = relativedelta(date2, date1).days
    months_between = relativedelta(date2, date1).months
    years_between = relativedelta(date2, date1).years

    increase = random.random()
    new_days = relativedelta(days=int(days_between * increase))
    new_months = relativedelta(months=int(months_between * increase))
    new_years = relativedelta(years=int(years_between * increase))

    between_date = date1 + new_years + new_months + new_days
    return between_date


def add_to_date(date1, years, months, days):
    time_addition = relativedelta(days=days, months=months, years=years)
    return time_addition + date1


# The min_length, max_length, pattern, disjoint, has_value properties are not taken into account at this point for date
# generation
def generate_date(min_exclusive, min_inclusive, max_exclusive, max_inclusive, less_than, less_than_or_equals):
    min_date, max_date = None, None
    if min_inclusive or min_exclusive:
        min_date = date.fromisoformat(min_inclusive) if min_inclusive else add_to_date(
            date.fromisoformat(min_exclusive), 0, 0, +1)
    if max_inclusive or max_exclusive:
        max_date = date.fromisoformat(max_inclusive) if max_inclusive else add_to_date(
            date.fromisoformat(max_exclusive), 0, 0, -1)
    if less_than_or_equals and len(less_than_or_equals) > 0:
        max_date = date.fromisoformat(min(less_than_or_equals))
    if less_than and len(less_than) > 0:
        max_date = date.fromisoformat(min(less_than))
    if max_date:
        if min_date:
            if max_date < min_date:
                raise Exception("A conflicting date definition")
        else:
            min_date = add_to_date(max_date, -50, 0, 0)
    else:
        if not min_date:
            min_date = date.fromisoformat('1970-07-07')
        max_date = add_to_date(min_date, 50, 0, 0)
    return get_date_between_two_dates(min_date, max_date)


# The min_length, max_length, pattern, disjoint, has_value properties are not taken into account at this point for
# integer generation
def generate_integer(min_exclusive, min_inclusive, max_exclusive, max_inclusive, less_than, less_than_or_equals):
    min_int, max_int = None, None
    if min_inclusive is not None or min_exclusive is not None:
        min_int = int(min_inclusive) if min_inclusive is not None else int(min_exclusive) + 1
    if max_inclusive is not None or max_exclusive is not None:
        max_int = int(max_inclusive) if max_inclusive is not None else int(max_exclusive) - 1
    if less_than_or_equals and len(less_than_or_equals) > 0:
        max_int = int(min(less_than_or_equals))
    if less_than and len(less_than) > 0:
        max_int = int(min(less_than) - 1)
    if max_int is not None:
        if min_int is not None:
            if max_int < min_int:
                raise Exception("Conflicting integer constraints")
        else:
            min_int = max_int - 50
    else:
        if min_int is None:
            min_int = 1
        max_int = min_int + 50
    return Literal(random.randint(min_int, max_int))


# The min_length, max_length, pattern, disjoint, has_value properties are not taken into account at this point for
# decimal generation
def generate_decimal(min_exclusive, min_inclusive, max_exclusive, max_inclusive, less_than, less_than_or_equals):
    min_float, max_float = None, None
    if min_inclusive is not None or min_exclusive is not None:
        min_float = float(min_inclusive) if min_inclusive is not None else math.nextafter(float(min_exclusive), +math.inf)
    if max_inclusive or max_exclusive:
        max_float = float(max_inclusive) if max_inclusive is not None else math.nextafter(float(max_exclusive), -math.inf)
    if less_than_or_equals and len(less_than_or_equals) > 0:
        max_float = float(min(less_than_or_equals))
    if less_than and len(less_than) > 0:
        max_float = math.nextafter(float(min(less_than)), -math.inf)
    if max_float is not None:
        if min_float is not None:
            if max_float < min_float:
                raise Exception("Conflicting float constraints")
        else:
            min_float = max_float - 50
    else:
        if min_float is None:
            min_float = 1
        max_float = min_float + 50
    return Literal(random.uniform(min_float, max_float))


# The min_exclusive, min_inclusive, max_exclusive, max_inclusive, disjoint, less_than, less_than_or_equals, has_value
# properties are not taken into account at this point for string generation
def generate_string(min_length, max_length, pattern):
    if min_length:
        min_length = int(min_length)
        if max_length:
            max_length = int(max_length)
            if min_length > max_length:
                raise Exception("Conflicting string constraints")
        else:
            max_length = min_length + 10
    else:
        if max_length:
            max_length = int(max_length)
            min_length = max_length - 5 if max_length > 5 else 0
        else:
            min_length, max_length = 8, 15
    if not pattern:
        pattern = '^([a-zA-Z0-9])*'
    length = random.randint(min_length, max_length)
    strp = ''
    while len(strp) < length:
        strp = strp + _randone(parse(pattern))
    if len(strp) > length:
        strp = strp[:length]
    return Literal(strp)


"""
    Generate a random value based on the specified constraints for a given SHACL property.

    Parameters:
    - datatype (URIRef): The datatype of the SHACL property.
    - min_exclusive, min_inclusive, max_exclusive, max_inclusive: Numeric constraints for the property.
    - min_length, max_length: String length constraints.
    - pattern (str): Regular expression pattern for string values.
    - equals, disjoint, less_than, less_than_or_equals, has_value: Specific constraints for certain values.
    - path (URIRef): SHACL path for the property.
    - sh_class (URIRef): SHACL class to which the property belongs.

    Returns:
    - Literal or None: The generated RDF literal value for the SHACL property, or None if it cannot be generated.

    Explanation:
    - The function starts by extracting the specific class (cl) and property path (path) from the given SHACL class.
    - It handles special cases and applies standard constraints based on the SHACL class and property path.
    - For specific properties like 'isbn', 'numberOfPages', 'abridged', 'bookEdition', 'date', 'number', 'email',
      and 'telephone', it sets standard data types and patterns if not explicitly specified.
    - If constraints like 'equals' are specified, the function returns the specified value.
    - For different data types (integer, decimal, boolean, date, string), it invokes specific helper functions
      to generate values based on constraints.
    - The function returns the generated value or None if a value cannot be generated based on constraints.
"""


def generate_default_value(datatype, min_exclusive, min_inclusive, max_exclusive, max_inclusive, min_length, max_length,
                           pattern, equals, disjoint, less_than, less_than_or_equals, has_value, path, sh_class):

    # Return specified value if 'equals' constraint is present
    if equals:
        return equals

    # Extract the class and property path from URIs
    cl = str(sh_class).split('/')[-1]
    path = str(path).split('/')[-1]

    # Apply default datatype and pattern for certain property paths
    if ('date' in path or 'Date' in path) and not datatype:
        datatype = XSD.date
    elif ('number' in path or 'Number' in path) and not datatype:
        datatype = XSD.integer

    # Apply default patterns for certain property paths
    elif 'email' in path and not pattern:
        pattern = '([a-z0-9]+[_])*[A-Za-z0-9]@gmail.com'
    elif 'telephone' in path and not pattern:
        pattern = '^(([0-9]{3})|[0-9]{3}-)[0-9]{3}-[0-9]{4}$'

    # Special handling for certain properties and their constraints
    if cl == 'Person':
        if 'taxID' == path and not pattern:
            pattern = '[0-9]{9}'
    if cl == 'Book':
        if 'isbn' in path and not pattern:
            pattern = '[0-9]{3}-[0-9]-[0-9]{2}-[0-9]{6}-[0-9]'
        elif 'numberOfPages' in path and not datatype:
            datatype = XSD.integer
            if not min_inclusive:
                min_inclusive = 100
        elif 'abridged' in path and not datatype:
            datatype = XSD.boolean
        elif 'bookEdition' in path and not datatype:
            datatype = XSD.integer

    # Generate values based on datatype and constraints
    if datatype == XSD.integer:
        return generate_integer(min_exclusive, min_inclusive, max_exclusive, max_inclusive, less_than,
                                less_than_or_equals)
    elif datatype == XSD.decimal:
        return generate_decimal(min_exclusive, min_inclusive, max_exclusive, max_inclusive, less_than,
                                less_than_or_equals)
    elif datatype == XSD.boolean:
        return Literal(bool(random.getrandbits(1)))
    elif datatype == XSD.date:
        return Literal(generate_date(min_exclusive, min_inclusive, max_exclusive, max_inclusive, less_than,
                                     less_than_or_equals))

    # Default case: Generate a string value
    return generate_string(min_length, max_length, pattern)


"""
    Function Explanation:
    ---------------------
    The 'get_predefined_value' function generates predefined values for specific SHACL properties based on the provided
    constraints. It handles different cases for SHACL classes such as 'Person', 'Book', 'Movie', and 'TVSeries' and
    generates values accordingly.

    Parameters:
    -----------
    sh_path (rdflib.term.Identifier): SHACL property for which to generate a predefined value.
    sh_class (rdflib.term.Identifier): SHACL class to which the property belongs.
    dependencies (dict): Dictionary containing required dependencies for generating predefined values.

    Returns:
    --------
    rdflib.term.Literal or None: The generated predefined value or None if a predefined value cannot be generated.

    Explanation:
    ------------
    - The function starts by extracting the specific property ('prop') and class ('cl') from the given SHACL path and class.
    - For each case (class-property combination), it generates a predefined value using the 'values_dict' dictionary.
    - The function supports various properties such as 'givenName', 'familyName', 'name', 'streetAddress', 'gender',
      'jobTitle', 'bookTitle', 'bookAward', 'bookGenre', 'movieTitle', 'movieAward', 'movieGenre', 'tvSeriesTitle', etc.
    - 'random.choice' is used to select values from predefined data, ensuring diversity in the generated values.
    - The function returns the generated predefined value or None if a predefined value cannot be generated for the given constraints.
"""


def generate_intuitive_value(sh_path, sh_class, dependencies):

    # Handle cases for Person class
    if sh_class == SCH.Person:
        gender = URIRef(SCH.gender)
        given_name = URIRef(SCH.givenName)
        family_name = URIRef(SCH.familyName)
        name = URIRef(SCH.name)

        if sh_path == SCH.additionalName or sh_path == SCH.givenName:
            # Generate predefined value based on gender dependency
            gender = str(dependencies.get(gender, ["none"])[0])
            if gender in (SCH.Female, 'female', 'f', 'fem'):
                return Literal(random.choice(dataset_dictionary.get('givenNameFemale')))
            elif gender in (SCH.Male, 'male', 'm'):
                return Literal(random.choice(dataset_dictionary.get('givenNameMale')))
            else:
                return Literal(
                    random.choice(dataset_dictionary.get('givenNameMale') + dataset_dictionary.get('givenNameFemale')))

        if sh_path == SCH.email:
            given_name = dependencies.get(given_name)
            family_name = dependencies.get(family_name)
            name = dependencies.get(name)

            # Generate email based on given_name, family_name, or name dependencies
            if given_name and family_name:
                return Literal(given_name[0].lower() + "_" + family_name[0].lower() + "@gmail.com")
            elif name:
                email = ""
                for p in name[0].split(' '):
                    email = email + p.lower()
                return Literal(email + "@gmail.com")
            elif given_name:
                return Literal(given_name[0].lower() + "_" + str(random.randrange(100, 1000)) + "@gmail.com")

        # Handle other properties for Person class
        if sh_path == SCH.familyName:
            return Literal(random.choice(dataset_dictionary.get('familyName')))
        if sh_path == SCH.name:
            gender = str(dependencies.get(gender, ["none"])[0])
            if gender in (SCH.Female, 'female', 'f', 'fem'):
                return Literal(random.choice(dataset_dictionary.get('givenNameFemale')) + " " + random.choice(
                    dataset_dictionary.get('familyName')))
            elif gender in (SCH.Male, 'male', 'm'):
                return Literal(random.choice(dataset_dictionary.get('givenNameMale')) + " " + random.choice(
                    dataset_dictionary.get('familyName')))
            else:
                return Literal(
                    random.choice(dataset_dictionary.get('givenNameMale') + dataset_dictionary.get('givenNameFemale')) +
                    " " + random.choice(dataset_dictionary.get('familyName')))
        if sh_path == SCH.streetAddress:
            return Literal(
                "no. " + str(random.randint(1, 100)) + " " + random.choice(dataset_dictionary.get('streetAddress')))
        if sh_path == SCH.gender:
            return Literal(random.choice(dataset_dictionary.get('gender')))
        if sh_path == SCH.jobTitle:
            return Literal(random.choice(dataset_dictionary.get('jobTitle')))

    # Handle cases for Book class
    elif sh_class == SCH.Book:
        # Handle properties for Book class
        if sh_path == SCH.name:
            return Literal(random.choice(dataset_dictionary.get("bookTitle")))
        if sh_path == SCH.award:
            return Literal(random.choice(dataset_dictionary.get('bookAward')))
        if sh_path == SCH.genre:
            return Literal(random.choice(dataset_dictionary.get('bookGenre')))
        if sh_path == SCH.bookEdition:
            return getBookFormat()

    # Handle cases for Movie class
    elif sh_class == SCH.Movie:
        # Handle properties for Movie class
        if sh_path == SCH.name:
            return Literal(random.choice(dataset_dictionary.get("movieTitle")))
        if sh_path == SCH.award:
            return Literal(random.choice(dataset_dictionary.get('movieAward')))
        if sh_path == SCH.genre:
            return Literal(random.choice(dataset_dictionary.get('movieGenre')))

    # Handle cases for TVSeries class
    elif sh_class == SCH.TVSeries:
        # Handle properties for TVSeries class
        if sh_path == SCH.name:
            return Literal(random.choice(dataset_dictionary.get("tvSeriesTitle")))
        if sh_path == SCH.genre:
            return Literal(random.choice(dataset_dictionary.get('movieGenre')))

    return None
