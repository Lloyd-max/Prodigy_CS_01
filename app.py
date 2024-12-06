from flask import Flask, request, jsonify

app = Flask(__name__)

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

@app.route('/encrypt', methods=['POST'])
def encrypt_text():
    data = request.get_json()
    text = data['text']
    shift = data['shift']
    encrypted = encrypt(text, shift)
    decrypted = decrypt(encrypted, shift)
    return jsonify({'encrypted': encrypted, 'decrypted': decrypted})

if __name__ == '__main__':
    app.run(debug=True)