# Notes
This project has been developed using TDD

# Docs
You can find the api documentation in the docs folder

# Prerequisites
- [Docker](https://docs.docker.com/docker-for-mac/install/) 

# How to run using docker-compose
```bash
docker-compose up
```

# How to run migrations
```bash
docker-compose run app sh -c "python manage.py migrate"
```

# How to run tests
```bash
docker-compose run app sh -c "python manage.py test"
```

# How to run commands inside the docuker container
```bash
docker-compose run --rm app sh -c "[command]"
```

# How to check using Postman
You can import my Postman collection, you will find it in the root of the project. In the collection, you'll see shortcuts to the different endpoints. Don't forgot to override the token to access to private endpoints.