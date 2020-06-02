import tensorflow as tf



sess = tf.InteractiveSession()

# 输入值, 只是一个实数
input_value = tf.constant(0.5, name="input_value")

# 权重, 它时一个可变量, 用Variable
weight = tf.Variable(1.0,name="weight") 

# 期望的输出值, 也就是正确答案
expected_output = tf.constant(0.0,name="expected_output")

# 计算输出值, 其实就是简单的相乘, 
output = input_value * weight

loss = (expected_output - output) ** 2

optimizer = tf.train.GradientDescentOptimizer(0.025).minimize(loss)

%matplotlib inline
sess.run(tf.global_variables_initializer())
losses = []
outputs = []
for i in range(200):
    losses.append(loss.eval())
    outputs.append(output.eval())
    sess.run(optimizer)

print('最后的预测值:', output.eval())
print('最后的loss:', loss.eval())