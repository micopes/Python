# 정적 메소드

<hr>

정적 메소드를 지원하는 방법에는 두 가지가 있다.
> `@static method`
> `@class method`
> 

같은 점은 둘 다 인스턴스를 만들지 않아도 class의 method를 바로 실행할 수 있다는 것이다.

##### @staticmethod


```
class hello:
  num = 10
   
  @staticmethod:
  def calc(x):
    return x + 10
    
print(hello.calc(10))

# 결과
20
```

##### @classmethod

```
class hello:
  num = 10
  
  @classmethod
  def calc(cls, x):
    return x + 10

print(hello.calc(10))
# 결과
20
```

둘 다 객체를 만들지 않고 바로 해당 메소드를 사용했다. 차이점은 calc 메소드를 만들 때 **cls**라는 인자가 추가된 점이다.
잠시 뒤 cls가 무엇인지 알게 될 것이다.

이제 개념적인 차이점을 살펴보자. 만약 hello 클래스의 num 속성에 접근하려면 어떻게 해야 할까? 우선 객체로 접근하는 것이 아니기 때문에 
self.num을 사용할 수는 없다. 억지로 사용하고 싶다면 @staticmethod는 다음과 같이 해야 한다.

##### @staticmethod

```
class hello:
  num = 10
  
  @staticmethod
  def calc(x):
    return x + 10 + hello.num

print(hello.calc(10))
# 결과
30
```

정적 변수로 접근했다. 좋은 방법처럼 보이지 않는다.

##### @classmethod

```
class hello:
  num = 10
  
  @staticmethod
  def calc(x):
    return x + 10 + cls.num

print(hello.calc(10))
# 결과
30
```

class method에는 cls가 있는데 이것은 'class(클래스)'를 가리킨다. 이것으로 클래스의 어떤 속성에도 접근할 수 있다. 위 예시 또한
cls.num을 통해 hello 클래스의 num 속성에 접근했다.

만약 상속 관계가 있는 클래스들에서는 cls는 어떤 클래스를 가리킬까?

```
class hello:
    t = '내가 상속해 줬어'

    @classmethod
    def calc(cls):
        return cls.t

class hello_2(hello):
    t = '나는 상속 받았어'

print(hello_2.calc())
#결과
내가 상속해 줬어
```

상속 받은 hello_2 클래스가 t속성을 업데이트했다. cls.t가 상속시켜준 클래스에 있더라도 이는 상속받은 클래스(여기서는 hello_2)의 t속성이다
cls는 상속받은 클래스에서 먼저 찾는다.

그렇다고 @staticmethod가 필요없는 것은 아니다. 사람에 따라 성격에 맞게 사용할 수 있다. 함수지만 클래스 내부에 넣고 싶으면 사용한다.

@classmethod는 클래스의 어떤 옵션을 바꾸는 용도로 사용할 수 있다.




[출처] https://wikidocs.net/21054
