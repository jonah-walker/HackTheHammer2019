#/Users/jenniferdryden/Desktop/Hello_handwriting_sample.jpg

def detect_document(path):
    """Detects document features in an image."""
    from google.cloud import vision
    import io
    from google.oauth2 import service_account
    credentials = service_account.Credentials. from_service_account_file('C:/dev/hth/HackTheHammer2019/hackthehammerdraw-463eff03ae21.json')

    client = vision.ImageAnnotatorClient(credentials=credentials)

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))

                    for symbol in word.symbols:
                        print('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))

detect_document("C:/dev/hth/hi.jpg")