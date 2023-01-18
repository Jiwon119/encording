import pyautogui
import os
import csv
import pyperclip
import logging
from datetime import datetime

logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()

# 로그 레벨 설정
logger.setLevel(logging.INFO)

# 스트림 (터미널)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d")
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

cameraNumList = [161, 162, 163, 164, 165, 166, 167,
                 168, 233, 234, 235, 236, 237, 238, 239, 240]

# region csv 파일 읽기
data = list()
f = open("C:/Users/KimJiwon/Desktop/list.csv", 'r', encoding='cp949')
listInfo = csv.DictReader(f)
f.close

dataInfolist = []

for i in listInfo:
    dic = {}
    for k, v in i.items():

        # print("key : ", k)
        # print("value : ", v)
        dic[k] = v
    dataInfolist.append(dic)

#     print(datalist)
#     print("--------------")
# print("-------------------------------------------------------------")

# print(datalist[0]["Name"])
# print(datalist[3]["Name"])

# if dataInfolist[0]["start"] != "-":
#     print(dataInfolist[0]["start"].split(":")[0][0])
#     print(dataInfolist[0]["start"].split(":")[0][1])
#     print(dataInfolist[0]["start"].split(":")[1][0])
#     print(dataInfolist[0]["start"].split(":")[1][1])
#     print(dataInfolist[0]["start"].split(":")[2][0])
#     print(dataInfolist[0]["start"].split(":")[2][1])
# endregion


def SaveCompleted(saveFileName, userName):
    pyautogui.write(saveFileName)
    pyautogui.hotkey('alt', 'd')
    pyautogui.sleep(2)
    cameranum = saveFileName[0:3]
    camerapath = "C:/Users/KimJiwon/Desktop/test/" + userName + "/" + cameranum
    path = "C:/Users/KimJiwon/Desktop/test/" + userName
    pyperclip.copy(camerapath)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    dirError = pyautogui.locateOnScreen(
        "dirError.png", region=(677, 452, 741, 506))

    pyautogui.sleep(1)
    pyautogui.moveTo(1416, 768)
    pyautogui.click()

    file = pyautogui.locateOnScreen(
        "saveDone.png", region=(729, 159, 460, 710))

    while file is None:
        dirError = pyautogui.locateOnScreen(
            "dirError.png", region=(677, 452, 741, 506))
        if (dirError is not None):
            print("폴더 없음 오류. 폴더 생성 후 다시 저장 시도")
            logger.info(f"{userName} 폴더 없음 오류. 폴더 생성 후 다시 저장 시도")
            pyautogui.press('enter')
            os.mkdir(path)
            for i in range(161, 241, 1):
                newpath = path + "/" + str(i)
                os.mkdir(newpath)
            pyautogui.sleep(1)
            pyautogui.hotkey('alt', 'd')
            camerapath = "C:/Users/KimJiwon/Desktop/test/" + userName + "/" + cameranum
            pyperclip.copy(camerapath)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.sleep(1)
            pyautogui.press('enter')
            pyautogui.sleep(1)
            pyautogui.moveTo(1416, 768)
            pyautogui.click()
            dirError = None

        file = pyautogui.locateOnScreen(
            "saveDone.png", region=(729, 159, 460, 710))
        print("저장 진행중")
        pyautogui.sleep(1)

    pyautogui.moveTo(1020, 569)
    pyautogui.click()

    print("저장 완료")
    logger.info(f"{userName} {saveFileName}번 카메라 저장 완료")


# 카메라 클릭


def setCamera(dataNum, userName):
    checkX = 877
    checkY = 308

    startBtnX = 1037
    startBtnY = 848

    pyautogui.moveTo(checkX, checkY)
    pyautogui.click()

    # 시작 버튼으로 이동
    pyautogui.moveTo(startBtnX, startBtnY)
    pyautogui.click()
    fileName = fileNameSet(dataNum, 0, "")
    currentFileName = fileName
    SaveCompleted(fileName, userName)

    for i in range(15):
        pyautogui.moveTo(checkX, checkY)
        pyautogui.click()
        checkX += 20
        pyautogui.moveTo(checkX, checkY)
        pyautogui.click()

        # 시작 버튼으로 이동
        pyautogui.moveTo(1037, 848)
        pyautogui.click()
        fileName = fileNameSet(dataNum, i+1, currentFileName)
        SaveCompleted(fileName, userName)

    # pyautogui.moveTo(checkX, checkY)
    # pyautogui.click()
    # checkX += 19
    # pyautogui.moveTo(checkX, checkY)
    # pyautogui.click()

    # # 시작 버튼으로 이동
    # pyautogui.moveTo(1037, 848)
    # pyautogui.click()
    # SaveCompleted()

    # pyautogui.moveTo(899, 308)
    # pyautogui.click()

    # for i in range(15):
    #     pyautogui.moveTo(878, 308)
    #     pyautogui.click()
    #     pyautogui.move(20, 0)
    #     pyautogui.click()
    #     pyautogui.sleep(1)

    return True

# save 버튼 클릭하고 시간까지 입력


cameraNum = 0
currentCameraNum = 0


