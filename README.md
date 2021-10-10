# fast-login
login service with fastAPI

python version: 3.9.7

ENV:
    - python 3.7
    - fastapi
    - mongodb
    - redis

PRE-INSTALL: (libs)
    - pip install fastapi
    - pip install uvicorn

    - pip install pytest
    - pip install request

    - pip install pymongo
    - pip install redis

    - pip install "python-jose[cryptography]"
    - pip install "passlib[bcrypt]"

RUN: uvicorn app.main:app --reload


Example:
- 
    Step1. verify Phone with SMS code
    - localhost:8000/api/auth/verify
        { phone: "010-1111-1111" }
        <RESPONSE> : "verify_token"

    Step2. Signup with SMS code & token
    - localhost:8000/api/auth/signup
        {
            "email": "myEmail1113@Email.com",
            "nickname": "Kyo",
            "password": "mypassword",
            "name": "test",
            "phone": "111222231113",
            "verify_token": <YOUR VERIFY TOKEN>,
            "code" : "0000" --> DUMMY SMS verify code
        }

    Step3. SignIn
    - localhost:8000/api/auth/signin
    {
        "id": <ID or Email or Phone number>,
        "password": "mypassword"
    }

    Step4. Get my info
    - localhost:8000/api/users/{my user id}
