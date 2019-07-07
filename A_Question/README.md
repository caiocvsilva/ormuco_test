# Question A

Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).



## How to Run

To test the code you can run `python test_case.py`, and all the test cases will be executed. 

If needed, a new Python script can be written using the function developed in `overlap.py`. To use it just import as :

`import A_Question.overlap as overlap`

and use as `overlap.check_overlap(line1,line2)` in which line1 and line2 are two tuples, representing ranges. The result of the function is True or False, indicating the existence of overlap.

## Explanation

To solve this question only some cases needed to be adressed:
- Overlap:
  - Both ranges are equal
  - The start of the first range is inside the second range
  - The start of the second range is inside the first range
- No Overlap:
  - Other cases

Before doing the comparasion I forced the start and end of each range to be corrected (min, max), not needing the input to be sorted.