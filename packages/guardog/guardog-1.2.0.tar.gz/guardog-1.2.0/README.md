## guardog-py
[Guardog](https://guardog.app) is a simple and easy-to-use application monitoring and alerting tool. It notifies you of runtime errors in realtime so that you can stay on top of issues and focus on delivering quality code to your users.

![guardog with python](https://guardog-website-assets.s3.eu-north-1.amazonaws.com/guardog_py_640_360.jpg)


## Installation

```bash
pip install guardog
```
**Note:** Guardog works on Python 3.7 and above

## Usage
```py
from guardog import Guardog


gd = Guardog(
    api_key='<YOUR_API_KEY>',
    uid='<UID>',
    service_id='<SERVICE_ID>'
)


@gd.watch() # Watches for any exceptions and notifies you
def this_function_will_fail():

    return 42 / 0


this_function_will_fail()
```

## Credentials

To get your `api_key`, `uid` and `service_id` values, [login](https://guardog.app/login) (or [signup](https://guardog.app/signup) if you already haven't) to Guardog

And once you are directed to your dashboard, follow these steps

1. `Create Service`
2. Choose `Application error alerting` in dropdown
3. Fill in the form along with the notification info
4. Once a new service is created, Click on `Details` and you should see your credentails there. You can generate a new API key anytime.

Here's an screenshot of an example service
![guardog service details](https://guardog-website-assets.s3.eu-north-1.amazonaws.com/details.jpg)

And that's it! You are all set to receive alerts everytime your program crashes during runtime.

**Note:**&nbsp; We don't spam you everytime an exception occurs. We only notify you every 6 hours from the last occurence.

For any issues, feedbacks and suggestions contact gautham@guardog.app

**Blog** - https://www.guardog.app/blog/guardog-python