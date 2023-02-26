from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

# GPIO 핀 번호 설정
buzzer_pin = 18

# GPIO 핀 모드 설정
GPIO.setmode(GPIO.BCM)

# GPIO 핀 출력 설정
GPIO.setup(buzzer_pin, GPIO.OUT)

# 초기값 설정
GPIO.output(buzzer_pin, GPIO.LOW)

# 버저 주파수 값 설정
buzzer_freq = 1000  # 기본 주파수 값

# 버저 울리는 함수
def play_buzzer(frequency, duration):
    global buzzer_pin
    p = GPIO.PWM(buzzer_pin, frequency)
    p.start(50)  # PWM 신호 시작
    time.sleep(duration)  # 일정 시간 동안 대기
    p.stop()  # PWM 신호 중지

# 첫번째 버튼 눌렀을 때
@app.route('/play-buzzer-1')
def play_buzzer_1():
    global buzzer_freq
    buzzer_freq = 3500  # 주파수 값을 높여서 더 높은 음을 만듭니다.
    for i in range(3):
        play_buzzer(buzzer_freq, 0.3)  # 버저를 1초 동안 울리기
        time.sleep(1)  # 4초 동안 대기
    return index()

# 두번째 버튼 눌렀을 때
@app.route('/play-buzzer-2')
def play_buzzer_2():
    global buzzer_freq
    buzzer_freq = 3500  # 주파수 값을 더 높여서 더 높은 음을 만듭니다.
    for i in range(3):
        play_buzzer(buzzer_freq, 0.3)  # 버저를 1초 동안 울리기
        time.sleep(0.2)  # 4초 동안 대기
        play_buzzer(buzzer_freq, 0.3)  # 버저를 1초 동안 울리기
        time.sleep(1)  # 4초 동안 대기
    return index()


# 세번째 버튼 눌렀을 때
@app.route('/play-buzzer-3')
def play_buzzer_3():
    global buzzer_freq
    buzzer_freq = 3500  # 주파수 값을 더 높여서 더 높은 음을 만듭니다.
    for i in range(3):
        play_buzzer(buzzer_freq, 0.3)  # 버저를 1초 동안 울리기
        time.sleep(0.2)  # 4초 동안 대기
        play_buzzer(buzzer_freq, 0.3)  # 버저를 1초 동안 울리기
        time.sleep(0.2)  # 4초 동안 대기
        play_buzzer(buzzer_freq, 0.3)  # 버저를 1초 동안 울리기
        time.sleep(1)  # 4초 동안 대기        
    return index()

@app.route('/play-buzzer-4')
def play_buzzer_4():
    global buzzer_freq
    buzzer_freq = 3500  # 주파수 값을 더 높여서 더 높은 음을 만듭니다.
    for i in range(3):
        play_buzzer(buzzer_freq, 0.2)  # 버저를 1초 동안 울리기
        time.sleep(0.2)  # 4초 동안 대기
        play_buzzer(buzzer_freq, 0.2)  # 버저를 1초 동안 울리기
        time.sleep(0.2)  # 4초 동안 대기        
        play_buzzer(buzzer_freq, 0.2)  # 버저를 1초 동안 울리기
        time.sleep(0.2)  # 4초 동안 대기
        play_buzzer(buzzer_freq, 0.2)  # 버저를 1초 동안 울리기
        time.sleep(1)  # 4초 동안 대기        
    return index()

@app.route('/play-buzzer-5')
def play_buzzer_5():
    global buzzer_freq
    buzzer_freq = 3500  # 주파수 값을 더 높여서 더 높은 음을 만듭니다.
    for i in range(3):
        play_buzzer(buzzer_freq, 0.2)  # 버저를 1초 동안 울리기
        time.sleep(0.2)  # 4초 동안 대기
        play_buzzer(buzzer_freq, 0.2)  # 버저를 1초 동안 울리기
        time.sleep(0.2)  # 4초 동안 대기        
        play_buzzer(buzzer_freq, 0.2)  # 버저를 1초 동안 울리기
        time.sleep(0.2)  # 4초 동안 대기
        play_buzzer(buzzer_freq, 0.2)  # 버저를 1초 동안 울리기
        time.sleep(0.2)  # 4초 동안 대기
        play_buzzer(buzzer_freq, 0.2)  # 버저를 1초 동안 울리기
        time.sleep(1)  # 4초 동안 대기          
    return index()

# index.html 렌더링
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def countdown():
    minutes = int(request.form["minutes"])
    seconds = int(request.form["seconds"])
    countdown_time = minutes * 60 + seconds

    while countdown_time:
        mins, secs = divmod(countdown_time, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        countdown_time -= 1

    return render_template('index.html')

if __name__ == "__main__":
    # Flask 앱 실행
    app.run(host='192.168.0.33', port=8080, debug=True)
