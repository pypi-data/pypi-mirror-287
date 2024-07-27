from typing import Literal, TypeVar, Generic
from dataclasses import dataclass

A = TypeVar('A')

@dataclass
class Skip:
  idx: int       
  tag: Literal['skip'] = 'skip'

@dataclass
class Insert(Generic[A]):
  idx: int
  value: A = None # type: ignore
  tag: Literal['insert'] = 'insert'
  
Edit = Insert[A] | Skip
  
@dataclass
class Inserted(Generic[A]):
  value: A