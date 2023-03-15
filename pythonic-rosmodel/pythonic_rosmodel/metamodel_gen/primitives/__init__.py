from pyecore.resources import global_registry
from .primitives import getEClassifier, eClassifiers
from .primitives import name, nsURI, nsPrefix, eClass
from .primitives import AbstractType, MessagePart, bool, int8, uint8, int16, uint16, int32, uint32, int64, uint64, float32, float64, string, time, duration, boolArray, int8Array, uint8Array, int16Array, uint16Array, int32Array, uint32Array, int64Array, uint64Array, float32Array, float64Array, stringArray, TopicSpecRef, ArrayTopicSpecRef, Header, Byte, ByteArray

from pythonic_rosmodel.metamodel_gen.ros import TopicSpec

from . import primitives

__all__ = ['AbstractType', 'MessagePart', 'bool', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64', 'float32', 'float64', 'string', 'time', 'duration', 'boolArray', 'int8Array', 'uint8Array',
           'int16Array', 'uint16Array', 'int32Array', 'uint32Array', 'int64Array', 'uint64Array', 'float32Array', 'float64Array', 'stringArray', 'TopicSpecRef', 'ArrayTopicSpecRef', 'Header', 'Byte', 'ByteArray']

eSubpackages = []
eSuperPackage = None
primitives.eSubpackages = eSubpackages
primitives.eSuperPackage = eSuperPackage

MessagePart.Type.eType = AbstractType
TopicSpecRef.TopicSpec.eType = TopicSpec
ArrayTopicSpecRef.TopicSpec.eType = TopicSpec

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [primitives] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


classes = [AbstractType, MessagePart, bool, int8, uint8, int16, uint16, int32, uint32, int64, uint64, float32, float64, string, time, duration, boolArray, int8Array, uint8Array,
           int16Array, uint16Array, int32Array, uint32Array, int64Array, uint64Array, float32Array, float64Array, stringArray, TopicSpecRef, ArrayTopicSpecRef, Header, Byte, ByteArray]
