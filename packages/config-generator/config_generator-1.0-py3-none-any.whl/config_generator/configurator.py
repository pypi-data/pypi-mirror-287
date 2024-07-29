import os, sys, json
from pydantic import BaseModel, ValidationError

class Configurator(BaseModel):
    def __init__(self, __path__ : str = None, **kwargs) -> None:
        super().__init__(**kwargs)

        if __path__:
            self.__load_self(path = __path__)

    def __load_self(self, path : str) -> None:
        model_dump = self.model_dump()

        if os.path.exists(path):
            model_dump.update(self.__load_json(path = path))

        try:
            configurator = self.__class__(**model_dump)
            self.__dict__ = configurator.__dict__

            model_dump = self.model_dump()

        except ValidationError as e:
            sys.exit(str(e))

        finally:
            self.__rewrite_json(path = path, obj = model_dump)

    def __load_json(self, path : str) -> dict:
        with open(path, 'r', encoding = 'utf-8') as file:
            return json.load(file)
        
    def __rewrite_json(self, path : str, obj : dict) -> None:
        with open(path, 'w', encoding = 'utf-8') as file:
            json.dump(obj, file, indent = 4, ensure_ascii = True)