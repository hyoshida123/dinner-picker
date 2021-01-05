#DTO

### DTO means Data Transfer Object

DTO represents data that is not python object. 

## Rest Framework Serializer vs DTO
- Rest Framework serializer is for converting request to database model.
- DTO is only for converting request dict to object that contains data.

## Util functions
Check api.util.dto_util_functions.py

## Rule
Every DTO that is only used by request (that only does deserialize), it should start with request <br>
In the same way, every DTO that is only used for response should start with response.

`ex) RequestCreateGroupDTO -> used only for request`
`ex) ResponseSuccessMessageDTO -> used only for response`
`ex) UserDTO -> Used for both request & response.`


## Parent
- DTO: parents of all dto
- RequestDTO: DTO that is used only for request
- ResponseDTO: DTO that is used only for response

## Children
- DTO should correspond to the path of endpoints. <br>
`ex) group_dto is used in group endpoints` <br>
- success_failture_DTO. It creates success & failure message.

## API 
### serialize()
Serialize is used to convert dto object to dictionary that is used for Response
```
message = "Verified"
success_DTO = SuccessDTO(message)
return Response(success_DTO.serialize(), status=...)
-> Response with serialized object. 
```
### deserialize()
Deserialize is used to convert request.data dictionary to dto object.<br>
__issue: this can be a class method. I might fix later, but for now, you should instantiate the class to use this function__
```
def get(self, request, format=None):
    group_DTO = GroupDTO().deserialize(request)
-> Then you will have group_DTO that deserializes request.data. 
```

### set_fields
Sometimes you don't want to manually write all the fields. 
    `set_fields` creates fields with default value `None`.
```
EX)
class GroupInfoDTO(DTO):
    self.id = None
    self.name = None
    self.user = None
    self.created = None
    self.preference_settings = None
It is equivalent to
class GroupInfoDTO(DTO):
    self.set_fields('id', 'name', 'user', 'created', 'preference_settings')
```

### sync_with_instance
Currently, DTO is for converting request object to object and dto object to dictionary (for Response).
But sometimes, you want to sync your DTOs with other object like model.<br>

In that moment, you can use sync_with_instance(instance). It syncs all the attribute values in the instance to your DTO.
__sync_with_instance mutates your dto and return self__

EX)<br>
__Your DTO__
```
class GroupInfoDTO(DTO):
    self.set_fields('id', 'name', 'user', 'created', 'preference_settings')
-> Currently all value is None.
```
__Your group model instance__
```
group_instance = GroupModelHandler.get_group_by_groupid(groupid)
group_instance.id = 34
group_instance.name = "sang"
group_instance.user = [12, 3, 4, 5]
group_instance.created = "2018-08-23, 23:12:34"
group_instance.preference_settings = 23 
```
__How to sync__
```
You can sync your DTO and group model instance by
group_info_DTO = GroupInfoDTO()
group_info_DTO.sync_with_instance(group_instance)
```
__In the shell__
```
>>> group_info_DTO.id
34
>>> group_info_DTO.name
"sang"
```

### sync_with_copied_instance
Sometimes you want to sync your DTOs but don't want to lose the original DTO.
In that case sync_with_copied_instance(instance) will not mutate your original DTOs. <br>

It just returns DTO instance that has synced with the given instance but does not mutate the original DTO.

EX) <br>
__Your DTO__
```
class GroupInfoDTO(DTO):
    self.set_fields('id', 'name', 'user', 'created', 'preference_settings')
-> Currently all value is None.
```
__Your group model instance__
```
group_instance = GroupModelHandler.get_group_by_groupid(groupid)
group_instance.id = 34
group_instance.name = "sang"
group_instance.user = [12, 3, 4, 5]
group_instance.created = "2018-08-23, 23:12:34"
group_instance.preference_settings = 23 
```
__How to sync__
```
You can sync your DTO and group model instance by
group_info_DTO = GroupInfoDTO()
copied_group_info_DTO = group_info_DTO.sync_with_copied_instance(group_instance)
```
__In the shell__
```
>>> group_info_DTO.id
None
>>> copied_group_info_DTO.id
34
>>> group_info_DTO.name
None
>>> copied_group_info_DTO.name
"sang"
```

