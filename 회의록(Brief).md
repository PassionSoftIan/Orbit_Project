# FINAL PROJECT

- 기술 회의록(기획은 README에 상세 기술이니 README 참고)

## 23/05/17

1. Front - End

2. Back - End

### 1. Front-End 진행상황

A. Front Project Frame 생성 완료

B. App.vue 에 기본적인 Nav bar 생성 완료

- Home Community Game router 링크 생성 완료

To-Do

A. 배경이미지 정상적 작동하게 만들기

B. Component 자리 배치(UI 프레임 설계) 

## 2. Back-End 진행상황

A. Back Project Frame 생성 완료

B. movies App에 Models.py 완료

C. movies App에 serializer.py 완료

D. CRUD Views.py 완료

E. CRUD URL.py 완료

F. Game App에 Views.py 완료

To-Do

A. CORS적용해서 브라우저에서 i-frame을 통해 게임 component화 해서 출력가능하게 알파테스트

B. API URL 카테고리화 해서 분류 및 문서정리

---

## 23/05/18

1. Front - End

2. Back - End

### 1. Front-End 진행상황

A. UI/Frame 구성

- App.vue 완료

- views.vue 완료

- components 완료

To-Do

A. CORS 이슈 해결

B. Community Section

- 어떤 추천 알고리즘을 만들 것인지 기획

- 

C. Home Sections

- Chat GPT API에서 어떤 질문이더라도 영화 추천 받기

- 답변 받은 영화 추천을 다시 Title만 받는 것으로 가공하여 DB와 연결

- 가독성 높일 수 있도록 하기

## 2. Back-End 진행상황

A. API Data Base 수정

- 기존 API 키 리스트 업데이트를 위해 API 요청 및 데이터 재구성

- 기존)
  
  title
  
  poster
  
  release_date
  
  genre
  
  vote_average(TMDB)
  
  over_view

- 새로운 리스트 업데이트)
  
  movie_images(스틸컷)
  
  revenue(수익, community 알고리즘 sort 를 위한 DB)
  
  video(유튜브 예고편 링크 URL)
  
  tagline(한줄 요약)

- TMDB API와 직접 소통)
  
  Actors(출연자)
  
  Director(감독자)
  
  Writer(작가)

To-Do

A. TMDB로부터 API 통신을 통해 DB 받아와서 수정하기

B. 연출부 파트 TMDB API와 직접 소통 Test 하기

- DB의 무결성을 위해 실제 DB에는 넣지 않고 직접 소통하기로 했음

---

## 23/05/19

1. Front - End

2. Back - End

## 1. Front-End 진행상황

A. Home에서 Chat-GPT와 통신하는 Input태그와 응답 출력 component 작성 완료

B. Movielist를 반복문으로 DB에서 가져와서 리스트업(Title, Over_view) 하고 각각의 리스트 Title을 누르면 영화의 Detail Page로 보내는 기능 완료

To-Do

A. Community 페이지에서 버튼을 누르면 장르, 랜덤, component출력 되도록 하기

B. Chat GPT가 아닌 영화 제목으로 영화를 검색하는 검색하는 input 만들기

C. 

## 2. Back-End 진행상황

A. 23/05/18에 진행하고자 했던 DB 업데이트 진행중

- 현재 API를 통해 새로운 데이터를 DB에 담는 것을 진행 중

- 오전 10시 DB 업데이트 완료

To-Do

A. filter기능 구현을 위해 사용자가 장르를 선택했을 때 Back_End Server로 리스트 분류를 요청

B. Server에서는 요청 받은 장르 영화를 프론트로 보내주는 기능 구현

C. 알고리즘으로 영화 추천 보여줄 수 있는 Nav Bar 에서 필요한 데이터 보내주기

- Vote_average를 기본으로 내림차순

- 수익 section은 revenue를 기준으로 내림차순

- 랜덤 section은 Vote_average 기준으로 내림차순
  
  - 이후 Gnere 별로 filter를 거쳐서 10개씩 Sever에서 Data 전송

---

## 23/05/22

1. Front - End

2. Back - End

3. Design

## 1. Front-End 진행상황

A. Auth Part 기본 기능

- Login(완료)
  
  - 외부 사이트 기반 로그인(진행중)
  
  - 로그인 form 안에서 enter 입력 시 로그인(완료)

- Logout(완료)
  
  - 창 닫으면 Local Storage Data 전부 삭제 기능(진행중)

- Sign Up(완료)
  
  - 외부 사이트 기반 회원가입(진행중)
  
  - 회원가입 form 안에서 enter 입력 시 회원가입(완료)

B. CRUD Part 기본 기능

- Review CRUD
  
  - Create(완료)
  
  - Detail(완료)
    
    - 계정이름으로 보이게하기
  
  - Update(완료)
    
    - 게시글 작성자가 아닌 다른 계정이 접근 못하게 방지 진행중(아이콘 숨기기)
    - (완료)
  
  - Delete(완료)
    
    - 게시글 작성자가 아닌 다른 계정이 접근 못하게 방지 진행중(아이콘 숨기기)
    - (완료)

C. Search Bar 기본 기능

- 자동완성기능(완료)

- 검색을 진행 했을 때 원하는 키워드 영화 리스트 나타내는 페이지로 전환(진행중)

## 2. Back-End 진행상황

A. 이전 진행 상황과 동일

To-do

1. 팔로잉 팔로우 기능

2. 좋아요 기능

3. 댓글 기능

4. 프로필 Field & serializer

## 3. Design

A. 배경 사진 적용 완료

- public index.html에 적용

B. Nav Bar 파트

- NavBar Design Frame 완료
  
  - 세부 Design (진행중)

- 반응형 버튼 기능
  
  - 화면이 축소 됐을 때 NavBar 목차를 모아놓는 버튼 기능 활성화
