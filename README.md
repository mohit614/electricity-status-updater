# electricity-status-updater
The script conitnuosly pings the Router IP to see if elecectricity is there at home. Since Routers IP is dyncamic we are using Dynamic DNS.

--> If continously 4 ping fails, it will deliver message that the "Electricity is out". And similary if four continuous ping succeeds after a failure it will say "Electricity came". 

1. Since router's IP is dynamic and will change after power-off, first you have to confgure DDNS on your router.
Reference video --> https://www.youtube.com/watch?v=WAw6w6IMRyM&t=298s

2. After following the step1, you will have your hostname, for example mohit614.ddns.net in my case.

3. Before finally running the script you need a webhook which will drop the message in a chat service group. I have used Amazon Chime, you can use any other service of your choice.
 [https://aws.amazon.com/chime/getting-started/]

4. Finally you need to run the script somewhere without disturbance. Cloud will be best option. You can use free-tier instance like t2.micro for the same.
[https://docs.aws.amazon.com/quickstarts/latest/vmlaunch/step-1-launch-instance.html]

Future scope:-
-------------
1. Making script more fault tolerant.
2. Using AWS Lambda instead of ec2
3. Using custom Dynamic DNS
https://aws.amazon.com/blogs/startups/how-to-build-a-serverless-dynamic-dns-system-with-aws/
4. Somehow avoiding continuous ping and make it event driven...


