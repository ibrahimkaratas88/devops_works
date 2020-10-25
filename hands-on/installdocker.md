From AWS EC2 service launch an instance using AMI : "Ubuntu Server 18.04 LTS (HVM), SSD Volume Type" 
Security group : select or create a new one that "HTTP and TCP anywhere" 

connect to the instance using SSH

# installition process for docker : 
1.
ubuntu@ip-172-31-31-235:~$  sudo apt install apt-transport-https ca-certificates curl software-properties-common

2.
ubuntu@ip-172-31-31-235:~$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic test"

3.
ubuntu@ip-172-31-31-235:~$ sudo apt install docker 

4.
ubuntu@ip-172-31-31-235:~$ sudo apt install docker.io

5. #lets see which version was installed:
ubuntu@ip-172-31-31-235:~$ sudo docker version

#output :
        Client:
        Version:           19.03.6
        API version:       1.40
        Go version:        go1.12.17
        Git commit:        369ce74a3c
        Built:             Fri Feb 28 23:45:43 2020
        OS/Arch:           linux/amd64
        Experimental:      false

        Server:
        Engine:
        Version:          19.03.6
        API version:      1.40 (minimum version 1.12)
        Go version:       go1.12.17
        Git commit:       369ce74a3c
        Built:            Wed Feb 19 01:06:16 2020
        OS/Arch:          linux/amd64
        Experimental:     false
        containerd:
        Version:          1.3.3-0ubuntu1~18.04.2
        GitCommit:        
        runc:
        Version:          spec: 1.0.1-dev
        GitCommit:        
        docker-init:
        Version:          0.18.0
        GitCommit:        


# check for docker containers
ubuntu@ip-172-31-31-235:~$ sudo docker info 
#output:      
        Client:
        Debug Mode: false

        Server:
        Containers: 0 # see this is zero now
        Running: 0 # see this is zero now
        Paused: 0
        Stopped: 0
        Images: 0 # see this is zero now
        Server Version: 19.03.6
        Storage Driver: overlay2
        Backing Filesystem: extfs
        Supports d_type: true
        Native Overlay Diff: true
        Logging Driver: json-file
        Cgroup Driver: cgroupfs
        Plugins:
        Volume: local
        Network: bridge host ipvlan macvlan null overlay
        Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
        Swarm: inactive
        Runtimes: runc
        Default Runtime: runc
        Init Binary: docker-init
        containerd version: 
        runc version: 
        init version: 
        Security Options:
        apparmor
        seccomp
        Profile: default
        Kernel Version: 5.3.0-1035-aws
        Operating System: Ubuntu 18.04.5 LTS
        OSType: linux
        Architecture: x86_64
        CPUs: 1
        Total Memory: 978.6MiB
        Name: ip-172-31-31-235
        ID: 4D23:NEPK:F4UE:YCRL:WQBD:6GIY:V3NL:OX3C:LM2Z:OEBF:VZHG:JFBZ
        Docker Root Dir: /var/lib/docker
        Debug Mode: false
        Registry: https://index.docker.io/v1/
        Labels:
        Experimental: false
        Insecure Registries:
        127.0.0.0/8
        Live Restore Enabled: false

        WARNING: No swap limit support

# create and start a container:
ubuntu@ip-172-31-31-235:~$ sudo docker run -i -t ubuntu /bin/bash
#output:
        Unable to find image 'ubuntu:latest' locally
        latest: Pulling from library/ubuntu
        d72e567cc804: Pull complete 
        0f3630e5ff08: Pull complete 
        b6a83d81d1f4: Pull complete 
        Digest: sha256:bc2f7250f69267c9c6b66d7b6a81a54d3878bb85f1ebb5f951c896d13e6ba537
        Status: Downloaded newer image for ubuntu:latest
        root@16a4ea975547:/#    
# now it works in : root@16a4ea975547:/#  (we are in container bash)

root@16a4ea975547:/#  exit

# now let's let’s check that the docker binary exists
ubuntu@ip-172-31-31-235:~$ sudo docker info 

