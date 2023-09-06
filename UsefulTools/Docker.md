Motivation:
- Compatibility
- Long setup time
Docker 容器将一个软件包在一个完整的文件系统中，该文件系统包含运行所需的一切：代码、运行时、系统工具、系统库——任何可以安装在服务器上的东西。这保证了软件无论其环境如何，都将始终运行相同的程序。

## Containers
- Completely isolated environments
-  can have their own processes, network interfaces, mounts.
- they share the same OS kernel
The main purpose of Docker is to package and containerize applications and to ship them , run them anywhere anytime.

#### Container vs Virtual Machines
![[Pasted image 20230714130922.png]]
#### Containers & VM
![[Pasted image 20230714131338.png]]

#### Container vs image
An image is a package or **template** used to create one or more containers.
Containers are running **instances** of images that are isolated

## Basic Docker Commands
`docker run [image]` : used to run a container from an image. If the image does not exist, Docker will pull the image down form the Docker hub. Existed image will be reused.
`docker run -d [image]` : used to run a container in a detached mode(run in the backend)
`docker attach [container ID/name]` : to attach back to the running container 
`docker ps` : lists all running containers and some basic information; `-a` outputs all including previously stopped or existed containers.
`docker stop [container ID/name]` 
`docker start [container]`
`docker rm [container ID/name]` : to remove a container(stopped ones). Use `docker rm $(docker ps -a -q)` to remove all.

`docker images` : to list all the images downloaded to local
`docker pull [image]` : to only pull the image and not run a container.
`docker rmi [image]` : to remove an image(ensure no containers are running off of that image; even exited)

Containers are not meant to host an operating system, but to **run a specific task or process**(such as to host an instance of  a web server or  application server or a DB,...). Once the task is complete the container exits.The container only lives as long as the process inside it is alive.
example:
`docker run ubuntu` will exit imediately
`docker run ubuntu sleep 5` will sleep for 5s and exit

`docker exec [container ID/name] [command]`

## Docker Run
### tag
`docker run redis:4.0` : add tag to choose a version of the image; default is the latest one. We can find the tags looking up the image.

### STDIN
By default, the docker container does not listen to a standard input, it does not have a terminal to read inputs from( runs in a **non-interactive mode**)
Use `-i` to map the STDIN of your host to the docker container.
`-t` : to create pseudo terminal