def fileNameSet(dataNum, cameraNum, currentFileName):
    saveFileName = str(cameraNumList[cameraNum])
    if dataInfolist[dataNum]["Name"] == dataInfolist[dataNum + 1]["Name"] or dataInfolist[dataNum]["Name"] == dataInfolist[dataNum - 1]["Name"]:
        if "_1" in saveFileName:
            saveFileName = str(cameraNumList[cameraNum]).replace("_1", "_2")
        elif "_2" in saveFileName:
            saveFileName = str(cameraNumList[cameraNum]).replace("_2", "_3")
        elif "_3" in saveFileName:
            saveFileName = str(cameraNumList[cameraNum]).replace("_3", "_4")
        else:
            saveFileName = str(cameraNumList[cameraNum]) + "_1"
    saveFileName = str(cameraNumList[cameraNum]) + "_3"
    cameraNumList[cameraNum] = saveFileName
    return saveFileName


def saveAuto(dataNum):
    # 파일이 선택되고 실행되었을때 동영상 저장 탭으로 이동
    pyautogui.moveTo(600, 230)
    pyautogui.move(280, 560)
    pyautogui.click()
    pyautogui.move(0, 80)
    pyautogui.click()

    pyautogui.sleep(0.5)

    if dataInfolist[dataNum]["start"] != "-":
        pyautogui.moveTo(1100, 213)
        pyautogui.click()
        timelist = dataInfolist[dataNum]["start"].split(":")
        pyautogui.write([timelist[0][0], timelist[0][1], "right", timelist[1][0], timelist[1][1], "right",
                         timelist[2][0], timelist[2][1]], interval=0.2)
    if dataInfolist[dataNum]["end"] != "-":
        pyautogui.moveTo(1100, 238)
        pyautogui.click()
        timelist = dataInfolist[dataNum]["end"].split(":")
        pyautogui.write([timelist[0][0], timelist[0][1], "right", timelist[1][0], timelist[1][1], "right",
                         timelist[2][0], timelist[2][1]], interval=0.2)

    setCamera(dataNum, dataInfolist[dataNum]['Name'])
    if dataInfolist[dataNum]["end"] != "-":
        cameraNumList.clear()
        cameraNumList.extend([161, 162, 163, 164, 165, 166, 167,
                              168, 233, 234, 235, 236, 237, 238, 239, 240])
    return True


num = 0
for i in dataInfolist:
    print(i["FilePath"])
    logger.info(f"{i['FilePath']} encording start")
    pyautogui.sleep(3)
    os.startfile('"{}"'.format(i["FilePath"]))
    pyautogui.sleep(3)
    saveAuto(num)
    num += 1
    pyautogui.hotkey('esc')
    pyautogui.hotkey('alt', 'f4')
    logger.info(f"{i['FilePath']} encording end")

# region 주석

# # region autoStart
# # 파일이 선택되고 실행되었을때 동영상 저장 탭으로 이동
# pyautogui.moveTo(600, 230)
# pyautogui.move(280, 560)
# pyautogui.click()
# pyautogui.move(0, 80)
# pyautogui.click()

# pyautogui.sleep(0.5)

# # 시간 설정 (엑셀로 파일 읽고 자료구조에 저장할 수 있도록 작업 필요)
# pyautogui.move(220, -657)
# pyautogui.click()

# pyautogui.write(["1", "1", "right", "0", "5", "right",
#                  "1", "1"], interval=0.5)

# # endregion


# 카메라 설정
# 1번 카메라 일단 기본으로 클릭설정
# 그 이후로는 클릭된 정보 기반으로 체크 해제 -> 다음 카메라 클릭
# 만약 그 카메라가 16번 카메라면 프로그램 종료
# for i in range(16):
#     file_check = pyautogui.locateOnScreen("check.png")
#     pyautogui.moveTo(file_check)
#     pyautogui.click()
#     pyautogui.move(20, 0)
#     pyautogui.click()
#     pyautogui.sleep(1)

# 시작 버튼 클릭 후 저장되면 이미지 찾아서 결과 리턴
# file = pyautogui.locateOnScreen("saveDone.png", grayscale=True)

# while file is None:
#     file = pyautogui.locateOnScreen("saveDone.png", grayscale=True)
#     print("저장 진행중")
#     pyautogui.sleep(1)

# pyautogui.click(file)
# print("저장 완료")

# print(pyautogui.position())

# pyautogui.sleep(3)

# print(pyautogui.position())


# pyautogui.move(-100, -600)

# endregion


# region exe 파일 읽기 주석처리함 필요 없음
# path = "D:\이화여대\영상"
# folder_list = os.listdir(path)
# filePath = "D:/이화여대/영상/" + folder_list[0]

# file_list = os.listdir(filePath)
# file_list_exe = [file for file in file_list if file.endswith(".exe")]
# print("file_list: {}".format(file_list))
# print(len(file_list_exe))


# # os.system('"D:/이화여대/영상/12.26(233~240, 161~168)/Local Host-Clip-20221226_182543"')
# f = filePath + "/" + file_list_exe[0]
# os.startfile('"{}"'.format(f))

# # while fileRead is None:
# #     print("아직 실행 안됨")
# #     # for i in range(len(file_list_exe)):
# #     #     f = filePath + "/" + file_list_exe[i]
# #     #     os.system('"{}"'.format(f))
# #     #     i += 1
# #     #     print(f)
# #     # pyautogui.sleep(3)

# pyautogui.sleep(5)

# print("실행 완료")
# endregion
