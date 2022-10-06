<p align='center'><img src="/gitassets/logo.png"></p>

![issues](https://img.shields.io/github/issues/vaaibhavsharma/quizApplication?style=flat-square)
[![GitHub forks](https://img.shields.io/github/forks/vaaibhavsharma/quizApplication)](https://github.com/vaaibhavsharma/quizApplication/network?style=flat-square)
[![GitHub stars](https://img.shields.io/github/stars/vaaibhavsharma/quizApplication)](https://github.com/vaaibhavsharma/quizApplication/stargazers?style=flat-square)
![Python](https://img.shields.io/badge/python-v3.8+-blue.svg?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-3.2.15-blue?style=flat-square&logo=django)
[![GitHub license](https://img.shields.io/github/license/vaaibhavsharma/quizApplication)](https://github.com/vaaibhavsharma/quizApplication/blob/main/LICENSE?style=flat-square)

Quizzapp is focused on:

- Authentication - User login/signup with Gmail verification (for organizations) to avoid spam mail
- Tracking - Tracking users with their IP address for identification
- Custom Error Messages - Feel free to customise the wording of quiz errors
- Versatility - All the basic features of a quiz app

## Running Locally

- You should have Python 3.8 or higher installed.

### First Steps

```sh
git clone https://github.com/vaaibhavsharma/quizApplication.git
cd quizApplication
python3 -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

### Environment Variables

Make file .env inside simpleQuiz2 with following content

```sh
DEBUG=True
SECRET_KEY= # Put your Django project secret key here - keep it secret!
RECAPTCHA_PUBLIC_KEY= # Add your reCAPTCHA site key here
RECAPTCHA_PRIVATE_KEY= # Add your reCAPTCHA private key here - keep it secret too!
environment= (prod for production and dev for developement)
# Still in work (for amazon rds)
DB_NAME=
HOST=
PASSWORD=
```

### Django Configurations

```sh
python manage.py makemigrations userProfile quiz
python manage.py migrate
python manage.py runserver 8080
```

Your local instance will now be up and running at http://127.0.0.1:8080/

## Make Your First Contribution

1. **star this repository** ⭐, and fork it
   ```sh
   git clone https://github.com/<your_account>/quizApplication.git
   ```
2. Create a new branch and switch to it.

   ```sh
   git checkout -b <new_branch_name>
   ```

3. Make changes to the code on that branch and commit.
4. Push the commit to GitHub.

   ```sh
   git push origin <new_branch_name>
   ```

5. Make a pull request on GitHub.

## Screenshots

![Front Page](/gitassets/frontPage.jpeg)
![Leaderboard](/gitassets/leaderboardPage.png)
![Questions Page](/gitassets/questionPage.png
![Custom Error Messages](/gitassets/customError.png)
![Custom Error Messages 2](/gitassets/customError2.png)
![Hint](/gitassets/customHint.png)

## License

Distributed under the MIT License. See [LICENSE](/LICENSE) for more information.
