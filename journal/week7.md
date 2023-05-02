# Week 7 — Solving CORS with a Load Balancer and Custom Domain

This week was delivered together with week 6 so some topics are overlapping and the below topics might not have been complited exactly in this order.

### Provision and configure ALB (application load balancer) along with target 

The application load balancer was created in the AWS console. Existing VPC and subnets were used and a new security group was created. All incoming and outcoming traffic was allowed. After that it was necessary to modify the security group that was previously created for the ECS service os that it wouldn't anymore allow incoming traffic from anywhere else than the load balancer. 

The ALB has two listeners, one for backend-flask listening to port 4567 and another for frontend-react-js listening to port 3000:

![listeners](assets/listeners.png)

The backend health-check could now be access through the load balancer:

![alb health](assets/alb_health.png)

This means also the load balancer target group displays status 'healthy'. 

The final step was to modify load balancer to enable access logs. A new S3 bucket for the logs had to also be created. 

### Create an SSL certificate via ACM

A cerficate was created for the domain and wildcard:

![acm](assets/acm.png)



### Manage your domain using Route53 via hosted zone

A Route53 hosted zone was created through the AWS console. The default nameservers at Godaddy (where the domain was bought from) were deplaced with the hosted zone nameservers. Godaddy account now displayes 'We can't desplay your DSN information because your nameservers aren't managed by us'. Now it was possible to modify the DNS information at the hosted zone. 

As there was no an ACM certificate, it was possible to create straight from there a CNAME record to Route 53. 

### Setup a record set for naked domain to point to frontend-react-js and a record set for api subdomain to point to the backend-flask

Some modifications for load balancer were needed after this. A rule to redirect HTTP 80 to HTTPS 443 was added first. The frontend is going to be our naked domain. Another route at the load balancer was created to add port 443 to the frontend target group. At this point the ACM certificate had to be added as well for this to work. 

Now it was time to delete the previously created listeners for ports 3000 and 4567. A new rule could be added for listener for port 443:

![listeners](assets/listeners.png)

All requests to api.cloudproject.online would be forwarded to the backend target group where others could go to frontend target group. 

Next an A record was created in the hosted zone to point to the load balancer, which was the main reason Route 53 is used in this project. By using an alias it is possible to point to the load balancer without defining a URL. Another A record was created for the subdomain. 

Both frontend and backend could now be accessed:

![curl frontend and backend](assets/curl_front_back.png)

After these steps the frontend docker image had to be rebuilt with the correct backend url. The service had to be re-deployed.

### Configure CORS to only permit traffic from our domain

The backend task definition was changed to include the actual URLs as it previously had which means traffic will be permitted from anywhere instead of only our our domain: 

```
     "environment": [
          {"name": "FRONTEND_URL", "value": "https://cloudproject.online"},
          {"name": "BACKEND_URL", "value": "https://api.cloudproject.online"},
        ],
```

The backend service was then re-deployed. 


## Additional fixes that were implemented during this week

### Secure Flask by not running in debug mode

The issue with Flask application was that it was running in debug mode, which meant anyone would be able to see the error messages and it is possible for attackers to to add arbitraty Python code through the browser. The best option is to use debug mode only for development instead of production. This shouldn't be an issue as Rollbar is used for error logging. A separate Dockerfile.prod was created now for frontend and these flags were added ``"--no-debug", "--no-debugger", "--no-reload"``. Accessing a path that doesn't exist, doesn't anymore reveal access logs, instead the user will just see a general internal server error:

![debug mode disabled](assets/debug_off.png)


### Refactor bin directory to be top level

In order to make our work easier, a few additional scripts were created to easily build and push images without having to copy-paste commands. 

A script was created to force-deploy services so that it doesn't have to be manually done through the console every time changes are made to the image. The script will the the ARN of the latest task definiton and then based on that force a new deployment. 

At this point it was noted that having the bin-directory within backend-flask doesn't make sense as there are several scripts for the frontend as well. The folder was moved to the top level and every script had to be checked after that to make sure that the pathing is corrected. This took a few attemps as there were several things that had to be corrected such as the path for the backend health-check as it now cause the container to be unhealthy as the new bin-folder was not reacher for the backend application. 

### Fix Messaging in Production


### Implement Refresh Token for Amazon Cognito

The issue with the implementation was that the CheckAuth.js didn't attempt to renew the tokens after they expire. This meant that it was sometimes necessary to manually login again, which made the app confusing to use. This code was added to the CheckAuth function:

```
.then((cognito_user_session) => {
        console.log('cognito_user_session',cognito_user_session);
        localStorage.setItem("access_token", cognito_user_session.accessToken.jwtToken)
```

There also had to be way to re-set the token in local storage every time an API call is made, to make sure that the token is fresh. This was implemented by adding a new function:

```
export async function getAccessToken() {
  Auth.currentSession()
  .then((cognito_user_session) => {
    const access_token = cognito_user_session.accessToken.jwtToken;
    localStorage.setItem("access_token", access_token)
  })
.catch((err) => console.log(err));
}
```

This function will now set the access token in local storage. The function is then used in other pages such as HomefeedPage, where the LoadData function gets the access token from local storage. 



