# Docker Instructions
If you want to run Hackalert in a docker container, follow these instructions.

# Prerequisites
## Installing Docker

### Windows

1. Download the Docker Desktop installer from the [Docker Hub](https://hub.docker.com/editions/community/docker-ce-desktop-windows).
2. Double-click the installer to run it.
3. Follow the instructions in the installer to complete the installation.
4. Download the Docker Compose binary from the [Docker Compose GitHub repository](https://github.com/docker/compose/releases).
5. Move the binary to a directory in your system's PATH.

### Mac

1. Download the Docker Desktop installer from the [Docker Hub](https://hub.docker.com/editions/community/docker-ce-desktop-mac).
2. Double-click the installer to run it.
3. Follow the instructions in the installer to complete the installation.
4. Install Docker Compose using Homebrew:

    `brew install docker-compose`

### Linux

1. Install Docker using your distribution's package manager. For example, on Ubuntu, you can use the following command:

    `sudo apt-get install docker.io`

2. Start the Docker service:

    `sudo systemctl start docker`

> ### Note: You can also enable Docker to start automatically at boot time:
>`sudo systemctl enable docker`

3. Install Docker Compose using pip:

    `sudo pip install docker-compose`


# Docker Build and Run
1. Command to build and run HackAlert using docker compose
    ```
    docker-compose -f .\docker-compose.yml up -d --build
    ```

    > ### Note: 
    > - Ensure that Config/config.ini file exists in the local filesystem
    > - Ensure `Config/config.ini` is populated with the right API Keys for *VirusTotal* and *HaveIBeenPwned*
    > - Format of `Config/config.ini` file: 

    > ```
    > [APIKeys] 
    > VT_APIKey = 1234567890
    > HIBP_APIKey = 1234567890
    > ```

2. Log in to running container
    ```
    docker exec -it hackalert /bin/sh
    ```

3. Once inside the container `hackalert`, run the relevant python commands:

    - `python hackalert.py -h`
    - `python hackalert.py -i 8.8.8.8`
    - `python hackalert.py -e x@x.com`

