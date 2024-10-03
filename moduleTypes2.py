# OS MODULE

import os
print(os.getcwd())                                                    # hangi klasördeyiz?
print(os.chdir("/Users/senanursir/PycharmProjectco/ModuleTypes2"))    # klasör değiştir.
print(os.listdir())                                                   # klasörün içeriğini listeler.
os.mkdir("bananaFolder")                                              # yeni klasör oluşturuldu (moduleTypes2 içerisine)
os.makedirs("deneme1/deneme2/deneme3")                                # iç içe klasörler oluşturuldu.
os.rmdir("bananaFolder")                                              # klasör silme
os.removedirs("deneme1/deneme2/deneme3")                              # iç içe klasörler (sadece boş klasör silinir.)


# dosyayı silebilmek için dosyanın iini tamamen sildik(gizli dosyaları da):
print(os.chdir("/Users/senanursir/PycharmProjects/ModuleTypes2/deneme1/deneme2"))
silinecek = os.listdir()[0]
os.remove(silinecek)

os.removedirs("deneme1/deneme2")

#
import os
#silinecek2 = os.listdir("/Users/senanursir/PycharmProjects/ModuleTypes2/deneme1")[0]
#os.remove("/Users/senanursir/PycharmProjects/ModuleTypes2/deneme1" +  silinecek2)
os.rmdir("deneme1")

#
os.rename("deneme1.docx","Deneme1")
os.satat("/Users/senanursir/PycharmProjects/ModuleTypes2".st_atime)

import os
for folder1, insidefolder, insidefile in os.walk("/Users/senanursir/PycharmProjects/ModuleTypes2"):
    print("folder1 :", folder1)
    print("insidefolder: ", insidefolder)
    print("insidefile: ", insidefile)
    print("")
#
import os
print(os.path.join("deneme1", "deneme2","deneme3"))    # / koyarsak koyduğumuz yeri başlangıç kabul eder.
os.path.isfile("deneme1")                              # false
os.path.splitext("U/Users/senanursir/PycharmProjects/ModuleTypes2/main.py")



