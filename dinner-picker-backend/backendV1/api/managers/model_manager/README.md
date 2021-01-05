# Model Manager

Each [modelName]_model_manager takes in charge of Save, Get, Delete, Update operations of corresponding models. 
    
## Important
Each model handler should not use other models. 

#Important2.    
    
## What if you have circular imports?
That means your design is wrong. Each model manager only handles CRUD operations of one model.
So if you want to add logic that needs multiple model_manager, put them into a different class.

```
ex)
Update preference by username -> add it into PreferenceManager class.

```  
    
## Components
Model_creator