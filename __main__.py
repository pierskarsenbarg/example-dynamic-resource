"""A Python Pulumi program"""

import pulumi
from component import MyResource, MyResourceInputs

my_resource = MyResource(name="my_resource", args=MyResourceInputs(value="1234"))
