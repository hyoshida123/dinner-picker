# design-proposal v1.

## frontend
We will use MVC pattern to create a frontend. MVC is a design architecture for maintainable codes. M indicates model, V indicates View, and C indicates controller. 
Always keep in mind that View should be a dumb component because UI unit testing is very hard.

Folder structure should be
model
view
Core (controllers)
Assets
Resources
Storyboards
and files like appDelegate that will be in charge of the whole application.

* Don't forget to create all the REST api call functions in one folder. 

## backend
We will also use MVC pattern for this. Since we would not do server side rendering, our backend will simply have model and controllers. 

Folder structure should follow django structure since django is meant to be MVC. 
