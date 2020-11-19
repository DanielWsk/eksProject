# circle2

This repo is designed to demonstrate how CircleCi uses CI/CD to build and deploy docker images to AWS ECS.
If part of the code fails, CirlceCi will block the commit and stop the image from being deployed. The advantage of using CircleCi is that the container will never experience downtime and bad code will never affect the status of the container that is already deployed. 

This repo used a simple flask container to run a basic hello world python application. There is also a test program that checks the code within the flask container.
The Dockerfile builds the image, copying the python file into the flask container and running the program.
CirclCi checks the code, runs the test, and then pushes the image to Docker Hub.

Finally, if the code passes the checks, it is deployed to AWS ECS.

- These steps are layed out within the .cirlceci/conf.yml file. First the image is build and pushed to Docker Hub, then the test file is run to test the python program. (If the test fails, the entire pipeline fails and the commit is canceled.) And then the image is deployed to an ECS service running on AWS.  

This is the EKS Branch