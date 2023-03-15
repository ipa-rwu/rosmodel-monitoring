"""Definition of meta model 'primitives'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'primitives'
nsURI = 'http://www.ipa.fraunhofer.de/primitives'
nsPrefix = 'primitives'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class EObject(Ecore.EObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key, value in kwargs.items():
            if key not in self.__dict__:
                setattr(self, key, value)


@abstract
class AbstractType(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MessagePart(EObject, metaclass=MetaEClass):

    Data = EAttribute(eType=EString, unique=True,
                      derived=False, changeable=True)
    Type = EReference(ordered=True, unique=True,
                      containment=True, derived=False)

    def __init__(self, *, Type=None, Data=None, **kwargs):
        super().__init__(**kwargs)

        if Data is not None:
            self.Data = Data

        if Type is not None:
            self.Type = Type


class bool(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class int8(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class uint8(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class int16(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class uint16(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class int32(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class uint32(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class int64(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class uint64(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class float32(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class float64(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class string(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class time(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class duration(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class boolArray(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class int8Array(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class uint8Array(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class int16Array(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class uint16Array(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class int32Array(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class uint32Array(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class int64Array(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class uint64Array(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class float32Array(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class float64Array(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class stringArray(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TopicSpecRef(AbstractType):

    TopicSpec = EReference(ordered=True, unique=True,
                           containment=False, derived=False)

    def __init__(self, *, TopicSpec=None, **kwargs):
        super().__init__(**kwargs)

        if TopicSpec is not None:
            self.TopicSpec = TopicSpec


class ArrayTopicSpecRef(AbstractType):

    TopicSpec = EReference(ordered=True, unique=True,
                           containment=False, derived=False)

    def __init__(self, *, TopicSpec=None, **kwargs):
        super().__init__(**kwargs)

        if TopicSpec is not None:
            self.TopicSpec = TopicSpec


class Header(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Byte(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ByteArray(AbstractType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
