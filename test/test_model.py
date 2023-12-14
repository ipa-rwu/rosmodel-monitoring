from pythonic_rosmodel.metamodel_gen.ros import *
from pythonic_rosmodel.metamodel_gen.primitives import *
import logging
import argparse


def setup_logging(log_level):
    logging.basicConfig(
        level=log_level,  # Set the logging level
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


sec = MessagePart(Type=int32.__call__(), Data="sec")
nanosec = MessagePart(Type=int32.__call__(), Data="nanosec")
Time = TopicSpec(name="Time", message=MessageDefinition(MessagePart=[sec, nanosec]))
Duration = TopicSpec(message=MessageDefinition(MessagePart=[sec, nanosec]))
builtin_interfaces = Package(name="builtin_interfaces", spec=[Time, Duration])

RefTime = TopicSpecMsgRef(Reference=Time)

Header = TopicSpec(
    message=MessageDefinition(
        MessagePart=[
            MessagePart(
                Type=RefTime,
                Data="stamp",
            )
        ]
    )
)


def main():
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(
        description="Example of configuring logging from the command line"
    )
    parser.add_argument(
        "--log_level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level (default: INFO)",
    )

    # Parse command-line arguments
    args = parser.parse_args()

    # Configure logging based on the command-line argument
    setup_logging(args.log_level)

    # Your application logic here

    logging.debug(dir(builtin_interfaces.spec))
    logging.info(builtin_interfaces.spec.__class_getitem__("Time"))
    for i in builtin_interfaces.spec:
        logging.debug(i)
        logging.debug(dir(i))
        logging.debug(i.package)

    logging.info(Time.package)


if __name__ == "__main__":
    main()


# CameraInfo = TopicSpec(name="CameraInfo", message=[TopicSpec()])
# realsense2_camera_node = Node(name="camera", publisher=Publisher())
# , publisher=["color/image_raw"]

# realsense2_camera_node.publisher.eType
