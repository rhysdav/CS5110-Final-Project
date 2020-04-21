# CS 5110 Final Project: New Graduate Selection
_Rhys Davies, Alec Jackson, Jason Boyd_


### Running our project
Our project was written in Python 3. We have provided a set of test cases which you may use in order to review our code.

To run the test cases:
```
cd src
python3 main.py
```

Tests can be found in the `/test` directory. `src/main.py` is set to run test cases from the `/test/central_agent_test.py` file.  Test cases in this file run our algorithm in its entirety, and may be easily manipulated to show different aspects of our project.

For arm pulls 2 and 3, if a top-k is not provided, one is randomly generated per employer. These k range from 2-12 depending on the arm pull. Additionally, if `num_employers` and `num_candidates` are not specified, `num_employers` defaults to 8 and `num_candidates` defaults to 100.

Please refer to our project report for additional details about our code.
