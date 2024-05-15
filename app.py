from flask import Flask, request, render_template
import lexer

app = Flask(__name__)

@app.route('/')
def index():
    tokens = []  # Inicialmente, definimos tokens como una lista vacía
    errores = lexer.errores  # Obtener la lista de errores actual
    lexer.errores = []  # Limpiar la lista de errores
    return render_template('index.html', tokens=tokens, errores=errores)

@app.route('/lex', methods=['POST'])
def lex_analysis():
    if request.method == 'POST':
        code = request.form.get('code', '')

        # Inicializar el lexer
        lexer.lexer.input(code)
        
        # Analizar tokens
        tokens = []
        while True:
            tok = lexer.lexer.token()
            if not tok:
                break
            tokens.append({
                'type': tok.type,
                'value': tok.value,
            })

        # Obtener lista de errores después del análisis léxico
        errores = lexer.errores
        lexer.errores = []  # Limpiar la lista de errores después de obtenerla

        # Renderizar la plantilla index.html con los tokens y errores
        return render_template('index.html', tokens=tokens, errores=errores)

if __name__ == '__main__':
    app.run(debug=True)
