def start_html():
    print('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Vjezba 3</title>
            <style>
                .container {
                    margin: 0 auto;
                    width: 80%;
                    text-align: center;
                }

                table {
                    border: 2px solid gray;
                    border-collapse: collapse;
                    margin: 0 auto;
                }

                table caption {
                    padding: 8px;
                }

                input {
                	font-size: 15px;
                }

                table th,
                table td {
                    padding: 8px;
                    border: 2px solid grey;
                }
            </style>
        </head>
        <body>
        <div class="container">
    ''')

def finish_html():
    print('''</div>
        </body>
        </html>''')

