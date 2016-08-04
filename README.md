# cf-sample-app
Simple python-based demo or test application for Cloud Foundry, based of the ideas in https://github.com/cloudfoundry-samples/test-app

# Instructions

To push to CF, simply execute `cf push test-app-python`

#Endpoints

Like the go-based test-app, the following endpoints are supported:

* `/`: Display a title, index number for the app, and uptime for the running instance.
* `/env`: Display a nicely formatted output of the environment variables
* `/port`: Return the port number the application is listening on
* `/exit`: Displays a warning message and then forcibly exits the server, (hopefully) causing CF to restart the instance

#Screenshots

`/`:
![index](https://raw.githubusercontent.com/dotnext/cf-sample-app/master/images/index.png)

`/env`
![env](https://raw.githubusercontent.com/dotnext/cf-sample-app/master/images/env.png)