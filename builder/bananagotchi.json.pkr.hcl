packer {
  required_plugins {
    ansible = {
      source  = "github.com/hashicorp/ansible"
      version = "~> 1"
    }
  }
}

variable "pwn_hostname" {
  type = string
}

variable "pwn_version" {
  type = string
}

source "arm-image" "bananagotchi" {
  iso_checksum      = "file:https://github.com/jayofelony/bananagotchi/releases/download/v1.0/Bpi-m4zero_1.0.0_debian_bookworm_minimal_linux6.1.31.img.xz.sha256"
  iso_url           = "https://github.com/jayofelony/bananagotchi/releases/download/v1.0/Bpi-m4zero_1.0.0_debian_bookworm_minimal_linux6.1.31.img.xz"
  image_type        = "armbian"
  image_arch        = "arm64"
  qemu_args         = ["-r", "6.1.31-sun50iw9"]
  target_image_size = 9368709120
  output_filename   = "../../../bananagotchi-$(pwn_version).img"
}

# a build block invokes sources and runs provisioning steps on them. The
# documentation for build blocks can be found here:
# https://www.packer.io/docs/from-1.5/blocks/build
build {
  name    = "bananagotchi"
  sources = ["source.arm-image.bananagotchi"]


  provisioner "file" {
    destination = "/usr/bin/"
    sources     = [
      "data/usr/bin/bettercap-launcher",
      "data/usr/bin/hdmioff",
      "data/usr/bin/hdmion",
      "data/usr/bin/monstart",
      "data/usr/bin/monstop",
      "data/usr/bin/pwnagotchi-launcher",
      "data/usr/bin/pwnlib",
    ]
  }
  provisioner "shell" {
    inline = ["chmod +x /usr/bin/*"]
  }

  provisioner "file" {
    destination = "/etc/systemd/system/"
    sources     = [
      "data/etc/systemd/system/bettercap.service",
      "data/etc/systemd/system/pwnagotchi.service",
      "data/etc/systemd/system/pwngrid-peer.service",
    ]
  }

  provisioner "file" {
    destination = "/etc/update-motd.d/01-motd"
    source      = "data/etc/update-motd.d/01-motd"
  }
  provisioner "shell" {
    inline = ["chmod +x /etc/update-motd.d/*"]
  }
  provisioner "shell" {
    inline = [
      "apt-get -y --allow-releaseinfo-change update",
      "apt-get -y dist-upgrade",
      "apt-get install -y --no-install-recommends ansible"
    ]
  }
  provisioner "ansible-local" {
    command         = "ANSIBLE_FORCE_COLOR=1 PYTHONUNBUFFERED=1 PWN_VERSION=${var.pwn_version} PWN_HOSTNAME=${var.pwn_hostname} ansible-playbook"
    extra_arguments = ["--extra-vars \"ansible_python_interpreter=/usr/bin/python3\""]
    playbook_file   = "bananagotchi.yml"
  }
}