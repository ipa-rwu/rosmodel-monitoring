"""Definition of meta model 'ros'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from pyecore.type import Base64Binary, Double, Int, Boolean, DateTime


name = 'ros'
nsURI = 'http://www.ipa.fraunhofer.de/ros'
nsPrefix = 'ros'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


GraphName = EDataType('GraphName', instanceClassName='java.lang.String')

GraphName.__name__ = 'GraphName'


class EObject(Ecore.EObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key, value in kwargs.items():
            if key not in self.__dict__:
                setattr(self, key, value)


class Node(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=GraphName, unique=True,
                      derived=False, changeable=True)
    serviceserver = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    publisher = EReference(ordered=True, unique=True,
                           containment=True, derived=False, upper=-1)
    subscriber = EReference(ordered=True, unique=True,
                            containment=True, derived=False, upper=-1)
    serviceclient = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    actionserver = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    actionclient = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    parameter = EReference(ordered=True, unique=True,
                           containment=True, derived=False, upper=-1)

    def __init__(self, *, serviceserver=None, publisher=None, subscriber=None, serviceclient=None, actionserver=None, actionclient=None, name=None, parameter=None, **kwargs):
        super().__init__(**kwargs)

        if name is not None:
            self.name = name

        if serviceserver:
            self.serviceserver.extend(serviceserver)

        if publisher:
            self.publisher.extend(publisher)

        if subscriber:
            self.subscriber.extend(subscriber)

        if serviceclient:
            self.serviceclient.extend(serviceclient)

        if actionserver:
            self.actionserver.extend(actionserver)

        if actionclient:
            self.actionclient.extend(actionclient)

        if parameter:
            self.parameter.extend(parameter)


class Package(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True,
                      derived=False, changeable=True, iD=True)
    fromGitRepo = EAttribute(eType=EString, unique=True,
                             derived=False, changeable=True)
    spec = EReference(ordered=True, unique=True,
                      containment=True, derived=False, upper=-1)
    artifact = EReference(ordered=True, unique=True,
                          containment=True, derived=False, upper=-1)
    dependency = EReference(ordered=True, unique=True,
                            containment=True, derived=False, upper=-1)

    def __init__(self, *, name=None, spec=None, artifact=None, fromGitRepo=None, dependency=None, **kwargs):
        super().__init__(**kwargs)

        if name is not None:
            self.name = name

        if fromGitRepo is not None:
            self.fromGitRepo = fromGitRepo

        if spec:
            self.spec.extend(spec)

        if artifact:
            self.artifact.extend(artifact)

        if dependency:
            self.dependency.extend(dependency)


@abstract
class Dependency(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Artifact(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True,
                      derived=False, changeable=True)
    node = EReference(ordered=True, unique=True,
                      containment=True, derived=False)

    def __init__(self, *, name=None, node=None, **kwargs):
        super().__init__(**kwargs)

        if name is not None:
            self.name = name

        if node is not None:
            self.node = node


@abstract
class SpecBase(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=False,
                      derived=False, changeable=True)
    fullname = EAttribute(eType=EString, unique=True, derived=False,
                          changeable=False, iD=True, transient=True)
    package = EReference(ordered=True, unique=True,
                         containment=False, derived=False)

    def __init__(self, *, name=None, package=None, fullname=None, **kwargs):
        super().__init__(**kwargs)

        if name is not None:
            self.name = name

        if fullname is not None:
            self.fullname = fullname

        if package is not None:
            self.package = package


class PackageSet(EObject, metaclass=MetaEClass):

    package = EReference(ordered=True, unique=True,
                         containment=True, derived=False, upper=-1)

    def __init__(self, *, package=None, **kwargs):
        super().__init__(**kwargs)

        if package:
            self.package.extend(package)


class MessageDefinition(EObject, metaclass=MetaEClass):

    MessagePart = EReference(ordered=True, unique=True,
                             containment=True, derived=False, upper=-1)

    def __init__(self, *, MessagePart=None, **kwargs):
        super().__init__(**kwargs)

        if MessagePart:
            self.MessagePart.extend(MessagePart)


@abstract
class Namespace(EObject, metaclass=MetaEClass):

    parts = EAttribute(eType=GraphName, unique=False,
                       derived=False, changeable=True, upper=-1)

    def __init__(self, *, parts=None, **kwargs):
        super().__init__(**kwargs)

        if parts:
            self.parts.extend(parts)


class InterfaceType(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=GraphName, unique=True,
                      derived=False, changeable=True)
    namespace = EReference(ordered=True, unique=True,
                           containment=True, derived=False)
    qos = EReference(ordered=True, unique=True,
                     containment=True, derived=False)

    def __init__(self, *, namespace=None, name=None, qos=None, **kwargs):
        super().__init__(**kwargs)

        if name is not None:
            self.name = name

        if namespace is not None:
            self.namespace = namespace

        if qos is not None:
            self.qos = qos


@abstract
class ParameterType(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ParameterStructTypeMember(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True,
                      derived=False, changeable=True)
    type = EReference(ordered=True, unique=True,
                      containment=True, derived=False)
    default = EReference(ordered=True, unique=True,
                         containment=True, derived=False)

    def __init__(self, *, name=None, type=None, default=None, **kwargs):
        super().__init__(**kwargs)

        if name is not None:
            self.name = name

        if type is not None:
            self.type = type

        if default is not None:
            self.default = default


@abstract
class ParameterValue(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ParameterStructMember(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True,
                      derived=False, changeable=True)
    value = EReference(ordered=True, unique=True,
                       containment=True, derived=False)

    def __init__(self, *, name=None, value=None, **kwargs):
        super().__init__(**kwargs)

        if name is not None:
            self.name = name

        if value is not None:
            self.value = value


class QualityOfService(EObject, metaclass=MetaEClass):

    QoSProfile = EAttribute(eType=EString, unique=True, derived=False,
                            changeable=True, default_value='default_qos')
    History = EAttribute(eType=EString, unique=True, derived=False,
                         changeable=True, default_value='keep_all')
    Depth = EAttribute(eType=Int, unique=True, derived=False, changeable=True)
    Reliability = EAttribute(eType=EString, unique=True, derived=False,
                             changeable=True, default_value='reliable')
    Durability = EAttribute(eType=EString, unique=True, derived=False,
                            changeable=True, default_value='transient_local')

    def __init__(self, *, QoSProfile=None, History=None, Depth=None, Reliability=None, Durability=None, **kwargs):
        super().__init__(**kwargs)

        if QoSProfile is not None:
            self.QoSProfile = QoSProfile

        if History is not None:
            self.History = History

        if Depth is not None:
            self.Depth = Depth

        if Reliability is not None:
            self.Reliability = Reliability

        if Durability is not None:
            self.Durability = Durability


class ServiceSpec(SpecBase):

    request = EReference(ordered=True, unique=True,
                         containment=True, derived=False)
    response = EReference(ordered=True, unique=True,
                          containment=True, derived=False)

    def __init__(self, *, request=None, response=None, **kwargs):
        super().__init__(**kwargs)

        if request is not None:
            self.request = request

        if response is not None:
            self.response = response


class ServiceServer(InterfaceType):

    service = EReference(ordered=True, unique=True,
                         containment=False, derived=False)

    def __init__(self, *, service=None, **kwargs):
        super().__init__(**kwargs)

        if service is not None:
            self.service = service


class TopicSpec(SpecBase):

    message = EReference(ordered=True, unique=True,
                         containment=True, derived=False)

    def __init__(self, *, message=None, **kwargs):
        super().__init__(**kwargs)

        if message is not None:
            self.message = message


class PackageDependency(Dependency):

    package = EReference(ordered=True, unique=True,
                         containment=False, derived=False)

    def __init__(self, *, package=None, **kwargs):
        super().__init__(**kwargs)

        if package is not None:
            self.package = package


class ExternalDependency(Dependency):

    name = EAttribute(eType=EString, unique=True,
                      derived=False, changeable=True)

    def __init__(self, *, name=None, **kwargs):
        super().__init__(**kwargs)

        if name is not None:
            self.name = name


class CatkinPackage(Package):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Publisher(InterfaceType):

    message = EReference(ordered=True, unique=True,
                         containment=False, derived=False)

    def __init__(self, *, message=None, **kwargs):
        super().__init__(**kwargs)

        if message is not None:
            self.message = message


class Subscriber(InterfaceType):

    message = EReference(ordered=True, unique=True,
                         containment=False, derived=False)

    def __init__(self, *, message=None, **kwargs):
        super().__init__(**kwargs)

        if message is not None:
            self.message = message


class ServiceClient(InterfaceType):

    service = EReference(ordered=True, unique=True,
                         containment=False, derived=False)

    def __init__(self, *, service=None, **kwargs):
        super().__init__(**kwargs)

        if service is not None:
            self.service = service


class ActionSpec(SpecBase):

    goal = EReference(ordered=True, unique=True,
                      containment=True, derived=False)
    result = EReference(ordered=True, unique=True,
                        containment=True, derived=False)
    feedback = EReference(ordered=True, unique=True,
                          containment=True, derived=False)

    def __init__(self, *, goal=None, result=None, feedback=None, **kwargs):
        super().__init__(**kwargs)

        if goal is not None:
            self.goal = goal

        if result is not None:
            self.result = result

        if feedback is not None:
            self.feedback = feedback


class ActionServer(InterfaceType):

    action = EReference(ordered=True, unique=True,
                        containment=False, derived=False)

    def __init__(self, *, action=None, **kwargs):
        super().__init__(**kwargs)

        if action is not None:
            self.action = action


class ActionClient(InterfaceType):

    action = EReference(ordered=True, unique=True,
                        containment=False, derived=False)

    def __init__(self, *, action=None, **kwargs):
        super().__init__(**kwargs)

        if action is not None:
            self.action = action


class GlobalNamespace(Namespace):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class RelativeNamespace(Namespace):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ParameterListType(ParameterType):

    sequence = EReference(ordered=True, unique=True,
                          containment=True, derived=False, upper=-1)
    default = EReference(ordered=True, unique=True,
                         containment=True, derived=False)

    def __init__(self, *, sequence=None, default=None, **kwargs):
        super().__init__(**kwargs)

        if sequence:
            self.sequence.extend(sequence)

        if default is not None:
            self.default = default


class ParameterStructType(ParameterType):

    parameterstructypetmember = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, parameterstructypetmember=None, **kwargs):
        super().__init__(**kwargs)

        if parameterstructypetmember:
            self.parameterstructypetmember.extend(parameterstructypetmember)


class ParameterIntegerType(ParameterType):

    default = EReference(ordered=True, unique=True,
                         containment=True, derived=False)

    def __init__(self, *, default=None, **kwargs):
        super().__init__(**kwargs)

        if default is not None:
            self.default = default


class ParameterStringType(ParameterType):

    default = EReference(ordered=True, unique=True,
                         containment=True, derived=False)

    def __init__(self, *, default=None, **kwargs):
        super().__init__(**kwargs)

        if default is not None:
            self.default = default


class ParameterDoubleType(ParameterType):

    default = EReference(ordered=True, unique=True,
                         containment=True, derived=False)

    def __init__(self, *, default=None, **kwargs):
        super().__init__(**kwargs)

        if default is not None:
            self.default = default


class Parameter(InterfaceType):

    type = EReference(ordered=True, unique=True,
                      containment=True, derived=False)
    value = EReference(ordered=True, unique=True,
                       containment=True, derived=False)

    def __init__(self, *, type=None, value=None, **kwargs):
        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if value is not None:
            self.value = value


class ParameterDateType(ParameterType):

    default = EReference(ordered=True, unique=True,
                         containment=True, derived=False)

    def __init__(self, *, default=None, **kwargs):
        super().__init__(**kwargs)

        if default is not None:
            self.default = default


class ParameterBooleanType(ParameterType):

    default = EReference(ordered=True, unique=True,
                         containment=True, derived=False)

    def __init__(self, *, default=None, **kwargs):
        super().__init__(**kwargs)

        if default is not None:
            self.default = default


class ParameterBase64Type(ParameterType):

    default = EReference(ordered=True, unique=True,
                         containment=True, derived=False)

    def __init__(self, *, default=None, **kwargs):
        super().__init__(**kwargs)

        if default is not None:
            self.default = default


class ParameterAnyType(ParameterType):

    default = EReference(ordered=True, unique=True,
                         containment=True, derived=False)

    def __init__(self, *, default=None, **kwargs):
        super().__init__(**kwargs)

        if default is not None:
            self.default = default


class ParameterArrayType(ParameterType):

    type = EReference(ordered=True, unique=True,
                      containment=True, derived=False)
    default = EReference(ordered=True, unique=True,
                         containment=True, derived=False)

    def __init__(self, *, type=None, default=None, **kwargs):
        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if default is not None:
            self.default = default


class ParameterAny(ParameterValue):

    value = EAttribute(eType=EString, unique=True,
                       derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):
        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class ParameterString(ParameterValue):

    value = EAttribute(eType=EString, unique=True,
                       derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):
        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class ParameterBase64(ParameterValue):

    value = EAttribute(eType=Base64Binary, unique=True,
                       derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):
        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class ParameterInteger(ParameterValue):

    value = EAttribute(eType=EIntegerObject, unique=True,
                       derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):
        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class ParameterDouble(ParameterValue):

    value = EAttribute(eType=Double, unique=True,
                       derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):
        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class ParameterBoolean(ParameterValue):

    value = EAttribute(eType=Boolean, unique=True,
                       derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):
        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class ParameterSequence(ParameterValue):

    value = EReference(ordered=True, unique=True,
                       containment=True, derived=False, upper=-1)

    def __init__(self, *, value=None, **kwargs):
        super().__init__(**kwargs)

        if value:
            self.value.extend(value)


class ParameterStruct(ParameterValue):

    value = EReference(ordered=True, unique=True,
                       containment=True, derived=False, upper=-1)

    def __init__(self, *, value=None, **kwargs):
        super().__init__(**kwargs)

        if value:
            self.value.extend(value)


class ParameterDate(ParameterValue):

    value = EAttribute(eType=DateTime, unique=True,
                       derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):
        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class AmentPackage(Package):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PrivateNamespace(RelativeNamespace):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
