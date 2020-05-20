# Users
Supports creating and listing

## Register a new user account

**Request**:

`POST` `/users/create`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
email      | string | Yes      | The username for the new user.
password   | string | Yes      | The password for the new user account.
name       | string | Yes      | The user's given name.
age        | string | Yes      | The user's family name.

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created

{
  "id": 1,
  "email": "jcazallasc@gmail.com",
  "name": "Javier",
  "age": 30,
}
```

## Get user detail

**Request**:

`GET` `/users/detail`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": "1",
  "email": "jcazallasc@gmail.com",
  "name": "Javier",
  "age": "30",
}
```
