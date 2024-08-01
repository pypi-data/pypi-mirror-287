# Orchestra Python SDK

![PyPI](https://img.shields.io/pypi/v/orchestra-sdk?label=pypi%20latest%20version)

This is a lightweight SDK that allows Orchestra ([getorchestra.io](https://www.getorchestra.io/)) to interact with self-hosted applications (Tasks).

The basic premise is for your self-hosted Task to send back status updates and logs to Orchestra. This is done via a HTTP request. The Task is started by Orchestra.

## Local Development

1. Create a Python3 virtual environment: `python3 -m venv venv`
1. Activate the virtual environment: `source venv/bin/activate`
1. Run `make install-dev`

At this point, you can start making changes to the code. Once completed:

1. Run `make test`
1. Update `pyproject.toml` with the new version number and any other PyPi updates
1. Run `make build`

To upload to PyPi, make sure you have API tokens set in your local `.pypirc` file. It should look like this:

```toml
[testpypi]
  username = __token__
  password = <API_TOKEN>

[pypi]
  username = __token__
  password = <API_TOKEN>
```

1. Run `make release-test` to confirm it can upload to Test PyPi as expected
1. Run `make release` to upload to PyPi

## Quickstart guide

Firstly, install the package:

```bash
pip install orchestra-sdk
```

Note - to install the test package from Test PyPi, use the following command:

```bash
pip install -i https://test.pypi.org/simple/ orchestra-sdk
```

To use the package:

```python
from orchestra_sdk.orcProcess import orcProcess

def run_example_process(correlation_id, creds):
    orcProcessInstance = orcProcess(correlation_id, creds)
    print('Starting complicated process')
    try:
        print('Trying something complicated')
        raise Exception
    except Exception as e:
        print('Failed to do something complicated')
        orcProcessInstance.sendFailure(message = str(e))
    finally:
        print('Completed')
        orcProcessInstance.sendCompletion(message = 'Completed', custom_data={'I sent this from':'my computer'})

creds = {'apikey':'my_api_key', 'clientid':'my_client_id'}
run_example_process('correlation_id', creds)
```

### Summary

1. The function takes a correlation id and a dictionary called 'creds'. The correlation id is a uuid that will be passed
   to the app by Orchestra when the app is triggered, and corresponds to a pipeline element / task. The creds object is a
   dictionary that contains an 'apikey' key that should be securely stored and accessed via your app e.g. using a local config
   file, environment variables, but ideally by interacting with a key vault
2. To kick off the process, add the code ```orcProcessInstance = orcProcess(correlation_id, creds)```. This lets Orchestra
   know the process has started
3. Use try/except/finally logic to ensure Orchestra knows when parts of the pipeline element / task fail or succeed.
   Use the methods ```sendFailure``` and ```sendCompletion``` to indicate whether stages fail. Note; arbitrary data can be
   appended to status updates using the "data" parameter. You do not need to include status codes or times in the "data"
   parameter; Orchestra calculates these by default.

Note; it's feasible that the above structure requires relatively deep nesting of try/except logic which can lead to
much lengthier code. It is perfectly fine to have a structure like below:

```python
def run_something_complicated():
    pass

def action_on_app_trigger(correlation_id, creds):
    orcProcessInstance = orcProcess(correlation_id, creds)
    try:
        run_something_complicated()
    except BaseException as e:
        orcProcessInstance.sendFailure(message = str(e), data={'some':'arbitrary stuff'})
    finally:
        print('Completed')
        orcProcessInstance.sendCompletion(message = 'Completed')
```

Which ensures that no matter what code is executed in ```run_something_complicated``` , Orchestra will know what happens
to the job.

## Quick-start; Fast API

For Production usage, you should have an App Service that accepts HTTP requests and contains all the logic you need
to carry out the pipeline/element task.

Firstly, ensure there is an endpoint that can be hit / triggered by Orchestra for the task you wish to carry out:

```python
from fastapi import Depends, FastAPI
from services.data_ingestion import dataIngester
from services.creds_manager import credsManager
from orchestra_sdk.orcProcess import orcProcess
from routers import base

app = FastAPI()

app.include_router(base.router)

@app.post("/kickOffIngestion")
async def root(body= Body()):
    creds = credsManager.get_creds()
    orcProcessInstance = orcProcess(body.correlation_id, creds)
    ingester__ = dataIngester()
    try:
        ingester__.run()
    except BaseException as e:
        orcProcessInstance.sendFailure(message = str(e), data={'some':'arbitrary stuff'})
    finally:
        print('Completed')
        orcProcessInstance.sendCompletion(message = 'Completed')
    return {"message": "Process kicked off successfully"}
```

There are a few things happening here:

1. You have a credentials service that securely fetches your Orchestra API Key, which is being imported and handles the
   generation of the ```creds``` object
2. You instantiate the ```orcProcess``` by using the creds object in (1) but also by accessing the correlation ID, which
   is passed to you in the body of the request usnig FastAPI's ```Body()``` function
3. You nest the function call ```ingeter__.run()``` within try / except / finally to ensure Orchestra has the relevant
   information to know how the task is performing
4. Bonus: the code above is not actually asynchronous although the function is defined with async def, and will _only_
   return the response once ```ingester.run()``` has finished running. It is good API practice to make the code execute
   and return a response immediately for Post-like requests
