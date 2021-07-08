# Assignment 9

This repo contains files for the 9th assignment on named tuples.

## Lessons Covered

## Assignment

1. Use the Faker (Links to an external site.)library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, and average age.

2. Do the same thing above using a dictionary. Prove that namedtuple is faster.

3. Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value the stock market started at, what was the highest value during the day, and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple.

### create_prof(n: int) -> "namedtuple and dict":

    - Function to create profiles. Both decimal and namedtuple are created.

### get_mode_bloodgroup(obj_col: list, obj_type: str) -> "bloodgroup":

    - Get the bloodgroup with highest frequency from a given
    namedtuple or dict.

### get_mean_location(obj_col: list, obj_type: str) -> "Decimal Coordinates":

    - Get mean x,y of all given coordinates.

### get_max_age(obj_col: list, obj_type: str) -> "Max age":

    - Function to obtain the max age given a namedtuple or dict.

### get_avg_age(obj_col, obj_type: str) -> "Average age":

    - Function to obtain the average age given a namedtuple or dict.

### prefix_creator(name: str) -> str:

    - Function to create unique prefixes given a company name.

### create_company(n: int) -> "namedtuple":

    - Function to create fake stock market data for n companies.

## `test_assignment.py`

This file contains test functions.

### 1. `test_check_doc()`

    - Test to check the check_docstring() function.

### 2. `test_fibonacci()`

    - Test to check the fibonacci() function.

### 3. `test_global_counter()`

    - Test to check the global_counter() function.

### 4. `test_param_counter()`

    - Test to check the param_counter() function.

### 5. `test_check_doc_freevar()`

    - Test to check if free variable exists in check_doc() closure.

### 6. `test_mode_bloodgroup()`

    - Test for the finding the most frequent blood group using tuple and dict.

### 7. test_max_age():

    - Test for finding max age using tuple and dict.

### 8. test_mean_location():

    - Test for finding the mean location using tuple and dict.

### 9. test_avg_age():

    - Test for finding the average age using tuple and dict.

### 10. test_company_stock():

    - Test for company stock question.
