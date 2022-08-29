pip install -r "../config/requirements.txt"


dir=$PWD
cd "$dir"/../testcases || exit

robot --outputdir ../report/  registration.robot login.robot
pytest -s -v --html=../report/apiReport.html
