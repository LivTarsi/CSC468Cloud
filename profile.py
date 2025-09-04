import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()

# Create a physical machine instead of a Xen VM
node = request.RawPC("node")
node.hardware_type = "c6525-25g"  # This is available on Utah and Wisconsin

# Use a standard Ubuntu 22 image
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD"

# Make the node externally accessible
node.routable_control_ip = True

# Add some services
node.addService(rspec.Execute(shell="/bin/sh", command="sudo apt update"))
node.addService(rspec.Execute(shell="/bin/sh", command="sudo apt install -y apache2"))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo systemctl status apache2'))

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()

