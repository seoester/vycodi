import argh
from vycodi.utils import loadJSONConfig
from vycodi.host import HostDaemon
from vycodi.worker import WorkerDaemon


@argh.named("start")
def startHost(configFile, foreground=False):
	config = loadJSONConfig(configFile)
	hostDaemon = HostDaemon.fromConfig(config, daemonize=not foreground)
	hostDaemon.start()


@argh.named("stop")
def stopHost(configFile):
	config = loadJSONConfig(configFile)
	hostDaemon = HostDaemon.fromConfig(config)
	hostDaemon.stop()


@argh.named("status")
def statusHost(configFile):
	config = loadJSONConfig(configFile)
	hostDaemon = HostDaemon.fromConfig(config)
	if hostDaemon.status():
		print("host daemon running")
	else:
		print("host daemon not running")


@argh.named("start")
def startWorker(configFile, foreground=False):
	config = loadJSONConfig(configFile)
	workerDaemon = WorkerDaemon.fromConfig(config, daemonize=not foreground)
	workerDaemon.start()


@argh.named("stop")
def stopWorker(configFile):
	config = loadJSONConfig(configFile)
	workerDaemon = WorkerDaemon.fromConfig(config)
	workerDaemon.stop()


@argh.named("status")
def statusWorker(configFile):
	config = loadJSONConfig(configFile)
	workerDaemon = WorkerDaemon.fromConfig(config)
	if workerDaemon.status():
		print("Worker daemon running")
	else:
		print("Worker daemon not running")

parser = argh.ArghParser()
parser.add_commands((startHost, stopHost, statusHost), namespace="host")
parser.add_commands((startWorker, stopWorker, statusWorker), namespace="worker")


def main():
	parser.dispatch()

if __name__ == '__main__':
	main()
