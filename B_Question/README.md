# Question B

The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

## How to Run

To test the code you can run `python test_case.py`, and all the test cases will be executed. 

If needed, a new Python script can be written using the function developed in `version.py`. To use it just import as :

`import version`

and use as `version.compare_version(version1, version2)` in which version1 and version2 are two version strings. The result of the function follows one of the three possible formats:

`version1 is greater than version2`

`version1 is less than version2`

`version1 is equal to version2`


Being the strings version1 and version2 substituted by their real values. 

## Explanation

For this question, I chose to use the `parse_version` function inside `pkg_resources` module, a native module of Python 3.x. This way it was not necessary any installation of third-party modules.

If the string used as input is not a version string following the PEP 808 formation, the code will still recognize and compare it, based on the Legacy format.