# SF-test-case
Test project for Solution Factory employer 

### Setup
Ensure that you have at least Python 3.8 installed  
To setup this project execute the following code:
```shell
python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

Now app is ready to start up, but you also need to create as user:  

`python manage.py createsuperuser`  

Then prompt username, password and repeat password  
Now you can run app with  

`python manage.py runserver`

## API description
### Auth
To get bearer token make this request:  
```shell
curl --location --request POST 'http://localhost:8000/api/v1/auth' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'username=<your username>>' \
--data-urlencode 'password=<your password>'
```

### Polls
#### Manage polls  

#### POST: http://localhost:8000/api/v1/polls/
**Requires auth with Bearer token**  

Required fields:  
`title`

Optional fields:  
`description`  

Response format:
```json lines
{
    "id": 2,
    "title": "New poll",
    "description": null,
    "date_created": "2021-11-08T23:44:33.775459Z",
    "questions": []
}
```
#### GET
http://localhost:8000/api/v1/polls/ID/  
Get all polls if ID is missing or poll with specified id  

Response format:
```json lines
[
    {
        "id": 2,
        "title": "New poll",
        "description": null,
        "date_created": "2021-11-08T23:44:33.775459Z",
        "questions": []
    }
]
```
```json lines
{
    "id": 2,
    "title": "New poll",
    "description": null,
    "date_created": "2021-11-08T23:44:33.775459Z",
    "questions": []
}
```

#### PATCH / PUT http://localhost:8000/api/v1/polls/ID/
**Requires auth with Bearer token**    
Change given poll 

Optional fields:  
`description`, `title`  

Response format:  
```json lines
{
    "id": 2,
    "title": "New poll patched",
    "description": null,
    "date_created": "2021-11-08T23:49:01.085238Z",
    "questions": []
}
```

#### DELETE http://localhost:8000/api/v1/polls/ID/
**Requires auth with Bearer token**    
Delete given poll  
No fields required, empty response with 204 status is returned

### Questions  
#### Manage questions of polls

#### POST: http://localhost:8000/api/v1/questions/
**Requires auth with Bearer token**  

Required fields:  
`poll_id`, `type`, `text`

- `poll_id` is id returned after success poll creation
- `text` is a question's text
- `type` is a question type. Available values: `TEXT`, `SINGLE_CHOICE`, `NULTIPLE_CHOICE`

Response format:
```json lines
{
    "id": 6,
    "text": "?????????????? ???????????????",
    "type": "TEXT",
    "answers": [],
    "poll_id": 1
}
```
#### GET http://localhost:8000/api/v1/questions/ID/  
Get all questions if ID is missing or question with specified id  

Response format:
```json lines
[
    {
        "id": 3,
        "text": "?????????? ???????????",
        "type": "MULTIPLE_CHOICE",
        "answers": [
            {
                "id": 1,
                "text": "??????????",
                "question": 3,
                "voter": 1
            }
        ],
        "poll_id": 1
    },
    {
        "id": 6,
        "text": "?????????????? ???????????????",
        "type": "TEXT",
        "answers": [],
        "poll_id": 1
    }
]
```
```json lines
{
    "id": 2,
    "title": "New poll",
    "description": null,
    "date_created": "2021-11-08T23:44:33.775459Z",
    "questions": []
}
```

#### PATCH / PUT http://localhost:8000/api/v1/questions/ID/
**Requires auth with Bearer token**    
Change given question

Optional fields:  
`type`, `text`

Response format:  
```json lines
{
    "id": 1,
    "text": "???????????? ????????",
    "type": "SINGLE_CHOICE",
    "answers": [],
    "poll_id": 1
}
```

#### DELETE http://localhost:8000/api/v1/questions/ID/
**Requires auth with Bearer token**  
Delete given question  
No fields required, empty response with 204 status is returned

### Answers
#### POST: http://localhost:8000/api/v1/polls/  
Voting in the given poll

Required fields:  
`text`, `question`

Optional fields:  
`voter`

- `text` is a question answer 
- `question` is a question id 
- `voter` is integer ID of someone who votes. Can be `null`

Response format:
```json lines
{
    "id": 8,
    "text": "??????????",
    "question": 3,
    "voter": 1
}
```
#### GET http://localhost:8000/api/v1/answers/ID/  
Get all answers if `ID` is missing or answer with specified id  

Response format:
```json lines
[
    {
        "id": 6,
        "text": "??????????",
        "question": 3,
        "voter": 1
    },
    {
        "id": 7,
        "text": "??????????",
        "question": 3,
        "voter": 1
    },
    {
        "id": 8,
        "text": "??????????",
        "question": 3,
        "voter": 1
    }
]
```
```json lines
{
    "id": 2,
    "text": "??????????",
    "question": 3,
    "voter": 1
}
```

#### PATCH / PUT http://localhost:8000/api/v1/answers/ID/
**Requires auth with Bearer token**    
After creating answer is not editable anymore unless you are admin

#### DELETE http://localhost:8000/api/v1/answers/ID/
**Requires auth with Bearer token**    
Delete given answer  
No fields required, empty response with 204 status is returned

### Voters
#### POST: http://localhost:8000/api/v1/voters/
**Requires auth with Bearer token**    
You can easily populate your table with new empty voters...but for what? 

Required fields:  
`id` 

Response format:
```json lines
{
    "id": 5,
    "voted_polls": []
}
```
#### GET http://localhost:8000/api/v1/voters/ID/  
Get all voters if `ID` is missing or voter with specified id  

Response format:
```json lines
[
    {
        "id": 1,
        "voted_polls": [
            {
                "id": 1,
                "title": "??????????",
                "description": null,
                "date_created": "2021-11-08T22:26:07.681122Z",
                "questions": [
                    {
                        "id": 3,
                        "text": "?????????? ???????????",
                        "type": "MULTIPLE_CHOICE",
                        "answers": [
                            {
                                "id": 1,
                                "text": "??????????",
                                "question": 3,
                                "voter": 1
                            },
                            {
                                "id": 2,
                                "text": "?????? ????????????????",
                                "question": 3,
                                "voter": 3
                            },
                            {
                                "id": 3,
                                "text": "?????????? ????????????",
                                "question": 3,
                                "voter": 1
                            },
                            {
                                "id": 4,
                                "text": "?????????? ??????????",
                                "question": 3,
                                "voter": 1
                            },
                            {
                                "id": 5,
                                "text": "???????? ??????????",
                                "question": 3,
                                "voter": 1
                            }
                        ],
                        "poll_id": 1
                    },
                    {
                        "id": 4,
                        "text": "???? ????????",
                        "type": "TEXT",
                        "answers": [],
                        "poll_id": 1
                    }
                ]
            }
        ]
    },
    {
        "id": 3,
        "voted_polls": []
    }
]
```
```json lines
{
    "id": 3,
    "voted_polls": []
}
```

#### PATCH / PUT http://localhost:8000/api/v1/voters/ID/
**Requires auth with Bearer token**    
Change given voter

Optional fields:  
`id`  

#### I do not think that patching voter directly is a good idea

#### DELETE http://localhost:8000/api/v1/voter/ID/
**Requires auth with Bearer token**    
Delete given voter  
No fields required, empty response with 204 status is returned