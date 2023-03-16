from pyecore.resources import global_registry

from . import primitives
from .primitives import (AbstractType, Byte, ByteArray, Header, MessagePart,
                         bool, boolArray, duration, eClass, eClassifiers,
                         float32, float32Array, float64, float64Array,
                         getEClassifier, int8, int8Array, int16, int16Array,
                         int32, int32Array, int64, int64Array, name, nsPrefix,
                         nsURI, string, stringArray, time, uint8, uint8Array,
                         uint16, uint16Array, uint32, uint32Array, uint64,
                         uint64Array)

__all__ = ['AbstractType', 'MessagePart', 'bool', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64', 'float32', 'float64', 'string', 'time', 'duration', 'boolArray',
           'int8Array', 'uint8Array', 'int16Array', 'uint16Array', 'int32Array', 'uint32Array', 'int64Array', 'uint64Array', 'float32Array', 'float64Array', 'stringArray', 'Header', 'Byte', 'ByteArray']

eSubpackages = []
eSuperPackage = None
primitives.eSubpackages = eSubpackages
primitives.eSuperPackage = eSuperPackage

MessagePart.Type.eType = AbstractType

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


classes = [AbstractType, MessagePart, bool, int8, uint8, int16, uint16, int32, uint32, int64, uint64, float32, float64, string, time, duration, boolArray,
           int8Array, uint8Array, int16Array, uint16Array, int32Array, uint32Array, int64Array, uint64Array, float32Array, float64Array, stringArray, Header, Byte, ByteArray]
