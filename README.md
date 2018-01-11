# 答题辅助
这两天一直被朋友圈刷屏直播答题 APP，
玩了两把之后发现，无论是打字搜索还是语音搜索速度都不够快
于是想着使用截图来进行文字识别自动搜索来做个小辅助的想法。


部分灵感来自：
> [答题辅助决策：冲顶大会等答题类游戏 ](https://github.com/Skyexu/TopSup)


## 具体思路

1. ADB 获取手机截屏

    因为没有安卓机 ，所以使用了[bluestacks](http://www.bluestacks.cn/)模拟器
    ```
    adb shell screencap -p /sdcard/screenshot.png
    adb pull /sdcard/screenshot.png .
    ```
   
2. OCR 识别题目与选项文字

   谷歌 [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) ，注意下载[中文字库](https://github.com/tesseract-ocr/tessdata)
3. 搜索判断

>1. 直接打开浏览器搜索问题
>2. 题目+每个选项都通过搜索引擎搜索，从网页代码中提取搜索结果计数
>3. 只用题目进行搜索，统计结果页面代码中包含选项的词频


4. 运行脚本
    ```
    cd main
    python main.py
    ```

    会自动识别文字并打开浏览器

**若屏幕分辨率不同，请在 config/config.py 中自行修改代码测试即可**

**测试时请将 config/config.py 中DEBUG修改为True**

