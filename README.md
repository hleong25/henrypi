# henrypi

A raspberry pi project that can be used as a command center for multiple input devices over USB.

# System setup

## My setup

- Raspberry Pi Zero 2 W
- 64GB micro sdcard
    - Note: don't pick a cheap one, make sure to pick a good one
    - Currently using [Samsung PRO Endurance 64GB](https://www.amazon.com/dp/B07B9KTLJZ)


## Operating System install

Use [Raspberry Pi Imager](https://www.raspberrypi.com/software/) to install the base OS.

Pick `Raspberry Pi OS Lite (64-bit)`. Currently it is debian bullseye.


## Docker install

Follow the [official docker install guide](https://docs.docker.com/engine/install/debian/).

Now, docker will only work when using `sudo`. Follow this [guide](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-debian-10#step-2-executing-the-docker-command-without-sudo-optional) so you can run docker commands without sudo.

## Docker Compose v2 install

Follow the [official docker compose v2 install guide](https://docs.docker.com/compose/cli-command/#install-on-linux).

To find the latest version, go to the [release page](https://github.com/docker/compose/releases) and find the `linux-arm7` binary.

