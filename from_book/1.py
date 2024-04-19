import cv2
import time
#加载训练模型
face_detect=cv2.CascadeClassifier(r"./data1/lbpcascade_frontalface_improved.xml")
cap=cv2.VideoCapture(0)
while cap.isOpened():
    #读取摄像头画面
    frla,img=cap.read()
    #画面翻转y轴
    img=cv2.flip(img,1)
    #视频图片经过灰色处理后只有黑白两种颜色，像素的位置并不会改变，便于像素识别
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #进行人脸检测
    faces = face_detect.detectMultiScale(
        img_gray, #进行检测的灰度图片
        scaleFactor=1.02,#将检测图片放大1.02被
        minNeighbors=5)#表示构成检测目标的相邻矩形的最小个数(默认为3个)，这里设置了5个。
    #判断是否有人脸
    if len(faces):
        #遍历检测到的人脸
        for x,y,w,h in faces:
            #绘制人脸矩形框
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    if cv2.waitKey(30) & 0xff == ord('q'):
        break
    if cv2.waitKey(30)&0xff == ord('s'):#按s键保存图片
        timer=time.time()#获取时间戳
        name=str(int(timer))+".jpg"#将时间戳转换成字符串类型和.jpg拼接，用作下一步的保存图片的名字
        cv2.imwrite(name,img)#保存图片
        print("图片保存成功")
    #显示人脸
    cv2.imshow("face",img)
#释放摄像头
cap.release()
#销毁窗口
cv2.destroyAllWindows()