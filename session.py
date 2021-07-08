import random
import datetime
from faker import Faker
from collections import namedtuple


def timed(fn: "function", reps: int, perf_dict: dict) -> "function":
    """
    Decorator to time performance of functions.
    """

    from time import perf_counter

    def inner(*args, **kwargs):
        nonlocal perf_dict
        total_elapsed = 0

        for i in range(reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed = end - start

        avg_runtime = total_elapsed / reps
        perf_dict[fn.__name__] = avg_runtime

        return result

    return inner


def create_prof(n: int) -> "namedtuple and dict":
    """
    Function to create profiles. Both decimal and namedtuple are created.
    """

    fake = Faker()

    Profile = namedtuple("Profile", ["blood_group", "current_location", "birthdate"])

    rand_profiles_tuple = []
    rand_profiles_dict = []

    for i in range(n):
        prof = fake.profile()

        prof_tuple = Profile(
            prof["blood_group"], prof["current_location"], prof["birthdate"]
        )
        prof_dict = {
            "blood_group": prof["blood_group"],
            "current_location": prof["current_location"],
            "birthdate": prof["birthdate"],
        }

        rand_profiles_tuple.append(prof_tuple)
        rand_profiles_dict.append(prof_dict)

    rand_profiles_dict = {i: obj for i, obj in enumerate(rand_profiles_dict)}

    return rand_profiles_tuple, rand_profiles_dict


def get_mode_bloodgroup(obj_col: list, obj_type: str) -> "bloodgroup":
    """
    Get the bloodgroup with highest frequency from a given
    namedtuple or dict.
    """

    if obj_type == "nt":
        val_count = {obj.blood_group: 0 for obj in obj_col}
        for obj in obj_col:
            val = obj.blood_group
            val_count[val] += 1
    else:
        val_count = {obj["blood_group"]: 0 for obj in obj_col.values()}
        for obj in obj_col.values():
            val = obj["blood_group"]
            val_count[val] += 1

    return max(val_count)


def get_mean_location(obj_col: list, obj_type: str) -> "Decimal Coordinates":
    """
    Get mean x,y of all given coordinates.
    """
    val_count = {"x": 0, "y": 0}

    if obj_type == "nt":
        for obj in obj_col:
            val_count["x"] += obj.current_location[0]
            val_count["y"] += obj.current_location[1]
    else:
        for obj in obj_col.values():
            val_count["x"] += obj["current_location"][0]
            val_count["y"] += obj["current_location"][1]

    avg_x = val_count["x"] / len(val_count)
    avg_y = val_count["y"] / len(val_count)

    return avg_x, avg_y


def get_max_age(obj_col: list, obj_type: str) -> "Max age":
    """
    Function to obtain the max age given a namedtuple or dict.
    """
    if obj_type == "nt":
        val_count = {(datetime.date.today() - obj.birthdate).days: 0 for obj in obj_col}
        for obj in obj_col:
            val = (datetime.date.today() - obj.birthdate).days
            val_count[val] += 1
    else:
        val_count = {
            (datetime.date.today() - obj["birthdate"]).days: 0
            for obj in obj_col.values()
        }
        for obj in obj_col.values():
            val = (datetime.date.today() - obj["birthdate"]).days
            val_count[val] += 1

    return max(val_count)


def get_avg_age(obj_col, obj_type: str) -> "Average age":
    """
    Function to obtain the average age given a namedtuple or dict.
    """
    val_count = []

    if obj_type == "nt":
        for obj in obj_col:
            val = (datetime.date.today() - obj.birthdate).days
            val_count.append(val)
    else:
        for obj in obj_col.values():
            val = (datetime.date.today() - obj["birthdate"]).days
            val_count.append(val)

    return sum(val_count) / len(val_count)


def prefix_creator(name: str) -> str:
    """
    Function to create unique prefixes given a company name.
    """
    name = "".join(name.split())
    name = str.upper(name)
    name_len = len(name)
    req_len = 4

    name_char_list = list(name)
    random.shuffle(name_char_list)
    shuffle_name = "".join(name_char_list)

    return shuffle_name[:req_len]


def create_company(n: int) -> "namedtuple":
    """
    Function to create fake stock market data for n companies.
    """
    fake = Faker()
    Company = namedtuple("Company", ["name", "symbol", "opens", "high", "close"])

    rand_compiles_tuple = []

    for i in range(n):
        comp = fake.company()
        opens = random.randrange(1, 4000)
        close = opens * random.uniform(0.8, 1.2)
        mid = opens * random.uniform(0.8, 1.2)
        if mid > close:
            high = mid
        elif mid <= close:
            high = close
        else:
            raise ValueError("Somthing is wrong")

        comp_tuple = Company(comp, prefix_creator(comp), opens, high, close)

        rand_compiles_tuple.append(comp_tuple)

    return rand_compiles_tuple
