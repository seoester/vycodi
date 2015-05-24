import argh
import json
from vycodi.utils import loadJSONConfig, redisFromConfig
from vycodi.host import fromConfig as hostDaemonFromConfig

@argh.named("start")
def startHost(configFile, foreground=False):
	config = loadJSONConfig(configFile)
	hostDaemon = hostDaemonFromConfig(None, config, daemonize=not foreground)
	hostDaemon.start()

@argh.named("stop")
def stopHost(configFile):
	config = loadJSONConfig(configFile)
	hostDaemon = hostDaemonFromConfig(None, config)
	hostDaemon.stop()

@argh.named("status")
def statusHost(configFile):
	config = loadJSONConfig(configFile)
	hostDaemon = hostDaemonFromConfig(None, config)
	if hostDaemon.status():
		print("host daemon running")
	else:
		print("host daemon not running")

parser = argh.ArghParser()
parser.add_commands((startHost, stopHost, statusHost), namespace="host")

def main():
	parser.dispatch()

if __name__ == '__main__':
	main()