import pwnagotchi.plugins as plugins
from threading import Lock
import subprocess
import os
import logging


class HashIt(plugins.Plugin):
    __author__ = 'Jayofelony'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = ('Check pcap file for valid hash, convert it to .22000 or remove it. '
                       'Optionally create a wordlist out of the pcap. Remove whitelisted pcaps.')

    def __init__(self, **kwargs):
        self.running = False
        self.lock = Lock()
        self.options = dict()

    def on_ready(self, agent):
        self.batch = 0
        self.removed = 0
        self.config = agent.config()
        logging.info("[HashIt] Batch converting handshakes")
        for filename in os.listdir(self.config['bettercap']['handshakes']):
            if filename.endswith('.pcap') and not filename.endswith('.22000'):
                outfile = str(filename.split('.')[0])
                subprocess.run(["/usr/bin/hcxpcapngtool", "-o", outfile + ".22000", filename], shell=True,
                               stdout=subprocess.PIPE)
                if os.path.exists(outfile + ".22000"):
                    self.batch += 1
                else:
                    self.removed += 1
                    os.remove(filename)
        if self.batch > 0:
            logging.info("[HashIt] Hashed " + str(self.batch) + " handshakes in this batch")
        elif self.removed > 0:
            logging.info("[HashIt] " + str(self.removed) + " handshakes removed in this batch")
        else:
            logging.info("HashIt] No handshakes needed hashing in this batch.")

    def on_loaded(self):
        if not os.path.exists('/usr/bin/hcxpcapngtool'):
            logging.error('[HashIt] The binary "hcxpcapngtool" is not available on your system. '
                          'Please install the latest "hcxtools" from github.com/ZerBea/hcxtools/')
            self.running = False
            return
        logging.info('[HashIt] Plugin loaded')
        self.running = True

    def on_config_changed(self, config):
        if 'wordlist' not in self.options:
            logging.debug('[HashIt] The wordlist option is not set. Setting it to False.')
            self.options['wordlist'] = bool(False)
        return

    def on_handshake(self, agent, filename, access_point, client_station):
        with self.lock:
            self.hash_output_filename = str(filename.split('.')[0])
            self.hash_output_filename = self.hash_output_filename + '.22000'
            self.hash_output_filename_wordlist = self.hash_output_filename + '.wordlist'

            if self.options['wordlist']:
                hcxpcapngtool_cmd = ["/usr/bin/hcxpcapngtool", "-E", f"{self.hash_output_filename_wordlist}", "-R",
                                     f"{self.hash_output_filename_wordlist}", "-o", f"{self.hash_output_filename}",
                                     f"{filename}"]
                subprocess.run(hcxpcapngtool_cmd)
                if not os.path.exists(self.hash_output_filename):
                    logging.info(f"[HashIt] No valid hash found in {filename}, removing file.")
                    os.remove(filename)

                hcxeiutool_cmd = ["/usr/bin/hcxeiutool", "-i", f"{self.hash_output_filename_wordlist}",
                                  "-d", f"{self.hash_output_filename_wordlist}", "-x",
                                  f"{self.hash_output_filename_wordlist}", "-c", f"{self.hash_output_filename_wordlist}",
                                  "-s", f"{self.hash_output_filename_wordlist}"]
                subprocess.run(hcxeiutool_cmd)
                logging.debug('[HashIt] Generating a wordlist from the captured handshake.')
            else:
                subprocess.run(["/usr/bin/hcxpcapngtool", "-o", self.hash_output_filename, filename], shell=True, stdout=subprocess.PIPE)
                if not os.path.exists(self.hash_output_filename):
                    os.remove(filename)
                logging.info(f"[HashIt] No valid hash found in {filename}, removing file.")
