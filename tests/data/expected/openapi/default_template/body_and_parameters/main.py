# generated by fastapi-codegen:
#   filename:  body_and_parameters.yaml
#   timestamp: 2020-06-19T00:00:00+00:00

from __future__ import annotations

from typing import List, Optional

from fastapi import FastAPI, Path, Query
from starlette.requests import Request

from .models import (
    Pet,
    PetForm,
    UserGetResponse,
    UserPostRequest,
    UsersGetResponse,
    UsersPostRequest,
)

app = FastAPI(
    version='1.0.0',
    title='Swagger Petstore',
    license={'name': 'MIT'},
    description='This description is for testing\nmulti-line\ndescription\n',
    servers=[{'url': 'http://petstore.swagger.io/v1'}],
)


@app.post('/bar', response_model=None)
def post_bar(request: Request) -> None:
    """
    Create a bar
    """
    pass


@app.get('/foo', response_model=str)
def get_foo(foo: Optional[str] = None) -> str:
    pass


@app.post('/food', response_model=None)
def post_food(body: str) -> None:
    """
    Create a food
    """
    pass


@app.get('/food/{food_id}', response_model=List[int])
def show_food_by_id(
    food_id: str, message_texts: Optional[List[str]] = None
) -> List[int]:
    """
    Info for a specific pet
    """
    pass


@app.get('/pets', response_model=List[Pet])
def list_pets(
    limit: Optional[int] = 0,
    home_address: Optional[str] = Query('Unknown', alias='HomeAddress'),
    kind: Optional[str] = 'dog',
) -> List[Pet]:
    """
    List all pets
    """
    pass


@app.post('/pets', response_model=None)
def post_pets(body: PetForm) -> None:
    """
    Create a pet
    """
    pass


@app.get('/pets/{pet_id}', response_model=Pet)
def show_pet_by_id(pet_id: str = Path(..., alias='petId')) -> Pet:
    """
    Info for a specific pet
    """
    pass


@app.put('/pets/{pet_id}', response_model=None)
def put_pets_pet_id(
    pet_id: str = Path(..., alias='petId'), body: PetForm = None
) -> None:
    """
    update a pet
    """
    pass


@app.get('/user', response_model=UserGetResponse)
def get_user() -> UserGetResponse:
    pass


@app.post('/user', response_model=None)
def post_user(body: UserPostRequest) -> None:
    pass


@app.get('/users', response_model=List[UsersGetResponse])
def get_users() -> List[UsersGetResponse]:
    pass


@app.post('/users', response_model=None)
def post_users(body: List[UsersPostRequest]) -> None:
    pass


@app.post('/{ue_id}/sdm-subscriptions', response_model=None)
def subscribe(ue_id: str = Path(..., alias='ueId'), body: Pet = ...) -> None:
    """
    subscribe to notifications
    """
    pass
