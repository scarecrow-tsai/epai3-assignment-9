import pytest
import os
import inspect
import re

import session

README_CONTENT_CHECK_FOR = [
    "create_prof",
    "get_mode_bloodgroup",
    "get_mean_location",
    "get_max_age",
    "get_avg_age",
    "prefix_creator",
    "create_company",
]
num_reps = 1000


def test_assignment_readme_exists():
    """Checks if README file exists"""
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_assignment_readme_words():
    """Checks if README file has a minimum of 300 words"""
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert (
        len(readme_words) >= 300
    ), "Make your README.md file interesting! Add atleast 300 words"


def test_assignment_readme_proper_description():
    """Checks if README file has description of all the functions/classes."""
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert (
        READMELOOKSGOOD == True
    ), "You have not described all the functions/classes well in your README.md file"


def test_assignment_readme_file_for_more_than_10_hashes():
    """Checks if README file has proper formatting (minimum of 10 hashes)"""
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_assignment_indentations():
    """ Returns pass if used four spaces for each level of syntactically \
        significant indenting (spaces%4 == 2 and spaces%4 ==0).
    """
    lines = inspect.getsource(session)
    spaces = re.findall("\n +.", lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert (
            len(re.sub(r"[^ ]", "", space)) % 4 == 0
        ), "Your code indentation does not follow PEP8 guidelines"


def test_assignment_function_name_had_cap_letter():
    """test fails if Capital letter(s) used for function names"""
    functions = inspect.getmembers(session, inspect.isfunction)
    for function in functions:
        assert (
            len(re.findall("([A-Z])", function[0])) == 0
        ), "You have used Capital letter(s) in your function names"


def test_mode_bloodgroup():
    """
    Test for the finding the most frequent blood group using tuple and dict.
    """
    test_prof_tuple, test_prof_dict = session.create_prof(num_reps)
    num_runs = 100

    perf_tuples = dict()
    perf_dict = dict()

    session.timed(session.get_mode_bloodgroup, num_runs, perf_tuples)(
        test_prof_tuple, "nt"
    )

    session.timed(session.get_mode_bloodgroup, num_runs, perf_dict)(
        test_prof_dict, "dict"
    )
    assert perf_tuples["get_mode_bloodgroup"] < perf_dict["get_mode_bloodgroup"]


def test_max_age():
    """
    Test for finding max age using tuple and dict.
    """
    test_prof_tuple, test_prof_dict = session.create_prof(num_reps)
    num_runs = 100

    perf_tuples = dict()
    perf_dict = dict()

    session.timed(session.get_max_age, num_runs, perf_tuples)(test_prof_tuple, "nt")
    session.timed(session.get_max_age, num_runs, perf_dict)(test_prof_dict, "dict")
    assert perf_tuples["get_max_age"] < perf_dict["get_max_age"]


def test_mean_location():
    """
    Test for finding the mean location using tuple and dict.
    """
    test_prof_tuple, test_prof_dict = session.create_prof(num_reps)
    num_runs = 100

    perf_tuples = dict()
    perf_dict = dict()

    session.timed(session.get_mean_location, num_runs, perf_tuples)(
        test_prof_tuple, "nt"
    )
    session.timed(session.get_mean_location, num_runs, perf_dict)(
        test_prof_dict, "dict"
    )
    assert perf_tuples["get_mean_location"] < perf_dict["get_mean_location"]


def test_avg_age():
    """
    Test for finding the average age using tuple and dict.
    """
    test_prof_tuple, test_prof_dict = session.create_prof(num_reps)
    num_runs = 100

    perf_tuples = dict()
    perf_dict = dict()

    session.timed(session.get_avg_age, num_runs, perf_tuples)(test_prof_tuple, "nt")
    session.timed(session.get_avg_age, num_runs, perf_dict)(test_prof_dict, "dict")
    assert perf_tuples["get_avg_age"] < perf_dict["get_avg_age"]


def test_company_stock():
    """
    Test for company stock question.
    """

    assert len(session.create_company(100)) == 100
