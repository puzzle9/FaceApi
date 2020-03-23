# Api

- default success

```json
{
  "code": 200,
  "message": "success"
}
```

- error

```json
{
  "code": 201,
  "message": "error face img"
}
```

# User

## create

`POST /user/create`

### Parameters

name | type | description
:--- | :--- | :--- 
user_id | int | have create or new user

### Response

```json
{
  "code": 200,
  "user_id": 5
}
```

## empty

`delete /user/empty`

- empty user and all save face

### Parameters

name | type | description
:--- | :--- | :--- 
user_id | int | 

## update

`POST /user/face/update`

- add or update default face or delete

### Parameters

name | type | description
:--- | :--- | :--- 
user_id | int | 
file | file | `face img` or `null`

## delete

`delete /user/face/delete`

- delete user_id all save img

### Parameters

name | type | description
:--- | :--- | :--- 
user_id | int | 


# Face

## check

`POST /face/check`

### Parameters

name | type | description
:--- | :--- | :--- 
user_id | int | 
file | file | `face img`

### Response

```json
{
  "code": 200,
  "count": 31,
  "current": 0.4656738424201913,
  "mean": 0.49017777844415206
}
```

