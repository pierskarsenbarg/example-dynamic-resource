from pulumi import Input, Output
from pulumi.dynamic import CreateResult, ResourceProvider, UpdateResult, Resource
from os import urandom
from binascii import b2a_hex


class MyResourceInputs(object):
    value: Input[str]

    def __init__(self, value):
        self.value = value


class MyResourceProvider(ResourceProvider):
    def create(self, props):
        return CreateResult("ref-" + b2a_hex(urandom(16)).decode("utf-8"), outs=props)

    def update(self, id, old_inputs, new_inputs):
        return UpdateResult(outs={**new_inputs})


class MyResource(Resource):
    def __init__(self, name: str, args: MyResourceInputs, opts=None):
        super().__init__(MyResourceProvider(), name, vars(args), opts)

