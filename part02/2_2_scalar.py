# %% [markdown]
# [구글 코랩(Colab)에서 실행하기](https://colab.research.google.com/github/lovedlim/tensorflow/blob/main/Part%202/2.1_eager_execution.ipynb) 

# %%
# tensor flow import
import tensorflow as tf

# 스칼라 정의
a = tf.constant(1)
b = tf.constant(2)
print("a:", a)
print("b:", b)


# %%
# 랭크 확인
print(tf.rank(a))

# %%
# 자료형 변환
a = tf.cast(a, tf.float32)
b = tf.cast(b, tf.float32)

print(a.dtype)
print(b.dtype)


# %%
# 덧셈
c = tf.math.add(a, b)
print("result: ", c)
print("rank: ", tf.rank(c))


# %%
# 뺄셈
print( tf.math.subtract(a, b) )

# %%
# 곱셈
print(tf.math.multiply(a, b))

# %%
# 나눗셈
print(tf.math.divide(a, b))

# %%
# 나눗셈(나머지)
print(tf.math.mod(a, b))

# %%
# 나눗셈(몫)
print(tf.math.floordiv(a, b))


