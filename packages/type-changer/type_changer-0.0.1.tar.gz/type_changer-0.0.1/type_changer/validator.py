# Copyright (C) 2024  All Rights Reserved

from pydantic import BaseModel
from types import GenericAlias, UnionType
from pydantic._internal._model_construction import ModelMetaclass


class valid:
    def __init__(self) -> None:
    
        self.get_cast_class  = {"int": [float, int, str, bool],
                                "float": [int, str, float, bool],
                                "bool": [int, str, float, bool],
                                "str": [list, tuple, int, float, bool, str],
                                "list": [list, tuple, str],
                                "tuple": [list, tuple, str]}
        

    def __type_checker(self, annot_model, val):
        if isinstance(val, str) and annot_model in [float, int]:
            assert val.replace(".", "").isdigit(), f"Data-type casting for the input type 'str' to '{annot_model.__name__}' does not possible for the given combination."

        else:
            if annot_model is str :
                return
            
            avail_cast = self.get_cast_class[type(val).__name__]
            assert annot_model in avail_cast, f"Data-type casting for the input type '{type(val).__name__}' to '{annot_model.__name__}' does not possible.\n\nAvailable casting type for {type(val).__name__} are [{', '.join([i.__name__ for i in avail_cast])}, None]"



    def __union_checker(self, annot_model, val):
        avail_cast = self.get_cast_class[type(val).__name__]
        flt_types = [i for i in annot_model.__args__ if not i is type(None)]
        cnt = 0
        for i in flt_types:
            try:
                if isinstance(val, str) and i in [float, int]:
                    assert val.replace(".", "").isdigit(), f"Data-type casting for the input type 'str' to '{annot_model.__name__}' does not possible for the given combination."
                if i is str:
                    break
                assert i in avail_cast, "break occured."
                break
            except:
                cnt += 1
        if cnt == len(flt_types):
            assert type(None) in annot_model.__args__, f"Data-type casting for the input type '{type(val).__name__}' to any other given type of '{annot_model}' does not possible.\n\nAvailable casting type for {type(val).__name__} are [{', '.join([i.__name__ for i in avail_cast])}, None]"



    def is_valid(self, pymodel:BaseModel, data:dict, iter:bool):

        assert isinstance(pymodel,(BaseModel, ModelMetaclass)), "pymodel must be a pydantic Basemodel."
        assert isinstance(iter, bool), "iter must be a bool."

        if iter:
            for dat in data:
                for key, val in pymodel.model_fields.items():

                    if isinstance(val.annotation, GenericAlias):
                        avail_cast = self.get_cast_class[type(dat[key]).__name__]
                        assert val.annotation.__origin__ in avail_cast, f"Data-type casting for the input type '{type(dat[key]).__name__}' to '{val.annotation.__origin__.__name__}' does not possible.\n\nAvailable casting type for {type(dat[key]).__name__} are [{', '.join([i.__name__ for i in avail_cast])}, None]"
                        
                        if isinstance(val.annotation.__args__[0], ModelMetaclass):
                            self.is_valid(val.annotation.__args__[0], dat[key], True)
                        
                        else:
                            for k in dat[key]:
                                if isinstance(val.annotation.__args__[0], UnionType):
                                    self.__union_checker(val.annotation.__args__[0], k)
                                else:
                                    self.__type_checker(val.annotation.__args__[0], k)

                    elif isinstance(val.annotation, UnionType):
                        self.__union_checker(val.annotation, dat[key])

                    else:
                        self.__type_checker(val.annotation, dat[key])

        else:

            for key, val in pymodel.model_fields.items():

                if isinstance(val.annotation, GenericAlias):
                    avail_cast = self.get_cast_class[type(data[key]).__name__]
                    assert val.annotation.__origin__ in avail_cast, f"Data-type casting for the input type '{type(data[key]).__name__}' to '{val.annotation.__origin__.__name__}' does not possible.\n\nAvailable casting type for {type(data[key]).__name__} are [{', '.join([i.__name__ for i in avail_cast])}, None]"
                    
                    if isinstance(val.annotation.__args__[0], ModelMetaclass):
                        self.is_valid(val.annotation.__args__[0], data[key], True)
                    
                    else:
                        for k in data[key]:
                            if isinstance(val.annotation.__args__[0], UnionType):
                                self.__union_checker(val.annotation.__args__[0], k)
                            else:
                                self.__type_checker(val.annotation.__args__[0], k)

                elif isinstance(val.annotation, UnionType):
                    self.__union_checker(val.annotation, data[key])
                
                elif isinstance(val.annotation, ModelMetaclass):
                    self.is_valid(val.annotation, data[key], False)

                else:
                    self.__type_checker(val.annotation, data[key])