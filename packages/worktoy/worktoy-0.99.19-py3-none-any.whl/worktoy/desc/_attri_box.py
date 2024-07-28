"""AttriBox subclasses the TypedDescriptor class and incorporates
syntactic sugar for setting the inner class, and for the inner object
creation. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Callable, Never, Any

from icecream import ic

from worktoy.desc import TypedDescriptor, Instance, Owner
from worktoy.parse import maybe
from worktoy.text import typeMsg, monoSpace

if sys.version_info.minor < 11:
  from typing_extensions import Self
else:
  from typing import Self

ic.configureOutput(includeContext=True)

if TYPE_CHECKING:
  pass
else:
  AttriClass = object


class AttriBox(TypedDescriptor):
  """AttriBox subclasses the TypedDescriptor class and incorporates
  syntactic sugar for setting the inner class, and for the inner object
  creation. """

  __positional_args__ = None
  __keyword_args__ = None
  __get_callbacks__ = None
  __set_callbacks__ = None
  __del_callbacks__ = None

  def _getGetCallbacks(self) -> list[Callable]:
    """Getter-function for list of functions to be called on get."""
    if self.__get_callbacks__ is None:
      self.__get_callbacks__ = []
    return self.__get_callbacks__

  def _getSetCallbacks(self) -> list[Callable]:
    """Getter-function for list of functions to be called on set."""
    if self.__set_callbacks__ is None:
      self.__set_callbacks__ = []
    return self.__set_callbacks__

  def _getDelCallbacks(self) -> list[Callable]:
    """Getter-function for list of functions to be called on del."""
    if self.__del_callbacks__ is None:
      self.__del_callbacks__ = []
    return self.__del_callbacks__

  def notifyGet(self, callMeMaybe: Callable) -> Callable:
    """Adds given callable to list of callables to be notified on get."""
    self._getGetCallbacks().append(callMeMaybe)
    return callMeMaybe

  def notifySet(self, callMeMaybe: Callable) -> Callable:
    """Adds given callable to list of callables to be notified on set."""
    self._getSetCallbacks().append(callMeMaybe)
    return callMeMaybe

  def notifyDel(self, callMeMaybe: Callable) -> Callable:
    """Adds given callable to list of callables to be notified on del."""
    self._getDelCallbacks().append(callMeMaybe)
    return callMeMaybe

  def ONGET(self, callMeMaybe: Callable) -> Callable:
    """Decorator for adding a function to the get callbacks."""
    return self.notifyGet(callMeMaybe)

  def ONSET(self, callMeMaybe: Callable) -> Callable:
    """Decorator for adding a function to the set callbacks."""
    return self.notifySet(callMeMaybe)

  def ONDEL(self, callMeMaybe: Callable) -> Callable:
    """Decorator for adding a function to the del callbacks."""
    return self.notifyDel(callMeMaybe)

  def __init__(self, *args, **kwargs) -> None:
    """Initializes the AttriBox instance. """
    TypedDescriptor.__init__(self, *args, **kwargs)
    if not kwargs.get('_root', False):
      e = """The AttriBox class should not be instantiated directly!"""
      raise TypeError(e)
    if not args:
      e = """The inner class must be provided. """
      raise TypeError(e)
    innerClass = args[0]
    if not isinstance(innerClass, type):
      e = typeMsg('innerClass', innerClass, type)
      raise TypeError(e)
    self._setInnerClass(innerClass)

  @classmethod
  def __class_getitem__(cls, innerClass: type) -> Self:
    """Syntactic sugar for setting the inner class. """
    return cls(innerClass, _root=True)

  def __call__(self, *args, **kwargs) -> Self:
    """Syntactic sugar for creating an instance of the inner class. """
    self.__positional_args__ = args
    self.__keyword_args__ = kwargs
    return self

  def _getArgs(self, instance: object) -> list:
    """Returns the arguments used to create the inner object. """
    out = []
    for arg in maybe(self.__positional_args__, []):
      if arg is Instance:
        out.append(instance)
      elif arg is Owner:
        out.append(self._getFieldOwner())
      else:
        out.append(arg)
    return out

  def _getKwargs(self, instance: object) -> dict:
    """Returns the keyword arguments used to create the inner object. """
    out = {}
    for (key, value) in maybe(self.__keyword_args__, {}).items():
      if value is Instance:
        out[key] = instance
      elif value is Owner:
        out[key] = self._getFieldOwner()
      else:
        out[key] = value
    return self.__keyword_args__

  def _createInnerObject(self, instance: object) -> object:
    """Creates an instance of the inner class. """
    innerClass = self.getInnerClass()
    args, kwargs = self._getArgs(instance), self._getKwargs(instance)
    innerObject = innerClass(*args, **kwargs)
    if TYPE_CHECKING:
      assert isinstance(innerObject, AttriClass)
    innerObject.setOuterBox(self)
    innerObject.setOwningInstance(instance)
    innerObject.setFieldOwner(self._getFieldOwner())
    innerObject.setFieldName(self._getFieldName())
    return innerObject

  def __str__(self, ) -> str:
    try:
      fieldName = self._getFieldName()
      ownerName = self._getFieldOwner().__name__
    except AttributeError as attributeError:
      if 'has not been assigned to a field' not in str(attributeError):
        raise attributeError
      ownerName = '(TBD)'
      fieldName = '(TBD)'
    innerName = self.getInnerClass().__name__
    return '%s.%s: %s' % (ownerName, fieldName, innerName)

  def __repr__(self, ) -> str:
    try:
      fieldName = self._getFieldName()
    except AttributeError as attributeError:
      if 'has not been assigned to a field' not in str(attributeError):
        raise attributeError
      fieldName = '(TBD)'
    innerName = self.getInnerClass().__name__
    args = [*self.__positional_args__, *self.__keyword_args__]
    args = ', '.join([str(arg) for arg in args])
    return '%s = AttriBox[%s](%s)' % (fieldName, innerName, args)

  @classmethod
  def _getOwnerListName(cls) -> str:
    """Returns the name at which the list of attribute instances of this
    type. Please note that this name is not unique to the owner as they
    are in separate scopes."""
    return '__boxes_%s__' % cls.__qualname__

  def __set_name__(self, owner: type, name: str) -> None:
    """Sets the name of the field. """
    ownerListName = self._getOwnerListName()
    if not getattr(owner, '__has_boxes__', False):
      setattr(owner, '__has_boxes__', True)

    TypedDescriptor.__set_name__(self, owner, name)
    existing = getattr(owner, ownerListName, [])
    if existing:
      return setattr(owner, ownerListName, [*existing, self])
    setattr(owner, ownerListName, [self, ])
    oldInitSub = getattr(owner, '__init_subclass__')

    def newInitSub(cls, *args, **kwargs) -> None:
      """Triggers the extra init"""
      oldInitSub(*args, **kwargs)
      self.applyBoxes(cls)

    setattr(owner, '__init_subclass__', classmethod(newInitSub))

  @classmethod
  def applyBoxes(cls, owner: type) -> None:
    """Applies the boxes to the owner class."""
    ownerListName = cls._getOwnerListName()
    boxes = getattr(owner, ownerListName, [])
    for box in boxes:
      if not isinstance(box, AttriBox):
        e = typeMsg('box', box, AttriBox)
        raise TypeError(e)
      boxName = box._getFieldName()
      setattr(cls, boxName, box)
      cls.__set_name__(box, owner, boxName)

  def __get__(self, instance: object, owner: type) -> Any:  # Footnote
    """The __get__ method is called when the descriptor is accessed via the
    owning instance. """
    value = TypedDescriptor.__get__(self, instance, owner)
    for callback in self._getGetCallbacks():
      callback(instance, value)
    return value

  def __set__(self, instance: object, value: object) -> None:
    """The __set__ method is called when the descriptor is assigned a value
    via the owning instance. """
    pvtName = self._getPrivateName()
    oldValue = getattr(instance, pvtName, None)
    setattr(instance, pvtName, value)
    for callback in self._getSetCallbacks():
      callback(instance, oldValue, value)

  def __delete__(self, instance: object, ) -> Never:
    """Deleter-function not yet implemented!"""
    e = """Tried deleting the '%s' attribute from instance of class '%s', 
    but this deleter-function is not yet implemented!"""
    msg = e % (self._getFieldName(), instance.__class__.__name__)
    raise NotImplementedError(monoSpace(msg))

#  Footnote: 'Any' or 'object'? Type hinting to 'Any' tells the type
#  checker to ignore this return value. Presently, that is the best the
#  static type checker can manage. However, type hinting to 'object' tells
#  the type checker that the return value cannot be assumed to belong to
#  any type. Thus, the type checker will indicate a problem if an object
#  is assumed belonging to a specific type when it was returned with type
#  hinting to 'object'. This is generally preferable, but in this
#  particular case, the type checker is not able to infer the type of the
#  objects created with AttriBox. For example:
#   ______________________________________________________________________
#  | class Foo:                                                           |
#  |   bar = AttriBox[int]()                                              |
#  |                                                                      |
#  |   def someMethod(self, ) -> int:                                     |
#  |     return self.bar  # Type checker will indicate a problem here!    |
#   ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#  The type checker is not able to infer that the AttriBox instance is in
#  fact an 'int'. However, this is an exception. In most cases,
#  type hinting to 'object' is preferable. The 'correct' way to handle this
#  would require the use of a stub file. It is possible to implement in
#  the AttriBox class functionality that creates a stub file at the first
#  runtime that sets the type hint to the type in the bracket. For the
#  above example, the stub file would be:
#   _____________________________________________________________________
#  | class Foo:                                                          |
#  |   bar: int                                                          |
#   ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#  Presently, having to use 'Any' instead of 'object' is a problem.
#  Implementing dynamic stub file creation will be very powerful,
#  but requires a significant effort. In the future, when more problems
#  are identified that will benefit dynamic stub file creation, this will
#  be one of the problems solved.
#  -- Asger Jon Vistisen, July 18, 2024 --
#  UPDATE, same day --
#  Writing a function that dynamically creates the code required by the
#  stub file and saving it was not as much work as the above note might
#  have indicated. Nevertheless, a bit more work is needed to add a unit
#  test. So far, the implementation is not able to look for an existing
#  stub file, but a future improvement will enable different scripts to
#  add rather than just overwrite.
#  UPDATE, again same day --
#  Implementation of the dynamically created stub file is now working. All
#  that remains is to add the unit tests. This does provide somewhat of a
#  novelty, as the unit test must test if a file is created. To ensure
#  that a unittest is not confused by an existing class from previous runs,
#  we use the 'setUpClass' and 'tearDownClass' methods to create and delete
#  the stub file.
#  UPDATE, again same day --
#  The unit tests are now implemented. This should allow the AttriBox
#  __get__ method to type hint to 'object', as the stub file will be
#  created automatically. What remains is to include methods in the
#  created stub files and to support multiple files in the same stub file.
#  UPDATE, again same day --
#  The stub files generated are missing the import statements.
#  UPDATE, again same day --
#  The stub files now include import statements. These are even formatted
#  correctly to support nested packages. Still missing is to include the
#  methods and to handle the case of multiple classes in the same file.
#  UPDATE, again same day --
#  Moved stub file generation to dedicated function.
