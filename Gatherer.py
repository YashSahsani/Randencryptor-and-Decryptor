from imports import  *
class Gatherer:
       def gatherer(self):
           generated_file = input("Enter the name of the file:")
           skey = input("Enter the key :")
           temp = generated_file.split(".")
           generated_file_without_extension = temp[0]
           pathOfDesktop = os.path.expanduser("~")
           pathFile = pathOfDesktop + "/Generated/" +generated_file_without_extension+"_PathFile.txt" 
           generate = pathOfDesktop+ "/" + generated_file
           pathFile = str(pathFile)
           try:
               filetoread = open(pathFile,'r')
           except:
               print("Enter correct filename or something went wrong")
           filetowrite = open(os.getcwd()+"/"+generated_file,'wb')
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
                        pass
           filetoread.close()
           filetowrite.close()
           os.remove(pathFile)
           os.rmdir(pathOfDesktop+"/Generated")
