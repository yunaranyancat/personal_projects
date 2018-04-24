import argparse

def caesar_cipher(filename_to_read,filename_to_append,mode):
    with open(filename_to_read, "r+") as thefile:
        lines = thefile.readlines()
        if (mode=="encrypt"):
            with open(filename_to_append, 'w+') as theEncryptedFile:
                for each_line in lines:
                    encrypted_text = encrypt_text(each_line)
                    theEncryptedFile.write(encrypted_text)

        elif (mode=="decrypt"):
            with open(filename_to_append, 'w+') as theDecryptedFile:
                for each_line in lines:
                    decrypted_text = decrypt_text(each_line)
                    theDecryptedFile.write(decrypted_text)


def encrypt_text(text):
    words = ''
    for each_line in text:
        if (32 < ord(each_line) < 123):
            words += chr(ord(each_line)+3)
        else:
            words += each_line
    return words

def decrypt_text(text):
    words = ''
    for each_line in text:
        if (32 < (ord(each_line)-3) < 123):
            words += chr(ord(each_line)-3)
        else:
            words += each_line
    return words

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The file you would like to encrypt/decrypt.", type=str)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d", "--decrypt", action="store_true")
    group.add_argument("-e", "--encrypt", action="store_true")
    parser.add_argument("-r", "--result", help="Specify filename for the encryption/decryption",type=str)

    args = parser.parse_args()

    #initialization
    getFileName = args.filename
    getResultFile = args.filename
    mode = "NOMODE"


    if args.result:
        getResultFile = args.result

    if not(args.decrypt or args.encrypt):
        parser.error("Please select one of the options, -e for encryption, -d for decryption")
    else:
        if args.decrypt:
            mode = "decrypt"
            caesar_cipher(getFileName,getResultFile,mode)
        elif args.encrypt:
            mode = "encrypt"
            caesar_cipher(getFileName,getResultFile,mode)


if __name__ == '__main__':
    main()
