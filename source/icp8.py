import tensorflow as tf
# create three axb matrix
a = tf.constant([4, 5])
# this tensor has a value of 4,5

b= tf.constant([5, 3])
# this tensor has a value of 5,3.

c = tf.constant([3, 5])
# this tensor has a value of 3,5

d = tf.add(a ** 2, b)
# sqaure matrix a and add it to matrix b

total = tf.multiply(d, c)
# multiplying matrix d to mattrix c

with tf.Session() as sess:
    print(sess.run(total))

matrix1 = tf.constant(2, shape=[2, 2])
# matrix number 1 creation
matrix2 = tf.constant(5, shape=[2, 2])
# matrix number 2
matrix3 = tf.constant(7, shape=[2, 4])
# creating another matrix
total1 = tf.add(matrix1 ** 2, matrix2)
# adding the two matrixes
total2 = tf.matmul(total1, matrix3)
# we use matmul cause different matrix size

with tf.Session() as sess:
    print (sess.run(total2))