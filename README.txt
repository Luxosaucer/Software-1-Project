HOW TO REQUEST:

1) Declare using local host as server using this code:

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

2) Create a queue to use using this formate

channel.queue_declare(queue='EXAMPLE')

Where exmple is the name of the queue

3)Send data using publish, following this formate

channel.basic_publish(exchange='', routing_key='EXAMPLE', body='test')

where routing_key is the same name the created queue, and body contains the data being sent

HOW TO RECEIVE:

1) Declare using local host as server using this code:

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

2) Connect to a queue to use using this formate

channel.queue_declare(queue='EXAMPLE')

3) Decode the body

Data is sent in a binary formate and must be decoded

To decode use body.decode()

4)Clean Up

After using the data from BODY its clean up using these commands:

    channel.basic_consume(queue='EXAMPLE', on_message_callback=callback, auto_ack=True)
	
	where queue is the queue name created
	
	then fanally to finish the process use   channel.start_consuming()

