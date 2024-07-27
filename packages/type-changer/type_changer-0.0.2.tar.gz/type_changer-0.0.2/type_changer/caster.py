# Copyright (C) 2024  All Rights Reserved

from pydantic import BaseModel
from types import GenericAlias, UnionType
from pydantic._internal._model_construction import ModelMetaclass

from type_changer import valid


class Caster:

    def __init__(self, pymodel:BaseModel, data:dict) -> None:

        val = valid()
        self.pymodel = pymodel.model_construct(**data)
        self.data = data
        try:
            val.is_valid(self.pymodel, data, False)
        except (AssertionError, Exception) as e:
            print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
            exit()

    
    def __change2(self, annot_data:GenericAlias, data:dict, key:str):
        for i in annot_data.__args__:
            if isinstance(i, ModelMetaclass):
                self.__change(i, data, key, True, annot_data)
            
            elif isinstance(i, UnionType):
                cnt = 0
                flt_types = [k for k in i.__args__ if not k is type(None)]
                for k in flt_types:
                    try:
                        data[key] = annot_data.__origin__([k(d) for d in data[key]])
                        break
                    except:
                        cnt += 1
                    
                if cnt == len(flt_types):
                    if type(None) in i.__args__:
                        data[key] = annot_data.__origin__([None for _ in data[key]])

            elif isinstance(i, type):
                data[key] = annot_data.__origin__([i(d) for d in data[key]])
        


    def __change(self, data_model:ModelMetaclass, data:dict, _key:str|None, iter:bool, annot_type:GenericAlias | None):
        
        if iter:
            temp = []

            for j in data[_key]:
                for key, val in data_model.model_fields.items():
                    
                    if isinstance(val.annotation, GenericAlias):
                        self.__change2(val.annotation, data, key)
                    else:
                        j[key] = val.annotation(j[key])

                temp.append(j)

            data[_key] = annot_type.__origin__(temp)
        
        else:
            for key, val in data_model.model_fields.items():

                if isinstance(val.annotation, GenericAlias):
                    self.__change2(val.annotation, data, key)

                elif isinstance(val.annotation, ModelMetaclass):
                    self.__change(val.annotation, data[key], key, False, None)

                elif isinstance(val.annotation, UnionType):
                    cnt = 0
                    flt_types = [i for i in val.annotation.__args__ if not i is type(None)]
                    
                    for i in flt_types:
                        try:
                            data[key] = i(data[key])
                            break
                        except:
                            cnt += 1
                        
                    if cnt == len(flt_types):
                        if type(None) in val.annotation.__args__:
                            data[key] = None

                else:
                    data[key] = val.annotation(data[key])



    def cast(self):
        try:
            self.__change(self.pymodel, self.data, None, False, None)
            return self.data
        except Exception as e:
            print("\nAn Error acquired. \033[91m\033[1m\033[4mError\033[00m:", e)
            exit()