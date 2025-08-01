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
1. Run `pulumi up` and see the `__provider` property change
