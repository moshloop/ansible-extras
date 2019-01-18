import docker
import json
client = docker.from_env()

#print (client.info())

print (json.dumps(client.images.get_registry_data('harbor.discsrv.co.za/dh-dcs/crm-gateway:4.1.0-SNAPSHOT').attrs))