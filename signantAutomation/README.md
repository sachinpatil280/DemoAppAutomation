# Signant Health Automation Suite

## Instructions to run

Navigate to signantAutomation/runTest folder and run:

```
sh run_all_test.sh
```

##Folder Structure
1. config  
   1. config.robot - This files contains setup and tear down method for robot test cases.
   2. requirements.txt - This file contains all the libraries required for the setup.
2. customLibraries
   1. apiCall.py - This contains custom method for connecting to database and resetting database.
3. pages - This folder contains page objects of respective pages.
4. report - This folder will contain reports of test execution.
5. runTest - This folder contains file to run all test cases (robot and api testcases)
6. testcases - This folder contains all test cases.
7. testdata -  This folder contains test data required for test cases.
8. utils
   1. APIRequest.py - This folder contains all api methods.