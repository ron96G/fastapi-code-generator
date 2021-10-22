# generated by fastapi-codegen:
#   filename:  oas_response_reference.yaml
#   timestamp: 2020-06-19T00:00:00+00:00

from __future__ import annotations

from typing import List, Optional

from fastapi import FastAPI

from .models import Pet

app = FastAPI(
    version='1.0.0',
    title='Swagger Petstore',
    license={'name': 'MIT'},
    description='This description is for testing\nmulti-line\ndescription\n',
    servers=[{'url': 'http://petstore.swagger.io/v1'}],
)


@app.get('/pets', response_model=List[Pet])
def list_pets(limit: Optional[int] = 0) -> List[Pet]:
    """
    List all pets
    """
    pass
