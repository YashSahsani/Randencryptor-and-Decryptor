from imports import *
class Shredder:
          def listdirs(self,folder):
                  return [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]
          def pathGenerator(self):
                path = "/" # Change this
                rand = random.randrange(10)
                for i in range(rand):
                     check = None
                     try:
                        dire = self.listdirs(path)
                     except:
                           continue
                     try:
                         if(len(dire) > 0):
                                      new_rand = random.randrange(len(dire))
                                      check = dire[new_rand]
                                      startTime =  int(round(time.time() * 1000))
                                      endTime = startTime + 60
                                      while( int(round(time.time() * 1000)) < endTime):
                                                                             new_rand = random.randrange(len(dire))
                                                                             check = dire[new_rand]
                                      path = path+"/"+check
                                      dire = check
                         else:
                              break
                     except Exception as e:
                                    print(e)
                return path
          def Shredder(self):
                  try:
                     path_of_the_file = input("Enter the Path of File:")
                     skey = input("Enter the key: ")
                     count = 0
                     total_byte = 0
                     lent = 1000
                     temp = path_of_the_file.split("/")
                     name_of_the_file_with_extension = temp[-1]
                     name_of_the_file_without_extension = temp[-1].split(".")[0]
                     pathOfDesktop = os.path.expanduser("~")
                     try:
                         os.mkdir(pathOfDesktop + "/Generated")
                     except:
                         pass
                     file_generated = open(pathOfDesktop + "/Generated/" + name_of_the_file_without_extension + "_PathFile.txt",'w')
                     output_file_generated = open(pathOfDesktop + "/Generated/" + name_of_the_file_without_extension + "_PathFile.txt",'wb')
                     srcFile = open(path_of_the_file,'rb')
                     content = srcFile.read()
                     content_len= len(content)
                     srcFile.close()
                     srcFile = open(path_of_the_file,'rb')
                     while(content_len > 0):
                                flag = True
                                path = None
                                while(flag):
                                       tempPath = self.pathGenerator()
                                       try:
                                          fout = open(tempPath + "/check",'w')
                                          flag = False
                                          path = tempPath
                                          fout.close()
                                          os.remove(tempPath + "/check")
                                       except Exception as e:
                                                    flag = True
                                                    continue
                                path = path + "/" + name_of_the_file_without_extension + "_" +str(count)
                                out = open(path,'wb')
                                con = AES.encrypt(srcFile.read(100*16),skey)
                                out.write(con)
                                out.close();
                                print(path + "File Created!")
                                path = path+"-->\n"
                                output_file_generated.write(path.encode())
                                count = count + 1
                                content_len = content_len - 100*16
                     srcFile.close()
                     os.remove(path_of_the_file)
                     output_file_generated.close()
                     file_generated.close()
                  except Exception as e:
                          print(e)

