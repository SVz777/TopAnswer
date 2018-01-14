import os
import subprocess
from PIL import Image

from config.config import pix, DEBUG, ocrPath
from lib.device import Device

from PIL.PngImagePlugin import PngImageFile


class Ocr(object):

    def __init__(self, app, count, lang="-l chi_sim+normal", cleanup=False):
        self.app=app
        self.count=count
        self.lang=lang
        self.cleanup=cleanup
        if not DEBUG:
            Device.init()
        self.device=Device.getDevice()

    def __binarizing(self,img:PngImageFile,threshold):
        pixdata = img.load()
        w, h = img.size
        for y in range(h):
            for x in range(w):
                if pixdata[x, y] < threshold:
                    pixdata[x, y] = 0
                else:
                    pixdata[x, y] = 255
        return img

    def ocr_img_count(self):
        if not DEBUG:
            self.__screencap()
        self.__img_processing()
        question=f"../screen/{self.app}/{self.count}_question.png"
        choices=f"../screen/{self.app}/{self.count}_choices.png"
        subprocess.call(ocrPath+' '+self.lang+' ' + question + ' ' +
                                question,shell=True)  # 生成同名txt文件
        qtxt = ''
        with open(question + '.txt', 'r',encoding='utf8') as f:
            qtxt = f.read().strip().replace('\n','').replace(' ','')
        if self.cleanup:
            os.remove(question + '.txt')

        subprocess.call(ocrPath+' '+self.lang+' ' + choices + ' ' +
                                choices,shell=True)  # 生成同名txt文件
        ctxt = ''
        with open(choices + '.txt', 'r',encoding='utf8') as f:
            ctxt = f.read().strip().split('\n')
            ctxt=[x.replace(' ','') for x in ctxt if x!='' and x!=' ']
        if self.cleanup:
            os.remove(choices + '.txt')
        self.count+=1
        return qtxt,ctxt

    def image_to_string(self,img:str, cleanup=True,lang='-l chi_sim',plus=''):
        # cleanup为True则识别完成后删除生成的文本文件
        # plus参数为给tesseract的附加高级参数
        subprocess.call(ocrPath+' '+lang+' ' + img + ' ' +
                                                           img + plus,shell=True)  # 生成同名txt文件
        text = ''
        with open(img + '.txt', 'r',encoding='utf8') as f:
            text = f.read().strip()
        if cleanup:
            os.remove(img + '.txt')
        return text.replace(' ','')

    def __screencap(self):
        path=f"../screen/{self.app}/{self.count}.png"
        subprocess.call(f"../adb -s {self.device} shell screencap -p /sdcard/1.png")
        subprocess.call(f"../adb -s {self.device} pull /sdcard/1.png "+path)

    def __img_processing(self):

        image=Image.open(f"../screen/{self.app}/{self.count}.png")
        image=image.transpose(Image.ROTATE_90)
        question=image.crop(pix[self.app]['question'])
        question=question.convert('L')
        question=self.__binarizing(question,190)
        choices=image.crop(pix[self.app]['choices'])
        choices=choices.convert('L')
        choices=self.__binarizing(choices,190)
        question.save(f"../screen/{self.app}/{self.count}_question.png")
        choices.save(f"../screen/{self.app}/{self.count}_choices.png")
        return True