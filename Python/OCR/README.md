# 简介：

​	此程序用于识别图片中的文字、对比两幅图片中文字的不同，主要针对缺字多字比较，不支持图片文本格式比对，可辅助人工审核，加快审核速度.

# 注意：

- 图片要求整洁干净，不能含过多花哨的元素、背景，最好一幅图片全为文字
- 建议一张图片只含一个连续的段落，精度极高，否则若对全文多段落识别对比，准确度会急剧下降
- 识别出的中文文本默认去除所有空格，这意味中文文本还需要人工审核图片中的文本是否含空格，英文文本默认不去空格（可调节 main.py 参数）.

# 配置：

- python 版本建议 3.6~3.9 之间
- 调试电脑建议 opencv-python 版本 4.3.0.38
- 调试电脑建议 pytesseract 版本 0.3.7
- 安装 language 文件夹的 tesseract-ocr-setup-4.00.00dev.exe 后端引擎
- 设置后端引擎 Tesseract-OCR 和 Tesseract-OCR\tessdata 的环境变量
- 修改 main.py 文件的 cls( ) 函数 os.environ['TESSDATA_PREFIX'] = r'A:\OCR\Tesseract-OCR\tessdata'，换成后端引擎相应的路径
- 把 language 文件夹的 chi_sim.traineddata 和 chi_tra.traineddata 两个训练好的中文字体拷贝到 Tesseract-OCR\tessdata 后端引擎文件夹.

# Push：

​	已同步.

# 使用：

​	把段落图片截图，放在和 main.py 同级根目录下（别的路径也行，但 input 参数的时候需要输入正确路径），在 main.py 同级路径下打开 cmd 终端控制台，输入：

python main.py

回车执行，对照 OCR效果.mp4 视频即可.

# Update：

​	简易程序，不更新升级，有问题可联系.

