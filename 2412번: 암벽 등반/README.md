# 2412번: 암벽 등반 - <img src="https://static.solved.ac/tier_small/12.svg" style="height:20px" /> Gold IV

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/2412)

<p>어떤 암벽에 n(1 ≤ n ≤ 50,000)개의 홈이 파져 있다. 각각의 홈의 좌표는 (x, y)와 같이 표현되는데, |a - x| ≤ 2이고 |b - y| ≤ 2이면 (x, y)에서 (a, b)로 이동할 수 있다. 이와 같이 홈들을 이용하여 이동하면서 y = T(1 ≤ T ≤ 200,000)일 때까지, 즉 암벽의 정상까지 오르려고 한다.</p>

<p>현재 당신이 있는 위치는 (0, 0)이다. 이 위치에서 시작하여 이동 회수를 최소로 하면서 정상에 오르려고 한다. 정상에 오를 때의 x좌표는 아무 것이나 되어도 상관이 없다.</p>

## 입력

<p>첫째 줄에 n, T가 주어진다. 다음 n개의 줄에는 각 점의 x, y좌표가 주어진다. 두 좌표는 모두 0이상이며, x좌표는 1,000,000이하, y좌표는 T이하이다. 입력에 현재 위치인 (0, 0)은 주어지지 않는다.</p>

## 출력

<p>첫째 줄에 최소 이동 회수를 출력한다. 만약, 정상에 오를 수 없으면 -1을 출력한다.</p>

## 소스코드

[소스코드 보기](암벽%20등반.py)