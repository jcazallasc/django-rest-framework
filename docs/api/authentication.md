# Authentication
For clients to authenticate, the token key should be included in the Authorization HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

## Retrieving Token

**Request**:

`POST` `user/token/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
email      | string | Yes      | The user's email
password   | string | Yes      | The user's password


**Response**:
```json
{ 
    "token" : "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" 
}
```
