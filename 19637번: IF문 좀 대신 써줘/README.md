# 19637번: IF문 좀 대신 써줘 - <img src="https://static.solved.ac/tier_small/8.svg" style="height:20px" /> Silver III

<!-- performance -->
### 성능 요약
메모리: 46284 KB, 시간: 244 ms
<!-- end -->

## 문제

[문제 링크](https://boj.kr/19637)

<p>게임 개발자인 밀리는 전투력 시스템을 만들어, 캐릭터가 가진 전투력을 기준으로 칭호를 붙여주려고 한다.</p>

<p>예를 들어, 전투력 10,000 이하의 캐릭터는 WEAK, 10,000 초과 그리고 100,000 이하의 캐릭터는 NORMAL, 100,000 초과 그리고 1,000,000 이하의 캐릭터는 STRONG 칭호를 붙여준다고 하자. 이를 IF문으로 작성한다면 아래와 같이 구현할 수 있다.</p>

<pre><code>if power &lt;= 10000
print WEAK
else if power &lt;= 100000
print NORMAL
else if power &lt;= 1000000
print STRONG</code></pre>

<p>혼자서 게임을 개발하느라 매우 바쁜 밀리를 대신해서, 캐릭터의 전투력에 맞는 칭호를 출력하는 프로그램을 작성하자.</p>

## 입력

<p>첫 번째 줄에는 칭호의 개수&nbsp;<em>N</em>&nbsp;(1&nbsp;≤&nbsp;<em>N</em>&nbsp;≤ 10<sup>5</sup>)과&nbsp;칭호를 출력해야 하는 캐릭터들의 개수&nbsp;<em>M</em>&nbsp;(1&nbsp;≤&nbsp;<em>M</em> ≤ 10<sup>5</sup>)이 빈칸을 사이에 두고 주어진다.&nbsp;(1&nbsp;≤&nbsp;<em>N, M</em> ≤ 10<sup>5</sup>)</p>

<p>두 번째 줄부터&nbsp;<em>N</em>개의 줄에 각 칭호의 이름을 나타내는 길이 1 이상, 11 이하의 영어 대문자로만 구성된 문자열과 해당 칭호의 전투력 상한값을 나타내는 10<sup>9</sup>&nbsp;이하의 음이 아닌 정수가&nbsp;주어진다. 칭호는 전투력 상한값의 비내림차순으로 주어진다.&nbsp;</p>

<p><em>N&nbsp;</em>+ 2번째 줄부터<em>&nbsp;M</em>개의 각 줄에는 캐릭터의 전투력을 나타내는 음이 아닌 정수가&nbsp;주어진다. 해당하는 칭호가 없는 전투력은&nbsp;입력으로 주어지지 않는다.</p>

## 출력

<p><em>M</em>개의 줄에 걸쳐 캐릭터의 전투력에 맞는 칭호를 입력 순서대로 출력한다. 어떤 캐릭터의 전투력으로 출력할 수 있는 칭호가 여러 개인 경우 가장 먼저 입력된 칭호 하나만 출력한다.</p>

## 소스코드

[소스코드 보기](IF문%20좀%20대신%20써줘.py)