# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['guardog']

package_data = \
{'': ['*']}

install_requires = \
['pytz>=2024.1,<2025.0', 'requests>=2.31.0,<3.0.0']

setup_kwargs = {
    'name': 'guardog',
    'version': '1.0.0',
    'description': '',
    'long_description': "## guardog-py\n[Guardog](https://guardog.app) is a simple and easy-to-use application monitoring and alerting tool. It notifies you of runtime errors in realtime so that you can stay on top of issues and focus on delivering quality code to your users.\n\n![guardog with python](https://guardog-website-assets.s3.eu-north-1.amazonaws.com/guardog_py_640_360.jpg)\n\n\n## Installation\n\n```bash\npip install guardog\n```\n**Note:** Guardog works on Python 3.7 and above\n\n## Usage\n```py\nfrom guardog import Guardog\n\n\ngd = Guardog(\n    api_key='<YOUR_API_KEY>',\n    uid='<UID>',\n    service_id='<SERVICE_ID>'\n)\n\n\n@gd.watch() # Watches for any exceptions and notifies you\ndef this_function_will_fail():\n\n    return 42 / 0\n\n\nthis_function_will_fail()\n```\n\n## Credentials\n\nTo get your `api_key`, `uid` and `service_id` values, [login](https://guardog.app/login) (or [signup](https://guardog.app/signup) if you already haven't) to Guardog\n\nAnd once you are directed to your dashboard, follow these steps\n\n1. `Create Service`\n2. Choose `Application error alerting` in dropdown\n3. Fill in the form along with the notification info\n4. Once a new service is created, Click on `Details` and you should see your credentails there. You can generate a new API key anytime.\n\nHere's an screenshot of an example service\n![guardog service details](https://guardog-website-assets.s3.eu-north-1.amazonaws.com/details.jpg)\n\nAnd that's it! You are all set to receive alerts everytime your program crashes during runtime.\n\n**Note:**&nbsp; We don't spam you everytime an exception occurs. We only notify you every 6 hours from the last occurence.\n\nFor any issues, feedbacks and suggestions contact gautham@guardog.app\n\n**Blog** - https://www.guardog.app/blog/guardog-python",
    'author': 'Gautham Reddy',
    'author_email': 'gautham@guardog.app',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
