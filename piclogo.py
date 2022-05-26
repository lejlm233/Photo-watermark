import os
import select
from PIL import Image,ImageDraw, ImageFont

pushimg =input("请拖入照片，路径不能为中文名")
#获取照片名称
image = Image.open(pushimg)
imgname = os.path.basename(os.path.realpath(pushimg))

#创建白色背景底图
x= int(image.width*1.25)
y=int(image.height*1.25)
impg = Image.new('RGB', (x, y),'#f9f9f9')
impg.paste(image.copy(),(int((impg.width-image.width)/2),int((impg.height-image.height)/2)))

#加入富士logo
fuji=Image.open("fuji.png")
if x>y:
    fuji2= fuji.resize((int(x/10),int(x/40)))
else:
    fuji2= fuji.resize((int(y/6),int(y/30)))
impg.paste(fuji2.copy(),(int((impg.width-fuji2.width)/2),int((image.height+(impg.height-image.height)/1.7))))

#加入照片信息
draw = ImageDraw.Draw(impg)
if x>=y:
    font = ImageFont.truetype('./legofy/times.ttf',int(impg.height/40))
else:
    font = ImageFont.truetype('./legofy/times.ttf',int(impg.width/27))
message1 = "Fujinon XF55-200mm F3.5-4.8 R LM OIS"
message2 =  "Fujinon XC16-50mm F3.5-5.6 OIS II"
message3 =  "Fujinon XC35mm F2"
message4 ="Canon EF-S 55-250mm f/4.0-5.6 IS STM"
info = str(image.info)
if message1 in info :
    message = message1
elif message2 in info :
    message = message2
elif message3 in info :
    message = message3
elif message4 in info:
    message = message4
else:
    message = input("未找到照片镜头信息，请输入：")
w, h = font.getsize(message)
draw.text((int((impg.width-w)/2),int((image.height+(impg.height-image.height)/1.2))), message,'rgb(0, 0, 0)',font=font)

#保存
#impg.show()
jpg = "jpg"
png ="png"
if jpg in imgname:
    impg.save("new"+imgname, quality=100,dpi=(300.0,300.0))
elif png in imgname:
    impg.save("new"+imgname,dpi=(300.0,300.0))
else:
    pass