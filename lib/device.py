import subprocess

from config.config import port


class Device(object):

    @classmethod
    def init(self):
        subprocess.call(f"../adb connect localhost:{port}")

    @classmethod
    def getDevice(self):
        text=subprocess.check_output('../adb devices')
        text=str(text.replace(b'\r\n',b'\n'),encoding='utf8').split('\n')
        device=None
        for d in text[1:]:
            if 'device' in d and port in d:
                device=d.split('\t')[0]
        print(device)
        return device