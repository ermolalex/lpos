1. В файле lato/message.py сделана корректировка:
```
class Message(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)   # todo АЕ - вставлена строка
    
    id: UUID = Field(default_factory=uuid4, alias="id")

    def get_alias(self):
        return self.__class__
```
Без нее выходит ошибка:
>pydantic.errors.PydanticSchemaGenerationError: Unable to generate pydantic-core schema for <class 'mopyx.models.model.<locals>.ModelProxy'>. Set `arbitrary_types_allowed=True` in the model_config to ignore this error or implement `__get_pydantic_core_schema__` on your type to fully support it.
>
>If you got this error by calling handler(<some type>) within `__get_pydantic_core_schema__` then you likely need to call `handler.generate_schema(<some type>)` since we do not call `__get_pydantic_core_schema__` on `<some type>` otherwise to avoid infinite recursion.

