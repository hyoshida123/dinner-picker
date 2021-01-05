# Model

Models are data object that will be stored in database & will be used as cache.
All the database stored models should have their own model handler

## Serializer
Model classes are coupled with serializer. Use serializers only when you want to
    create a model directly from the request. Otherwise use DTO to serialization & deserialization.

## Important!
You should add your model to `__init__.py` to migrate

## Important2!
Don't move this directory to a different folder