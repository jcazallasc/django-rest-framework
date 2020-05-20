# Transactions
Supports creating, listing, and custom summaries.

## Create a new transaction
This endpoint allows for creation in bulk mode. Means, it can receive a list of the indicated parameters.

**Request**:

`POST` `/transaction/create/`

Parameters:

Name       | Type           | Required | Description
-----------|----------------|----------|------------
reference  | string, unique | Yes      | The transaction's reference
account    | string         | Yes      | The transaction's account
date       | string         | Yes      | The transaction's date
amount     | string         | Yes      | The transaction's category. If type is inflow, amount must be positive. If type is outflow, amount must be negative
type       | string         | Yes      | The transaction's type. Options: inflow or outflow
category   | string         | Yes      | The transaction's category

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
201 Created

{
  "reference": "000069",
  "account": "C00001",
  "date": "2020-12-12",
  "amount": "55.00",
  "type": "inflow",
  "category": "groceries"
}
```

## Get transaction list

**Request**:

`GET` `/transaction/list`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

[
  {
    "reference": "000069",
    "account": "C00001",
    "date": "2020-12-12",
    "amount": "55.00",
    "type": "inflow",
    "category": "groceries"
  }
]
```

## Get summary by account

**Request**:

`GET` `/transaction/summary-by-account`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

[
 {"account": "C00099", "balance": "1738.87", "total_inflow": "2500.72", "total_outflow": "-761.85"},
 {"account": "S00012", "balance": "150.72", "total_inflow": "150.72", "total_outflow": "0.00"},
]
```

## Get summary by category

**Request**:

`GET` `/transaction/summary-by-category`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "inflow": {
    "salary": "2500.72", "savings": "150.72"
  },
  "outflow": {
    "groceries": "-51.13", "rent": "-560.00", "transfer": "-150.72"
  }
}
```

