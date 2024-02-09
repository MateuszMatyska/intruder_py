# Intruder for Penetration tests and Bug Bounties.

## Functions

* Scan possible routes.
* Scan route with different parameters.

## Running

* clone repo from github `git clone https://github.com/MateuszMatyska/intruder_py.git`
* create virtual env for project (optional) `python3 -m venv /path/to/new/virtual/environment`
* install packages from requirements.txt `pip install -r requirements.txt`
* run script `python3 run_intruder -h`

## Important
For running intruder you have to remember about create file with data which you would like  to test. 
File should contains params with values for example {'login': 'admin', 'password': 'admin123'}.