# output:
        Client:
        Debug Mode: false

        Server:
        Containers: 1 # this is changed to one 
        Running: 1 # this is changed to one 
        Paused: 0
        Stopped: 0
        Images: 1 # this is changed to one 
        Server Version: 19.03.6
        Storage Driver: overlay2
        Backing Filesystem: extfs
        Supports d_type: true
        Native Overlay Diff: true
        Logging Driver: json-file
        Cgroup Driver: cgroupfs
        Plugins:
        Volume: local
        Network: bridge host ipvlan macvlan null overlay
        Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
        Swarm: inactive
        Runtimes: runc
        Default Runtime: runc
        Init Binary: docker-init
        containerd version: 
        runc version: 
        init version: 
        Security Options:
        apparmor
        seccomp
        Profile: default
        Kernel Version: 5.3.0-1035-aws
        Operating System: Ubuntu 18.04.5 LTS
        OSType: linux
        Architecture: x86_64
        CPUs: 1
        Total Memory: 978.6MiB
        Name: ip-172-31-31-235
        ID: 4D23:NEPK:F4UE:YCRL:WQBD:6GIY:V3NL:OX3C:LM2Z:OEBF:VZHG:JFBZ
        Docker Root Dir: /var/lib/docker
        Debug Mode: false
        Registry: https://index.docker.io/v1/
        Labels:
        Experimental: false
        Insecure Registries:
        127.0.0.0/8
        Live Restore Enabled: false
        WARNING: No swap limit support

# Installing a package in container
root@16a4ea975547:/# apt-get update && apt-get install nano 

root@16a4ea975547:/# exit
# Once we exited the container, that command ended, and the container was stopped.

# The container still exists; we can show a list of current containers
ubuntu@ip-172-31-31-235:~$ sudo docker ps -a

#output:
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS         NAMES           
1946f83d53a0        ubuntu              "/bin/bash"                                             goofy_panini(DOCKER'ın verdiği defaultname)

# If we want to specify a particular container name 
ubuntu@ip-172-31-31-235:~$ sudo docker run --name clarusway -i -t ubuntu /bin/bash
#This would create a new container called clarusway.

# Names are unique. We need to delete the previous container with the same name before we can create a new one. 
ubuntu@ip-172-31-31-235:~$ sudo docker rm name

# As we see above, we stopped clarusway container. If we want, we can restart a stopped container like so:
ubuntu@ip-172-31-31-235:~$ sudo docker start container-name 
# instead of name we can write containerID

# We started the container but we are not in container bash. To go back to our container’s Bash prompt again
ubuntu@ip-172-31-31-235:~$ sudo docker attach container-name
#output :
root@2f5a96f3ccde:/#       #we are in container bash now

# exit (container stops when we exit but not deleted)
root@2f5a96f3ccde:/# exit  

ubuntu@ip-172-31-31-235:~$ sudo docker rm name   #this command deletes container

# lets check docker and container info:
ubuntu@ip-172-31-31-235:~$ sudo docker info
#output:
Client:
 Debug Mode: false

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 1  # this is still one, at the beginning it was zero 
 Server Version: 19.03.6
 Storage Driver: overlay2
  Backing Filesystem: extfs
  Supports d_type: true
  Native Overlay Diff: true
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
 Swarm: inactive
 Runtimes: runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 
 runc version: 
 init version: 
 Security Options:
  apparmor
  seccomp
   Profile: default
 Kernel Version: 5.3.0-1035-aws
 Operating System: Ubuntu 18.04.5 LTS
 OSType: linux
 Architecture: x86_64
 CPUs: 1
 Total Memory: 978.6MiB
 Name: ip-172-31-31-235
 ID: 4D23:NEPK:F4UE:YCRL:WQBD:6GIY:V3NL:OX3C:LM2Z:OEBF:VZHG:JFBZ
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Registry: https://index.docker.io/v1/
 Labels:
 Experimental: false
 Insecure Registries:
  127.0.0.0/8
 Live Restore Enabled: false

WARNING: No swap limit support

