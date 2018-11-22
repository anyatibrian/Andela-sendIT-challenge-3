# sendIT
SendIT is a courier service that helps users deliver parcels to different destinations. SendIT
provides courier quotes based on weight categories

## Requirements
- `Python3.6` - programming language that can be used on any modern computer operating system. 
- `Flask` - Python based web micro framework
- `Virtualenv` - Allows you to work on a specific project without worry of affecting other projects.
- `python-pip` - Package management system used to install and manage software packages,its a replacemnt of easy_install

## Functionality
- `create parcel delivery order` Enables user to create create parcel delivery order
- `Get all parcel delivery order` Enables user to view all parcel delivery orders made
- `Get single parcel order` Enables user  to get specific parcel delivery order
- `update parcel order status` Enables  user/admin to update her parcel delivery order status 
- `create new user` Enables  users to create their own accounts
- `login user` Enables  users having accounts to login 
- `login user` Enables  users having accounts to login 
- `get all parcel orders according to the user id`Enables users to get all his/her specific parcel orders 
- `get all parcel orders `Enables admin to get all parcel orders made by users
- `update parcel present location `Enables admin to update the present delivery location



## To view the API on Heroku 
Copy this url paste it in a new tab
```
- https://sendit-challenge-three.herokuapp.com/api/v1/parcels

```

## Installation
First clone this repository
```
$ https://github.com/anyatibrian/Andela-sendIT-challenge-3.git
$ cd andela-sendIT-challenge-3
```
Create virtual environment and install it
```
$ virtualenv venv
$ source/venv/bin/activate
```
Then install all the necessary dependencies
```
pip install -r requirements.txt
```

## Run the application
At the terminal or console type
```
python run.py
```
To run tests run this command at the console/terminal
```
pytest
```
## Versioning
```
This API is versioned using url versioning starting, with the letter 'v'
This is version one"v1" of the API
```
## End Points
|           End Point                              |     Functionality                                   |
|--------------------------------------------------|-----------------------------------------------------|
|     POST  api/v1/auth/signup                     |registers users                                      |  
|     POST  api/v1/auth/login                      |logs in users                                        |   
|     POST  api/v1/parcels                         |creates parcel delivery orders                       |  
|     GET   api/v1/parcels                         |GET all parcel delivery orders                       |
|     GET   api/v1/parcels/parcelID                |get specific parcel orders
|     PUT   api/v1/parcels/parcel_id/destination   |Updates specific parcel delivery destination         |
|     PUT   api/v1/parcels/parcelId/status         |change status of specific delivery order by admin    |
|     PUT   api/v1/parcels/parcelID                |change status of specific delivery order by user     |
|     PUT   api/v1/parcels/ParcelID/presentLocation|change the present location of the parcels


## Contributors
- Anyatibrian

