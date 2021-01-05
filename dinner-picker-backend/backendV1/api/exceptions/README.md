# Custom Exceptions

## what are api exceptions?
The problem of using django or python exceptions is that 
    it returns too informative response to users. 
    Response sometimes contain database password<br>

customized api exceptions that are children of APIView will help you
    to return a `good response`, which contains the only information
    that you would users to know. 