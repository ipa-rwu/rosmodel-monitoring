from pyecore.resources import global_registry
from .ros import getEClassifier, eClassifiers
from .ros import name, nsURI, nsPrefix, eClass
from .ros import Node, Package, Dependency, ServiceSpec, ServiceServer, TopicSpec, PackageDependency, ExternalDependency, CatkinPackage, Publisher, Artifact, SpecBase, Subscriber, ServiceClient, PackageSet, ActionSpec, ActionServer, ActionClient, MessageDefinition, Namespace, GlobalNamespace, RelativeNamespace, PrivateNamespace, InterfaceType, GraphName, ParameterType, ParameterListType, ParameterStructType, ParameterIntegerType, ParameterStringType, ParameterDoubleType, Parameter, ParameterDateType, ParameterBooleanType, ParameterBase64Type, ParameterAnyType, ParameterStructTypeMember, ParameterArrayType, ParameterValue, ParameterAny, ParameterString, ParameterBase64, ParameterInteger, ParameterDouble, ParameterBoolean, ParameterSequence, ParameterStruct, ParameterStructMember, ParameterDate, AmentPackage, QualityOfService

from pythonic_rosmodel.metamodel_gen.primitives import MessagePart

from . import ros

__all__ = ['Node', 'Package', 'Dependency', 'ServiceSpec', 'ServiceServer', 'TopicSpec', 'PackageDependency', 'ExternalDependency', 'CatkinPackage', 'Publisher', 'Artifact', 'SpecBase', 'Subscriber', 'ServiceClient', 'PackageSet', 'ActionSpec', 'ActionServer', 'ActionClient', 'MessageDefinition', 'Namespace', 'GlobalNamespace', 'RelativeNamespace', 'PrivateNamespace', 'InterfaceType', 'GraphName', 'ParameterType', 'ParameterListType', 'ParameterStructType',
           'ParameterIntegerType', 'ParameterStringType', 'ParameterDoubleType', 'Parameter', 'ParameterDateType', 'ParameterBooleanType', 'ParameterBase64Type', 'ParameterAnyType', 'ParameterStructTypeMember', 'ParameterArrayType', 'ParameterValue', 'ParameterAny', 'ParameterString', 'ParameterBase64', 'ParameterInteger', 'ParameterDouble', 'ParameterBoolean', 'ParameterSequence', 'ParameterStruct', 'ParameterStructMember', 'ParameterDate', 'AmentPackage', 'QualityOfService']

eSubpackages = []
eSuperPackage = None
ros.eSubpackages = eSubpackages
ros.eSuperPackage = eSuperPackage

Node.serviceserver.eType = ServiceServer
Node.publisher.eType = Publisher
Node.subscriber.eType = Subscriber
Node.serviceclient.eType = ServiceClient
Node.actionserver.eType = ActionServer
Node.actionclient.eType = ActionClient
Node.parameter.eType = Parameter
Package.artifact.eType = Artifact
Package.dependency.eType = Dependency
ServiceSpec.request.eType = MessageDefinition
ServiceSpec.response.eType = MessageDefinition
ServiceServer.service.eType = ServiceSpec
TopicSpec.message.eType = MessageDefinition
PackageDependency.package.eType = Package
Publisher.message.eType = TopicSpec
Artifact.node.eType = Node
Subscriber.message.eType = TopicSpec
ServiceClient.service.eType = ServiceSpec
PackageSet.package.eType = Package
ActionSpec.goal.eType = MessageDefinition
ActionSpec.result.eType = MessageDefinition
ActionSpec.feedback.eType = MessageDefinition
ActionServer.action.eType = ActionSpec
ActionClient.action.eType = ActionSpec
MessageDefinition.MessagePart.eType = MessagePart
InterfaceType.namespace.eType = Namespace
InterfaceType.qos.eType = QualityOfService
ParameterListType.sequence.eType = ParameterType
ParameterListType.default.eType = ParameterSequence
ParameterStructType.parameterstructypetmember.eType = ParameterStructTypeMember
ParameterIntegerType.default.eType = ParameterInteger
ParameterStringType.default.eType = ParameterString
ParameterDoubleType.default.eType = ParameterDouble
Parameter.type.eType = ParameterType
Parameter.value.eType = ParameterValue
ParameterDateType.default.eType = ParameterDate
ParameterBooleanType.default.eType = ParameterBoolean
ParameterBase64Type.default.eType = ParameterBase64
ParameterAnyType.default.eType = ParameterAny
ParameterStructTypeMember.type.eType = ParameterType
ParameterStructTypeMember.default.eType = ParameterStruct
ParameterArrayType.type.eType = ParameterType
ParameterArrayType.default.eType = ParameterSequence
ParameterSequence.value.eType = ParameterValue
ParameterStruct.value.eType = ParameterStructMember
ParameterStructMember.value.eType = ParameterValue
Package.spec.eType = SpecBase
SpecBase.package.eType = Package
SpecBase.package.eOpposite = Package.spec

otherClassifiers = [GraphName]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [ros] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


classes = [Node, Package, Dependency, ServiceSpec, ServiceServer, TopicSpec, PackageDependency, ExternalDependency, CatkinPackage, Publisher, Artifact, SpecBase, Subscriber, ServiceClient, PackageSet, ActionSpec, ActionServer, ActionClient, MessageDefinition, Namespace, GlobalNamespace, RelativeNamespace, PrivateNamespace, InterfaceType, GraphName, ParameterType, ParameterListType, ParameterStructType,
           ParameterIntegerType, ParameterStringType, ParameterDoubleType, Parameter, ParameterDateType, ParameterBooleanType, ParameterBase64Type, ParameterAnyType, ParameterStructTypeMember, ParameterArrayType, ParameterValue, ParameterAny, ParameterString, ParameterBase64, ParameterInteger, ParameterDouble, ParameterBoolean, ParameterSequence, ParameterStruct, ParameterStructMember, ParameterDate, AmentPackage, QualityOfService]
