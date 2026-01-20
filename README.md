# pre-learning-2026
IoT개발자 과정 사전학습 리포지토리

## 1일 차
과정소개

학습 리포지토리 생성

- 마크다운 학습
1. 제목
    ```markdown
    # 제목1
    ## 제목2
    ### 제목3
    #### 제목4
    ##### 제목5
    ###### 제목6 (잘사용안함)
    <!-- 주석(HTML주석 동일) -->
    ```

2. 목록
  ```markdown
  - 목록
  * 목록
  1. 숫자목록
  2. 숫자목록
  ```

3. 링크, 이미지
    ```markdown
    [네이버](http://naver.com)
    
    ![이미지](이미지URL)
    
    ## 사이즈 조절 이미지
    src : 이미지URL
    width : 이미지 넓이 픽셀단위 지정
    <img src="이미지URL" width="500">
    ```
    - [네이버](http://naver.com)
    
    - ![이미지](https://www.fitpetmall.com/wp-content/uploads/2023/10/shutterstock_1844153299-1024x683-1.png)
    
    - <img src="https://camo.githubusercontent.com/964c6e7cf851b4607cddebae3c83e0f022a92f35fe16c3b22ec26bb0c3e292f2/68747470733a2f2f73736c2e707374617469632e6e65742f6d656c6f6e612f6c6962732f313532322f313532323032302f61613562343862376537663765316536643434635f32303235303130393137343135323633302e6a7067" width="400">
    
    <img width="259" height="194" alt="image" src="https://github.com/user-attachments/assets/796c56f1-122a-4234-8aef-631c91715dfc" />
    - 이미지와 링크는 ! 차이 밖에 없음
   
4. 가로줄
   ```markdown
   ---
   ```
---
5. 코드블럭
   - 소스코드를 작성할 때 코드하이라이팅, 영역표시 때 사용
   - 백틱(`)을 세번 후 표시언어를 입력 또는 한번 사용(인라인코드블럭)
   ```python
   print('Hello, Pythohn!') 
   ```
   - 일반적인 문장에서 한 단어를 강조하고 싶을 때 `인라인 코드블럭`을 사용
  
6. 강조 및 취소, 밑줄
   ```markdown
   **, ~~, __, html u 태그 사용, i 이탤릭
   ```
   - 문장을 작성할 시 **강조**, ~~취소선~~, __강조2__, <u>밑줄</u>, <i>이탤릭</i>을 사용할 수 있습니다.
  

- 깃허브 로컬리포지토리 생성
    1. git for windows 설치
       - https://git-scm.com/install/windows 에서 `Install for windows` 버튼 클릭
       - git for windows/x64 setup 클릭
       - `git 설치 옵션`은 기본 그대로 사용가능(변경하지말것)
       - cmd 또는 powershell 에서 `git --version`, `git -v`로 확인
    2. Github Desktop 설치
       - https://desktop.github.com/download/ 에서 다운로드 클릭, 설치
       -  계정 브라우저 연동
    3. 리포지토리 클릭
   
