
# Install
Instructions here: https://docs.docker.com/get-started/

Installation here: https://docs.docker.com/install/

Add yourself to the docker group so you don't need `sudo`:

    sudo groupadd docker
    sudo usermod -aG docker pteehan

Then restart (log out and log back in)

Confirm it works:

     docker run hello-world

### Configure to start on boot
