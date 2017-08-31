# Project Title

Restful Surveys App

## Scope

Surveys on soft-drinks people drink in given locations for the purpose of
analysis 


### Running the Project
Deployed instance available at 

```
http://107.170.39.149/
```

### Rest Endpoints

```
http://107.170.39.149/api/drinks/ 			[GET]
http://107.170.39.149/api/locations/			[GET]
http://107.170.39.149/api/surveys/			[GET]
```

### Curl API calls

[GET AUTH TOKEN]

```
curl --request POST --url http://107.170.39.149/api/login --header 'content-type: application/json' --data '{"username": "YOUR_USERNAME", "password": "YOUR_PASSWORD"}'
```

[ GET ]

```
curl -H "Content-Type: application/json" -H "Authorization: Token YOUR_AUTH_TOKEN" http://107.170.39.149/api/drinks/
curl -H "Content-Type: application/json" -H "Authorization: Token YOUR_AUTH_TOKEN" http://107.170.39.149/api/locations/
curl -H "Content-Type: application/json" -H "Authorization: Token YOUR_AUTH_TOKEN" http://107.170.39.149/api/surveys/
```

[ RETRIEVE ]

```
curl -H "Content-Type: application/json" -H "Authorization: Token YOUR_AUTH_TOKEN" http://107.170.39.149/drinks/1/
curl -H "Content-Type: application/json" -H "Authorization: Token YOUR_AUTH_TOKEN" http://107.170.39.149/api/locations/1/
curl -H "Content-Type: application/json" -H "Authorization: Token YOUR_AUTH_TOKEN" http://107.170.39.149/api/surveys/1/
```

[ POST ]

```
curl -H "Content-Type: application/json" -H "Authorization: Token YOUR_AUTH_TOKEN" -X POST -d '{"drink":"YOUR_DRINK"}' http://107.170.39.149/api/drinks/

curl -H "Content-Type: application/json" -H "Authorization: Token YOUR_AUTH_TOKEN" -X POST -d '{"location":"YOUR_LOCATION"}' http://107.170.39.149/api/locations/

curl -H "Content-Type: application/json" -H "Authorization: Token YOUR_AUTH_TOKEN" -X POST -d '{"research_person":"NAME","research_area":LOCATION_ID,"drink":DRINK_ID}' http://localhost:8000/api/surveys/
```

[ DELETE ]
```
curl -H "Content-Type: application/json" -H "Authorization: Token YOUR_AUTH_TOKEN" -X DELETE  http://107.170.39.149/api/drinks/4/
curl -H "Content-Type: application/json" -H "Authorization: Token YOUR_AUTH_TOKEN" -X DELETE  http://107.170.39.149/api/locations/4/
curl -H "Content-Type: application/json" -H "Authorization: Token YOUR_AUTH_TOKEN" -X DELETE  http://107.170.39.149/api/surveys/4/
```
## Powered by

* [Django](https://www.djangoproject.com/) - Web framework
* [Rest] (http://www.django-rest-framework.org/) - Rest Framework

