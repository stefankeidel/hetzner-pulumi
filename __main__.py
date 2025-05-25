"""A Python Pulumi program"""

import pulumi
import pulumi_hcloud
import pulumi_digitalocean as do

web = do.Droplet("web",
    image="ubuntu-20-04-x64",
    name="web-1",
    region=do.Region.SGP1,
    size=do.DropletSlug.DROPLET_S1_VCPU1_GB,
    backups=False,
    ssh_keys=[3233077]
)

# Create a 100GB block storage volume
volume = do.Volume("web-volume",
    region=do.Region.SGP1,
    size=100,  # 100GB
    name="web-data",
    description="100GB block storage for web server",
    initial_filesystem_type="ext4"
)

# Attach the volume to the droplet
volume_attachment = do.VolumeAttachment("web-volume-attachment",
    droplet_id=web.id,
    volume_id=volume.id
)

# Export the droplet IP and volume details
pulumi.export("droplet_ip", web.ipv4_address)
pulumi.export("volume_id", volume.id)
pulumi.export("volume_name", volume.name)
pulumi.export("volume_size_gb", volume.size)
