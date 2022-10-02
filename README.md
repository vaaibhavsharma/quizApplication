# Quiz Application
![issues](https://img.shields.io/github/issues/vaaibhavsharma/quizApplication?style=flat-square)
[![GitHub forks](https://img.shields.io/github/forks/vaaibhavsharma/quizApplication)](https://github.com/vaaibhavsharma/quizApplication/network?style=flat-square)
[![GitHub stars](https://img.shields.io/github/stars/vaaibhavsharma/quizApplication)](https://github.com/vaaibhavsharma/quizApplication/stargazers?style=flat-square)
![Python](https://img.shields.io/badge/python-v3.8+-blue.svg?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-3.2.15-blue?style=flat-square&logo=django)
[![GitHub license](https://img.shields.io/github/license/vaaibhavsharma/quizApplication)](https://github.com/vaaibhavsharma/quizApplication/blob/main/LICENSE?style=flat-square)

Django Based Quiz Application having 

- Authentication - user login/Signup with Google email Verification (for organizations) to avoid spam
- Tracking - Tracking every user Inputs with IPAddress for better Judgements
- Custom Error Messages - yes with exclusive gali support 🥲
- All Basic Features Of Quiz APP

## Running Locally 
- Basic Requirement - Python 3.8+

### First Steps

```sh
git clone https://github.com/vaaibhavsharma/quizApplication.git
cd quizApplication
python3 -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

###  Environment Variables
Make file .env inside simpleQuiz2 with following content
```shell
DEBUG=True
SECRET_KEY= #Your Django Project Secret Key 
RECAPTCHA_PUBLIC_KEY= #RECAPTCHA PUBLIC KEY (GOOGLE)
RECAPTCHA_PRIVATE_KEY= #RECAPTCHA PRIVATE KEY (GOOGLE)
```

### Django Configurations

```sh
python manage.py makemigrations userProfile quiz
python manage.py migrate
python manage.py runserver 8080
```

The Project Will now be up and running locally at http://127.0.0.1:8080/

## Make Your First Contribution

1. **star this repository** ⭐, and fork it
   ```
   git clone https://github.com/<your_account>/quizApplication.git
   ```
2. Create a new branch and switch to it.

   ```
   git checkout -b <new_branch_name>
   ```

3. Make changes to the code on that branch and commit.
4. Push the commit to GitHub.

   ```
   git push origin <new_branch_name>
   ```
5. Make a pull request on GitHub.

## Screenshots
![Front Page](/gitassets/frontPage.jpeg "LeaderBoard Page")
![Leaderboard](/gitassets/leaderboardPage.png "LeaderBoard Page")
![Questions Page](/gitassets/questionPage.png "Questions Page")
![Custom Error Messages](/gitassets/customError.png "Questions Page")
![Custom Error Messages 2](/gitassets/customError2.png "Questions Page")
![Hint](/gitassets/customHint.png "Hint")

## License

Distributed under the MIT License. See [LICENSE](/LICENSE) for more information.
