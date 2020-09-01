from imports import  *
class Gatherer:
       def gatherer(self):
           generated_file = input("Enter the name of the file:")
           skey = input("Enter the key :")
           temp = generated_file.split(".")
           generated_file_without_extension = temp[0]
           pathOfDesktop = os.path.expanduser("~/Desktop")
           pathFile = pathOfDesktop + "/Generated/" +generated_file_without_extension+"_PathFile.txt" 
           generate = pathOfDesktop+ "/" + generated_file
           pathFile = str(pathFile)
           filetoread = open(pathFile,'r')
           filetowrite = open(generate,'wb')
           paths = filetoread.read()
           singlePath = paths.split("-->")
           for path in singlePath:
                    try:
                        path = path.lstrip()
                        freadtemp = open(path,'rb')
                        blob = freadtemp.read()
                        decrypted = AES.decrypt(blob,skey)
                        filetowrite.write(decrypted)  
                        freadtemp.close()
                        os.remove(path)
                    except Exception as e:
                        print(e)
           filetoread.close()
           filetowrite.close()
           os.remove(pathFile)
           os.rmdir(pathOfDesktop+"/Generated")
