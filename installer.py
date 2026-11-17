def cloud_init_script():
    """Cloud-init untuk menyiapkan paket dasar setelah Droplet dibuat."""
    return """#cloud-config
package_update: true
package_upgrade: true
packages:
  - curl
  - git
  - docker.io
  - ufw
runcmd:
  - [systemctl, enable, --now, docker]
  - [usermod, -aG, docker, root]
"""
