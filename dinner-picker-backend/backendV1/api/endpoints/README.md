# endpoint

Endpoint classes are children of Rest Framework's View classes. 
    It receives request from external resources, process, and respond.

## Rule
Each endpoint starting with same path should be in the same directory.
EX)
```
authentication/signUp and authentication/login starts with same path authentictaion.
Then put both of class into authentication directory.
```    
    
## IMPORTANT
endpoint classes should not do more than receiving request, process, and respond. 
    That being said, saving user account, convert dictionary to classes should not
    happen in here. They should be in separated classes and used in endpoint classes.
    
EX)
```
Instead of doing,
username = request.data["username"]
do,
username = get_query_value_from(request, "username")
```
The first case exposes the implementation logic. The second one hides it.
    
## parent
- APIView: Rest Framework's view classes. It would be parents of most endpoint classes.

## children
- snippet_views: example classes to show how to create endpoints
- group: endpoint starting with group
- authentication: endpoint starting with authentication
- settings: endpoint starting with settings
- suggest_restaurants_endpoint: endpoint starting with suggestion