### PORT mapping(not fully understanded)
`docker run kodekloud/webapp`
![[Pasted image 20230715000044.png]]
The app is listening on port 5000
IPs used to access the web app from a web browser :
* [[Computer Network#^cd3338|IP of the docker container]]. Every docker container gets an IP assigned by default(here `172.17.0.2` ). It is an **internal IP** and is only accessible within the docker host.
  If we open a browser form within the docker host(??), we can go to `http://172.17.0.2:5000`(可以使用wsl2 `curl`, 但是不知道为啥浏览器不行，可能因为是子系统？ 不行还是不好使)
  (users outside the docker host cannot access it).
* [[Computer Network#^e3f057|IP of the docker host]] . But we must have mapped the port inside the docker container to a free port on the docker host.
  Use `-p` to map the port.
   `docker run -p 80:5000 kodekloud/webapp` 
   We can also use `localhost:80`
  All traffic on port 80 on docker host will get routed to port 5000 inside the docker.
  Using this way we can run multiple instances of the app and map them to different ports.
  `docker run -p 8000:5000 kodekloud/webapp`
 
  ![[Pasted image 20230715004434.png]]
### Volume mapping
```
docker run mysql
docker stop mysql
docker rm mysql
```
Assume we dumped data into the DB, if we were to remove the mysql container,  the container with the data would be removed.
To persist data, we can map a directory outside the container on the docker host to a directory inside the container.
```bash
docker run -v /opt/datadir:/var/lib/mysql mysql
#map outside dir /opt/datadir to inside /var/lib/mysql
```
![[Pasted image 20230715011502.png]]
When docker container runs, it will implicitly mount the external directory to the folder.  All the data will be stored in the external volume.

### Inspect Container
`docker inspect [container ID/name]` used to return all details of a container in a JSON format.

### Container Logs
`docker logs [container]` used to see the logs(STDOUT&STDERR) of a container running in the background

## Docker Images
### To create an image
Example: containerize a simple web application built using the Python flask framework:
* What application we are containerizing(creating an image for), how it is built?
1. OS - ubuntu
2. Update apt repository `apt update`
3. Install dependencies using apt
4. Install Python dependencies using pip
5. Copy source code of the app to a location like /opt folder
6. Run the web server using "flask" command
### Dockerfile
Dockerfile is a **text file** written in an **instruction and arguments format** that Docker can understand.
`INSTRUCTION [argument]` 
An example:
```dockerfile
FROM ubuntu
#Start from a base OS or another image based on an OS
#All dockerfiles must start with a FROM instruction
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y pip
RUN pip install -y flask
#-y is important; assume yes to any questions that pop up through installation, or it will get stuck!!!

COPY app.py /opt/app.py
#copies files from the local system onto the docker image
ENTRYPOINT FLASK_APP=app.py flask run --host=0.0.0.0
#allows us to specify a command that will be run when the image is run as a container
```
### Layered architecture
When Docker builds the image, it builds these in a layered architecture.
Each line of a instruction creates a new layer in the docker image. 
Each layer only stores the changes from the previous layer(?)
### Failure
All the layers built are cached by Docker. Failure or adding a layer  is faster as only the layer above need rebuilding.

Build the image locally
```
docker build . -t [imagename]
```
Push it to docker hub
```
docker build . -t [account/imagename]
docker login
docker push [account/imagename]
```

### Environment Variables
`docker inspect [image or container]` to check the env of an image/a container.
`docker run -e ENV_NAME=[env] [image]` to change the env of a container.
We can find the image's additional ENV on docker hub.

### Commands vs Entrypoint
Containers are not meant to host an operating system, but to **run a specific task or process**(such as to host an instance of  a web server or  application server or a DB,...). Once the task is complete the container exits.The container only lives as long as the process inside it is alive.

Example:
`docker run ubuntu` will exit imediately
Dockerfile for `ubuntu` image:
![[Pasted image 20230716142852.png]]
#### CMD
`CMD` defines the default program that will run within the container.
`bash` listens for inputs from a terminal, if it cannot find the terminal or get `exit` , it will exit.

**Specify a different command to start the container：**
* append a command to **overide** the default
`docker run ubuntu sleep 5`
* change the Dockerfile
```Dockerfile
#ubuntu-sleeper
	...
CMD ["sleep","5"]
```
```Dockerfile
CMD command param1
CMD ["command", "param1"]
#JSON array format, the first element should be executable!!!
```
#### ENTRYPOINT
`ENTRYPOINT` instruction also specifies the program that will be run when the container starts.
```Dockerfile
ENTRYPOINT command
ENTRYPOINT ["command"]
```
Whatever we specify on the command, it will be **appended** to the entry point
```Dockerfile
	...
ENTRYPOINT ["sleep"]
```
`docker run ubuntu-sleeper 10`

We can also combine `CMD` & `ENTRYPOINT` to set a default argument to the program.
NOTE: only in json array format
```Dockerfile
ENTRYPOINT ["command"]
CMD ["para1"]
```
`ENTRYPOINT` can be overrided using:
`docker run --entrypoint [command] [image] [param] `

## Docker Compose
We can create a configuration file in Yaml format called `docker-compose.yml`, and put together different services and the options to run.
![[Pasted image 20230716170646.png]]
Then simply run `docker-compose up` to bring up the app stack.

Example: voting application
```
#data layer
docker run -d --name=redis redis
#naming is important
docker run -d --name=db postgres

#web layer
docker run -d --name=vote -p 5000:80 voting-app
docker run -d --name=result -p 5001:80 result-app

docker run -d --name=worker worker
```
### docker run --links
`docker run -d --name=vote -p 5000:80 --link redis:redis voting-app`
It creates an entry into the /etc/host file on the voting container, adding  an entry with the hostname redis with an internal IP of the Redis container
![[Pasted image 20230716183004.png]]
`docker run -d --name=result -p 5001:80 --link db:db result-app`
`docker run -d --name=worker --link redi:redis --link db:db worker`
NOTE: using links this way is deprecated, as advanced concepts in Docker swarm and networking supoorts better way of the above.
### docker compose
![[Pasted image 20230717084840.png]]
### docker compose - build
![[Pasted image 20230717085117.png]]
Some user developed images needn't have been built but can be written into Docker-compose file as directory, and they'll be built.
### docker compose - versions
![[Pasted image 20230717092615.png]]
Docker Compose evolved over time.
`version: 1` has lots of limitations: network setting, start-up or
ders, ...
- Docker compose attaches all the containers to the default bridged network and use links to enable communication between the containers
`version: 2` 
- The `version` must be specified at the top.
- Docker Compose creates a bridge network for the app and then attaches all containers to that new network. All containers are then able to communicate to each other using their service names. So you **donot need links** in version 2.
- Dependency feature. Add a `depends-on` property to indicate the dependency relationships
`version: 3`
- With support for Docker Swarm

```yaml
version: 2
services:
     redis:
        image: redis
        networks:
            - backend
     db:
        image: portgres:9.4
        
```


## Docker Engine
When we install Docker on a Linux host, we actually install:
- Docker Daemon: background process that manages Docker objects(images, containers, volumes and networks,...).
- REST API: API interface that programs can use to talk to the daemon and provide instructions
- Docker CLI: need not be on the same host; can work with a remote Docker engine `docker -H=remote-docker-engine-address:port`
### Containerization
Docker uses namespaces to isolate workspace:
Process ID, network, interprocess communication, mount, Unix timesharing systems are created in their own spaces,  providing isolation between containers.
### Namespace - PID
Whenever a Linux system boots up, it starts with the root process `PID: 1` which kicks off all the other processes in the system.
`PID` s are unique.
![[Pasted image 20230718101837.png]]
We can create a child system in the host Linux system. The processes running inside the container are in fact processes running on the underlying host. So they get the `PID` in the host and another `PID` in the container namespace. 
The container thinks that it has its own root process tree, so it is an independent system.
### cgroups(control groups)
The underlying Docker host as well as the containers shared the same system resources(CPU, memory,..)
By default there's no restriction to how much resource a container can use.
We can use `--cpus` and `--memory` to set a limit.
```
docker run --cpu=.5 ubuntu
docker run --memory=100m ubuntu
```
## Docker Storage
### File system
When we install Docker on a system, it creates a file structure `/var/lib/docker`
![[Pasted image 20230718105100.png]]
### Layered architecture
Each line of the instruction in the Dockerfile creates a new layer in the Docker image, each layer stores the changes from the previous layer.
![[Pasted image 20230718110230.png]]
The same image layer is shared by all containers created using this image.
The container layer is writable, used to store data created by the container(such ad log files written by the app, any temporary files generated by the container, any file modified by the user on the container). The life of this layer is only as long as the container is alive.
![[Pasted image 20230718111804.png]]
### Volumes
If we wish to persist the data in the container, we can map the host dir to the dir storing the data in the container.
Volume mounting:
```bash
docker volume create data_volume
#create a dir named data_volume in host dir /var/lib/docker/volumes
#If not created before run -v is also ok
#Docker will automatically create a volume and mount it to the container
docker run -v data_volume:[default location the image stores data]
```
Bind mounting: mounts a dir from any location on the host
```bash
docker run -v [absolute path]:[location the image stores data]
docker run \
--mount type=bind,source=[abs path],target=[loc] image
```
### Storage drivers
Docker uses storage drivers to enable layered architecture.
![[Pasted image 20230718115237.png]]
The selection of storage driver depends on the OS(ubuntu's default storage driver is `aufs`

## Docker network
When we install Docker, it creates three networks automatically: Bridge, None, Host.
Use `--network=none/host/[network]` to change the network. 
- Bridge
The Bridge network is a private **internal network** created by Docker on the host.
All containers are attached to this network **by default**, 
and they get an internal IP address usually in the range `172.17` series. The **containers can access each other** using this internal IP.
To access the containers from outside, map the ports of these containers to ports on the Docker host; or aossociate the container to the host network(in this way we cannot run multiple same containers as they all use the same port now)
- None
The containers are not attached to any network and cnnot access other containers or external.
### User-defined networks
By default, Docker only creates one bridge network.
To create our own network:
```
docker network create \
--driver bridge \
--subnet [like 182.18.0.0/16] \
[custom-isolated-network-name]
```
To list the networks:
`docker network ls`
### Inspect network
To see an existing container's network settings and IP:
`docker inspect [container]`
To inspect an existing network
`docker network inspect [network]`
### Embedded DNS

## Docker Registry
Docker registry is a central repository of all Docker images.

Image naming convention: `[user/account]/[image/repository]`
if we don't give `[user/account]` , then Docker assumes it is the same as the given one.
If we donot specified the location where the images are push to/pull from, it is assumed to be on Docker's default registry Docker Hub. `docker.io` is Docker Hub's DNS name.
![[Pasted image 20230718151303.png]]
### Private Registry
Many cloud service providers(AWS,AZure,...) provide a private registry by default when openning an account.
We can choose to make a repository private so that it can only be accessed using a set of credentials.
```
docker login private-registry.io
docker run private-registry.io/apps/internal-app
```
### Deploy Private Registry
![[Pasted image 20230718152309.png]]
