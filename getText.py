import glob
import pika

"""""
import glob, os
os.chdir("./")
for file in glob.glob("*.pdf"):
    print(file)
  """

file = input("Enter your file name: ")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='sendPDF')


channel.basic_publish(exchange='', routing_key='sendPDF', body=file)
print(" [x] Sent 'A message getText'")
connection.close()
