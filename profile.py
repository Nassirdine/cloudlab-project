import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
# See https://docs.cloudlab.us/geni-lib.html for more details on this api
request = portal.context.makeRequestRSpec()

# Create node requests
nodes = [request.XenVM("node")]
nodes[0].cores = 4

# Create the nodes and handle updates and initial setup
for node in nodes:
  node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
  node.routable_control_ip = "true"
  node.addService(rspec.Execute(shell="bash", command="sudo tmux new-session -d -s setup 'sudo bash /local/repository/setup;bash -i'"))

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
