import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://github.com/JunBumShee" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["blue", "blue"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "박수현")
write("description", "대구중학교")
write("button", "기터브")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "생년월일": "2007년 11월 3일",
  "좋아하는것": "게임",
  "잘하는것": "롤",
  "싫어하는것": "공부"
}
information(informations)
