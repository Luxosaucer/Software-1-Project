import pika, sys, os, PyPDF2
from transformers import pipeline

summarizer = pipeline("summarization",  model="t5-base", tokenizer="t5-base", framework="tf")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='sendPDF')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

        pdfGet = body.decode()
        # Open the PDF file in read-binary mode
        with open(pdfGet, 'rb') as file:
            # Create a PDF object
            pdf = PyPDF2.PdfReader(file)  
            # Get the number of pages in the PDF
            page = pdf.pages[6]
            text = page.extract_text()
            summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
            sum = (summary[0]['summary_text'])
            channel.queue_declare(queue='sendTxt')
            channel.basic_publish(exchange='', routing_key='sendTxt', body=sum)
            print(" [x] Sent 'A message getText'")


    channel.basic_consume(queue='sendPDF', on_message_callback=callback, auto_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
   
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)






