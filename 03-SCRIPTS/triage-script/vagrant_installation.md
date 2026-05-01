
# Installing Vagrant on a Vultr Server running Debian GNU/Linux
    sudo apt update
    sudo apt install -y [docker.io](http://docker.io/) vagrant
    sudo systemctl enable --now docker
    vagrant init generic/debian12

# Vagrantfile Configuration
    Vagrant.configure("2") do |config|
    config.vm.provider "docker" do |d|
    # Use Debian 12 base image
    d.image = "roboxes/debian12:latest"

 # Keep the container running
    d.remains_running = true 
    d.cmd = ["/bin/bash", "-c", "while true; do sleep 1000; done"]

    # Map container SSH port (22) to host port 2222
    d.ports = ["2222:22"]
    end
  
# Install and enable SSH in the container
    config.vm.provision "shell", inline: <<-SHELL
    apt update -y
    apt install -y openssh-server sudo
    mkdir -p /var/run/sshd
    echo 'root:vagrant' | chpasswd
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
    systemctl enable ssh
    systemctl restart ssh`
    SHELL
    end

<img width="668" height="598" alt="Group 4 (2)" src="https://github.com/user-attachments/assets/4960c8da-bce0-48bf-a958-8a11b6308720" />

