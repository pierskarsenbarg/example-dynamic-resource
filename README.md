# Simple dynamic provider example

## Deploy

1. Clone repo: `git clone https://github.com/pierskarsenbarg/example-dynamic-resource`
1. Change to correct directory: cd example-dynamic-resource
1. Create virtual environment: `python3 -m venv venv`
1. Activate virtual environment: `source venv/bin/activate`
1. Install dependencies: `pip3 install -r requirements.txt`
1. Run `pulumi up` and select "yes" to create resources
1. Rename components file: `mv components.py components2.py`
1. Update `__main__.py` and change line 4 to read `from component2 import MyResource, MyResourceInputs`
1. Run `pulumi up` and see the `__provider` property change:

```console
Previewing update (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/pierskarsenbarg/example-dynamic-resource/dev/previews/73c3a356-13d3-41e7-b2ca-081f9ff06110

     Type                               Name                          Plan       Info
     pulumi:pulumi:Stack                example-dynamic-resource-dev
 ~   └─ pulumi-python:dynamic:Resource  my_resource                   update     [diff: ~__provider]

Resources:
    ~ 1 to update
    1 unchanged

Do you want to perform this update? no
confirmation declined, not proceeding with the update
```
